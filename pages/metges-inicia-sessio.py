import streamlit as st
import time

st.set_page_config(
    page_title="Simple Login",
    page_icon="🔒",
    layout="centered"
)

st.title("Hola de nou!")
st.subheader("Inicia sessió per continuar")

with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Contrasenya", type="password")
    remember = st.checkbox("Recorda'm")
    
    submitted = st.form_submit_button("Inicia sessió")
    
    if submitted:
        with st.spinner("Iniciant sessió..."):
            time.sleep(1)
            st.success("Sessió iniciada!")
            time.sleep(0.5)
            st.switch_page("pages/metges.py")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/metges-crea-compte.py", label="No tens compte? Crea un compte")
with col2:
    st.page_link("pages/reseteja-contrasenya.py", label="Reseteja la contrasenya")