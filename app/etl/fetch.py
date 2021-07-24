import json
import csv
import os
from codecs import iterdecode
from contextlib import closing

import requests
import pandas as pd
from datetime import datetime

from app.main import ROOT_DIR, app


def extract(url: str) -> pd.DataFrame:
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

    data.rename(columns={
        'Facility Reference \nNumber': 'facility_ref',
        'License Holder': 'licence_holder',
        'Site Common Name': 'site_name',
        'Fish Health Zone': 'fish_health_zone',
        'Comments': 'comments',
        'Year Class': 'year_class',
    })

    data.apply(lambda x: datetime.datetime())

    for col in data.columns:
        print(col)
    return data
