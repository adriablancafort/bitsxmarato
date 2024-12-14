import streamlit as st
import pandas as pd
import time

df = pd.read_csv('data.csv')

df = df[df['classe']=='Institut Torre Vicens Lleida 2n ESO  Classe1']
df = df[['num_alumnes']]
coords = pd.read_csv('totcat-centres-educatius.csv')
coords = coords[coords['Denominació_completa']=='Torre Vicens']



# Genera les coordenades
start_coords = (41.392065747410015, 2.156790852279326)
delta = 0.001

coords = [start_coords]
for i in range(9):
    coords.append((coords[-1][0] + delta, coords[-1][1] + delta))

# Crea DataFrames
dframes = [pd.DataFrame({'lat': [c[0]], 'lon': [c[1]]}) for c in coords]

# Contenidor del mapa
map_container = st.empty()

# Inicial mapa
df = dframes[0]
map_container.map(df)

# Actualització del mapa en bucle
for tick in range(1, len(dframes)):
    time.sleep(1)  # Pause
    df = dframes[tick]
    map_container.map(df)

# Botó per regenerar
st.button("Regenerate")
