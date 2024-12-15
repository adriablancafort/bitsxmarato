import streamlit as st
import time

CENTERS = [
    "Escola Joan Maragall",
    "Escola Miquel Carreras",
    "Escola Samuntada",
    "Escola La Romànica",
    "Escola Tarlatana",
    "Escola Roureda",
    "Escola Agnès Armengol",
    "Escola Calvet d'Estrella", 
    "Escola Pau Casals",
    "Escola Floresta",
    "Escola Torreguitart",
    "Escola Font Rosella"
]

st.set_page_config(
    page_title="Crea el teu compte",
    page_icon="📝",
    layout="centered"
)

st.title("Crea el teu compte d'Alumne")
st.subheader("Si us plau, omple les teves dades")

with st.form("registration_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Nom*")
    with col2:
        surname = st.text_input("Cognoms*")
    
    email = st.text_input("Correu electrònic*")
    
    center = st.selectbox(
        "Selecciona el teu centre*",
        options=CENTERS,
        index=None,
        placeholder="Tria el teu centre..."
    )
    
    password = st.text_input("Contrasenya*", type="password")
    password_repeat = st.text_input("Repeteix la contrasenya*", type="password")
    
    submitted = st.form_submit_button("Crear compte")
    
    if submitted:
        if not all([name, surname, email, center, password, password_repeat]):
            st.error("Si us plau, omple tots els camps obligatoris")
        elif password != password_repeat:
            st.error("Les contrasenyes no coincideixen!")
        elif len(password) < 6:
            st.error("La contrasenya ha de tenir almenys 6 caràcters")
        elif '@' not in email:
            st.error("Si us plau, introdueix un correu electrònic vàlid")
        else:
            with st.spinner("Creant el teu compte..."):
                time.sleep(1.5)
                st.success("Compte creat correctament!")
                time.sleep(1)
                st.switch_page("pages/alumnes-inicia-sessio.py")

st.page_link("pages/alumnes-inicia-sessio.py", label="Ja tens un compte? Inicia sessió")