import streamlit as st
from db import Database

st.page_link("app.py", label="back", icon="1️⃣")

db = Database()
profes_collection = db.db["profe"]

names = [profe['name'] for profe in profes_collection.find()]
st.write("List of Profes Names:")
st.write(names)
