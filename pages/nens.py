import streamlit as st
from PIL import Image
from db import Database
from datetime import datetime

st.set_page_config(
    page_title="Alumnes",
    page_icon="‍🧒",
)

db = Database()
responses = db.db["responses"]

st.page_link("app.py", label="Tornar", icon="↩️")

st.title("Quins simptomes tens?")
st.divider()

def insert_selected_simptoms(selected_simptoms):
    timestamp = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for simptom in selected_simptoms:
        existing_document = responses.find_one({"timestamp": timestamp, "simptom": simptom})
        if existing_document:
            responses.update_one({"timestamp" : timestamp, "simptom":simptom}, {"$inc": {"count": 1}})
        else:
            new_datapoint= {
                "timestamp": timestamp,
                "simptom": simptom,
                "count": 1
            }
            responses.insert_one(new_datapoint)


        

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

