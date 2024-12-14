import streamlit_authenticator_mongo as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
# from dbscript import collection

with open("auth.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    # collection,
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],

)
st.page_link("app.py", label="back", icon="1️⃣")


name, authentication_status, email = authenticator.login('Login', 'main')
print(name, authentication_status, email)