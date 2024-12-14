import streamlit as st

st.markdown("""
    <style>
    .stButton>button {
        font-size: 24px !important;
        padding: 20px 40px !important;
        margin: 10px;
        color: white;
        background-color: #FF5733; 
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #C70039; 
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("1️⃣ Metges"):
      st.switch_page("pages/metges.py")

with col2:
    if st.button("2️⃣ Nens"):
      st.switch_page("pages/nens.py")

with col3:
    if st.button("2️⃣ Profes"):
      st.switch_page("pages/profes.py")