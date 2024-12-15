import streamlit as st

st.set_page_config(
    page_title="Success!",
    page_icon="‍✅",
)

st.page_link("pages/alumnes-enquesta.py", label="Tornar a enviar",icon="↩️")
st.success("Resposta registrada!")