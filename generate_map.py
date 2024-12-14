import pymongo
import streamlit as st
import pandas as pd
import time
import random
from db import Database



# Connect to MongoDB
db = Database()
# Read data from MongoDB
data = db.db['simptoms']
cursor = data.find()
df = pd.DataFrame(list(cursor))

data = []
for i in range(0,41):
    data.append(df[df['time'] == i])


map_container = st.empty()

# Inicial mapa
df = data[0]
map_container.map(df, size='value')

# Actualització del mapa en bucle
for tick in range(1, len(data)):
    time.sleep(0.1)  # Pause
    df = data[tick]
    map_container.map(df, size='value')

# Botó per regenerar
st.button("Regenerate")