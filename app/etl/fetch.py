import json
import csv
import os
from codecs import iterdecode
from contextlib import closing

import requests
import pandas as pd
from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from app.main import ROOT_DIR, get_db
from app.crud import create_fish_data
from app.schemas import Fish


def extract(url: str) -> pd.DataFrame:
    # r = requests.get(url)
    # open(f'{ROOT_DIR}/downloads/fishdata.csv', 'wb').write(r.content)
    with open(f'{ROOT_DIR}/downloads/fishdata.csv', 'wb') as f, \
            requests.get(url, stream=True) as r:
        for line in r.iter_lines():
            f.write(line + '\n'.encode())

    return pd.read_csv(f'{ROOT_DIR}/downloads/fishdata.csv')


def transform(data: pd.DataFrame) -> pd.DataFrame:
    # remove unnamed columns
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    # drop columns we don't care about
    data = data.drop(columns=
                     ['Latitude (Decimal Degrees)', 'Longitude (Decimal Degrees)',
                      'Number of Counts Performed', 'Average L. salmonis motiles per fish',
                      'Average L. salmonis females per fish',
                      'Average chalimus per fish',
                      'Average caligus per fish'
                      ],
                     )
    # rename columns for ease of use later
    data = data.rename(columns={
        'Facility Reference \nNumber': 'facility_ref_number',
        'Licence Holder': 'licence_holder',
        'Site Common Name': 'site_name',
        'Fish Health Zone': 'fish_health_zone',
        'Comments': 'comments',
        'Year Class': 'year_class',
    })

    # combine the 'Year' and 'Month' columns into 'Date', dropping after
    data['date'] = data['Year'].astype(str) + " " + data["Month"]
    data = data.drop(
        columns=[
            'Year',
            'Month'
        ]
    )

    # transform the values in the date column into actual datetime values
    data['date'] = data['date'].apply(lambda x: datetime.strptime(x, "%Y %B"))

    return data


def load(data: pd.DataFrame, db: Session = next(get_db())):

    for index, row in data.iterrows():
        create_fish_data(db, Fish(
            date=row['date'],
            facility_ref_number=row['facility_ref_number'],
            licence_holder=row['licence_holder'],
            site_name=row['site_name'],
            fish_health_zone=row['fish_health_zone']
        ))
    # print(data['date'])
    # data['date'] = data['date'].to_datetime()
    # data.apply(create_fish_data(db, Fish(date=data['date'],
    #                                      facility_ref_number=data['facility_ref_number'],
    #                                      licence_holder=data['licence_holder'],
    #                                      site_name=data['site_name'],
    #                                      fish_health_zone=data['fish_health_zone'])))
