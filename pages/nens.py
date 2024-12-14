import streamlit as st
from PIL import Image
from db import Database

db = Database()
responses = db.db["respostes"]

st.page_link("app.py", label="back", icon="1️⃣")

st.title("Quins simptomes tens?")
st.divider()

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
        print(responses.insert_one({"options": selected_simptoms}))
        st.switch_page("pages/success.py")
    else:
        st.error("Selecciona almenys un simptoma")