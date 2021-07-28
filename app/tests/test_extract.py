import os

import pandas as pd

from fastapi.testclient import TestClient

from dotenv import load_dotenv

from app.etl import fetch
from app.main import app

from app.database import SessionLocal as TestingSessionLocal

load_dotenv()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[override_get_db()] = override_get_db

fish_url = 'https://open.canada.ca/data/dataset/3cafbe89-c98b-4b44-88f1-594e8d28838d/resource/2a4617cf-a9df-4179-b6c6-39c5ac37e366/download/lice-count-dens-pou-2011-2019-rpt-pac-dfo-mpo-aquaculture-eng.csv'


def test_create_dict(client: TestClient) -> None:
    # response = client.post(f"{settings.API_VERSION}/products", json=random_product)
    # product = response.json()
    # assert response.status_code == 200
    # assert product.get("name") == random_product.get("name")
    # assert product.get("price") == random_product.get("price")

    data = fetch.extract(fish_url)
    assert type(data) == pd.DataFrame


def test_extract_data(client: TestClient) -> None:
    data = fetch.extract(fish_url)

    assert isinstance(data, pd.DataFrame)


def test_transform_data(client: TestClient) -> None:
    data = fetch.extract(fish_url)
    data_t = fetch.transform(data)

    assert isinstance(data_t, pd.DataFrame)


def test_load_data(client: TestClient) -> None:
    fetch.load(fetch.transform(fetch.extract(fish_url)))
