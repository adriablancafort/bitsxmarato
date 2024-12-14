import streamlit as st
import pandas as pd
import time
import random
from db import Database

schools = pd.read_csv('data/datasets/totcat-centres-educatius.csv',encoding='latin1',sep=';')


df = pd.DataFrame()
columns = ['day', 'value', 'escola', 'lat', 'lon']
df = pd.DataFrame(columns=columns)


# Extract the necessary columns for the map

schools = schools[['Coordenades_GEO_Y', 'Coordenades_GEO_X', 'Denominació_completa', 'Nom_localitat']]
schools.columns = ['lat', 'lon', 'escola', 'localitat']
schools = schools.dropna(subset=['lat', 'lon'])
schools['value'] = 0
schools = schools[schools['localitat'] == 'Barcelona']
schools = schools.sample(frac=0.7, random_state=1)
schools['lat'] = schools['lat'].str.replace(',', '.').astype(float)
schools['lon'] = schools['lon'].str.replace(',', '.').astype(float)
schools['value'] = [random.randint(0, 30) if random.random() < 0.9 else random.randint(50, 250) for _ in range(len(schools))]
schools.head()


N = len(schools)





def simulate_data(data, i):
    new_data = data[-1].copy()
    new_data['value'] = new_data.get('value', 0)  # Ensure 'value' column exists

    global j  # Ensure j is accessed as a global variable
    if random.random() < 0.10:
        # add new focuses
            #new_data.loc[new_data['escola'] == focuses[j], 'value'] = data[-1].loc[data[-1]['escola'] == 'Reina Elisenda', 'value'].values[0] + 100
            random_index = random.randint(0, len(new_data) - 1)
            new_data.loc[new_data.index[random_index], 'value'] = random.randint(70, 200)
            j = random.randint(0, len(data[-1]) - 1)


    for i in range(N):
        if random.random() > 0.30:
            new_data.loc[new_data.index[i], 'value'] = data[-1].loc[data[-1].index[i], 'value'] - random.randint(1, 20)
        else:
            new_data.loc[new_data.index[i], 'value'] = data[-1].loc[data[-1].index[i], 'value'] + random.randint(1, 35)
    
    return new_data




duration = 40
schools['time'] = 0
data = [schools]
from collections import defaultdict
db = Database()

for i in range(duration):
    new_df = simulate_data(data, i)
    new_df['time'] = i+1
    data.append(new_df)




if db.db is not None:
    sintoms = db.db['simptoms']
    insert_data = []
    for element in data:
        insert_data.extend(element.to_dict('records'))
    if insert_data:
        sintoms.insert_many(insert_data)
else:
    print("Database connection failed.")
