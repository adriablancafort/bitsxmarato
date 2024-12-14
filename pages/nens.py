import streamlit as st
from PIL import Image
from db import Database
from datetime import datetime, date

db = Database()
responses = db.db["responses"]

st.page_link("app.py", label="back", icon="1️⃣")

st.title("Quins simptomes tens?")
st.divider()

def insert_selected_simptoms(selected_simptoms):
    timestamp = datetime.combine(date.today(), datetime.min.time())
    
    for simptom in selected_simptoms:
        data_point = {
            "timestamp": timestamp,
            "count": 1,
            "simptom": simptom
        }
        responses.insert_one(data_point)

simptoms = [
    {"name": "Diarrea", "slug": "diarrea"},
    {"name": "Esgotament", "slug": "esgotament"},
    {"name": "Mal de cap", "slug": "mal_de_cap"},
    {"name": "Mal de coll", "slug": "mal_de_coll"},
    {"name": "Mal de panxa", "slug": "mal_de_panxa"},
    {"name": "Mocs", "slug": "mocs"},
    {"name": "Tos", "slug": "tos"},
    {"name": "Vòmits", "slug": "vomits"},
    {"name": "Altres", "slug": "altres"},
]
selected_simptoms = []

for i, simptom in enumerate(simptoms):
    if i % 4 == 0:
        cols = st.columns(4)
    with cols[i % 4]:
        img = Image.open(f"images/simptoms/{simptom['slug']}.png")
        img = img.resize((100, 100))
        st.image(img, caption=simptom['name'])
        if st.checkbox("", key=f"checkbox_{i}"):
            selected_simptoms.append(simptom['slug'])

submit_button = st.button("Enviar")

if submit_button:
    if selected_simptoms:
        insert_selected_simptoms(selected_simptoms)
        st.switch_page("pages/success.py")
    else:
        st.error("Selecciona almenys un simptoma")