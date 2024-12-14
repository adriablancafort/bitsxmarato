import streamlit as st
from PIL import Image
import os
from db import Database

db = Database()
responses_collection = db.db["responses"]
print(responses_collection.insert_one({"option": "asdasd"}))


st.page_link("app.py", label="back", icon="1️⃣")

st.title("Quins simptomes tens?")
st.divider()

image_dir = os.path.join(os.path.dirname(__file__), "../images/icons")
images = [f for f in os.listdir(image_dir) if f.endswith('.png')]

simptomes = []

for i, image in enumerate(images):
  if i % 4 == 0:
    cols = st.columns(4)
  with cols[i % 4]:
    img = Image.open(os.path.join(image_dir, image))
    img = img.resize((100, 100))
    caption = os.path.splitext(image)[0].replace('_', ' ')
    st.image(img, caption=caption)
    if st.checkbox("", key=f"checkbox_{i}"):
      simptomes.append(caption)

submit = st.button("Enviar")
if submit:
  if simptomes:
    print(responses_collection.insert_one({"option": simptomes}))
    st.success("Enviat!")
  else:
    st.error("Selecciona alguna cosa!")