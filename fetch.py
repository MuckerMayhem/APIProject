import json
import csv
import os
from codecs import iterdecode
from contextlib import closing

import requests
import pandas as pd
from datetime import datetime


def extract(url: str) -> pd.DataFrame:
    with open('downloads/fishdata.csv', 'wb') as f, \
            requests.get(url, stream=True) as r:
        for line in r.iter_lines():
            f.write(line + '\n'.encode())

    return pd.read_csv('downloads/fishdata.csv')


def transform(data: pd.DataFrame) -> pd.DataFrame:
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    data.drop(
        ['Latitude (Decimal Degrees)', 'Longitude (Decimal Degrees)',
         'Number of Counts Performed', 'Average L. salmonis motiles per fish',
         'Average L. salmonis females per fish',
         'Average chalimus per fish',
         'Average caligus per fish'
         ],
        axis=1)
    return data
