import streamlit as st
import pandas as pd
import time
import random
from db import Database


df = pd.read_csv('qualitat-aire-punts-mesurament-automatic-socrata.csv')
df['DATA'] = pd.to_datetime(df['DATA'])
df['TOTAL'] = sum(df[h] for h in [f'0{i}h' for i in range(1,10)]+ \
                  [f'{i:2d}h' for i in range(10,25)])
df = df[['DATA','TOTAL', 'CONTAMINANT']]
df = df.groupby(['DATA', 'CONTAMINANT']).mean().reset_index()
df = df[df['DATA'] > '2024-01-01']

db = Database()
airqual = db.db['airquality']
data = df.to_dict(orient='records')
airqual.insert_many(data)