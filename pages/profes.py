import streamlit as st
from db import Database

st.page_link("app.py", label="back", icon="1️⃣")

db = Database()
profes = db.get_collection("profes")

# Extract and display all "name" values
names = [profe['name'] for profe in profes]
st.write("List of Profes Names:")
st.write(names)
