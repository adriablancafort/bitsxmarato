import streamlit as st


st.set_page_config(
    page_title="La lluita continua",
    page_icon="🦠",
)

st.markdown("""
    <style>
    p{
       font-size: 20pt !important;
    }
    .stButton>button {
        width: 300px;
        height: 300px;
        font-size: 30pt !important;

        padding: 20px 40px !important;
        margin: 10px;
        background-color: #FF5733; 
        border: none; 
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #ffffff; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" 📈 ️La lluita continua")
st.divider()

col1, col2 = st.columns(2)
with col1:
    if st.button("👨‍⚕️️ Metges"):
      st.switch_page("pages/metges-crea-compte.py")

with col2:
    if st.button("️🧒 Alumnes"):
      st.switch_page("pages/alumnes-inicia-sessio.py")