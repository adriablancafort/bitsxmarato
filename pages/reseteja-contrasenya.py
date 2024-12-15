import streamlit as st
import time

st.set_page_config(
    page_title="Reseteja Contrasenya",
    page_icon="🔑",
    layout="centered"
)

st.title("Reseteja la teva contrasenya")

with st.form("reset_password_form"):
    email = st.text_input("Correu electrònic*")
    new_password = st.text_input("Nova contrasenya*", type="password")
    confirm_password = st.text_input("Confirma la nova contrasenya*", type="password")
    
    submitted = st.form_submit_button("Canvia contrasenya")
    
    if submitted:
        if not email or not new_password or not confirm_password:
            st.error("Si us plau, omple tots els camps")
        elif '@' not in email:
            st.error("Si us plau, introdueix un correu electrònic vàlid")
        elif len(new_password) < 6:
            st.error("La contrasenya ha de tenir almenys 6 caràcters")
        elif new_password != confirm_password:
            st.error("Les contrasenyes no coincideixen")
        else:
            with st.spinner("Actualitzant contrasenya..."):
                time.sleep(1.5)
                st.success("Contrasenya actualitzada correctament!")
                time.sleep(1)
                st.switch_page("pages/alumnes-inicia-sessio.py")

st.page_link("pages/alumnes-inicia-sessio.py", label="Ja recordes la contrasenya? Inicia sessio")