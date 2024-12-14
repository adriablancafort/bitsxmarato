import streamlit as st
import folium
import geopandas as gpd
from folium import IFrame
from folium import GeoJsonTooltip

# Cargar el archivo GeoJSON con las comarcas de Cataluña
geojson_file = 'datasets/comarques.geojson'  # Modifica la ruta si es necesario

# Cargar el GeoJSON de las comarcas
comarcas_gdf = gpd.read_file(geojson_file)

# Crear un mapa centrado en Cataluña
m = folium.Map(location=[41.6, 1.2], zoom_start=8)

# Crear el GeoJSON con las comarcas
geojson_layer = folium.GeoJson(
    comarcas_gdf,
    name='Comarcas',
    tooltip=GeoJsonTooltip(
        fields=['nom_comar'],  # Asegúrate de que el campo se llama 'nom_comarca' en tu GeoJSON
        aliases=['Comarca:'],
        localize=True
    )
)

# Añadir la capa GeoJSON al mapa
geojson_layer.add_to(m)

# Función para resaltar la comarca seleccionada
def highlight_comarca(feature):
    return {
        'fillColor': 'blue',
        'color': 'blue',
        'weight': 2,
        'fillOpacity': 0.6
    }

# Función para restaurar el color original
def reset_comarca(feature):
    return {
        'fillColor': '#FFFFFF',
        'color': '#000000',
        'weight': 0.5,
        'fillOpacity': 0.1
    }

# Añadir eventos de clic en el mapa
def on_click(event):
    # Extraer el nombre de la comarca
    comarca_name = event['properties']['nom_comar']
    st.write(f"Has seleccionado la comarca: {comarca_name}")

    # Resaltar la comarca seleccionada
    geojson_layer.geojson.add_child(
        folium.GeoJson(
            comarcas_gdf[comarcas_gdf['nom_comarca'] == comarca_name],
            style_function=highlight_comarca
        )
    )
    # Cambiar el color al hacer clic para reflejar que está seleccionada
    geojson_layer.geojson.add_child(
        folium.GeoJson(
            comarcas_gdf,
            style_function=reset_comarca
        )
    )

# Mostrar el mapa interactivo de Folium en Streamlit
st.write("Selecciona una comarca haciendo clic en el mapa:")
st.components.v1.html(m._repr_html_(), height=600)
