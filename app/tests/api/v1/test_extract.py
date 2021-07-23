from typing import Dict
import pandas as pd

from fastapi.testclient import TestClient

import app.constants as settings
import fetch


def test_create_dict(client: TestClient) -> None:
    # response = client.post(f"{settings.API_VERSION}/products", json=random_product)
    # product = response.json()
    # assert response.status_code == 200
    # assert product.get("name") == random_product.get("name")
    # assert product.get("price") == random_product.get("price")

    data = fetch.extract('https://open.canada.ca/data/dataset/3cafbe89-c98b-4b44-88f1-594e8d28838d/resource/2a4617cf'
                         '-a9df-4179-b6c6-39c5ac37e366/download/lice-count-dens-pou-2011-2019-rpt-pac-dfo-mpo'
                         '-aquaculture-eng.csv')
    assert type(data) == pd.DataFrame


def test_extract_data(client: TestClient) -> None:
    data = fetch.extract('https://open.canada.ca/data/dataset/3cafbe89-c98b-4b44-88f1-594e8d28838d/resource/2a4617cf'
                         '-a9df-4179-b6c6-39c5ac37e366/download/lice-count-dens-pou-2011-2019-rpt-pac-dfo-mpo'
                         '-aquaculture-eng.csv')
    data_t = fetch.transform(data)

    print(data_t.head(10))
    assert type(data_t) == pd.Dataframe
