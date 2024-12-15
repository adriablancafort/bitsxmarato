import streamlit as st
from db import Database
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

symptoms = ["mal_de_panxa","calfreds","mal_de_cap","mal_de_coll","mocs","nas_tapat","esternut","vomits","altres","tos"]
diseases = ['Impetigen', 'Escarlatina', 'Faringoamigdalitis', 'Faringoamigdalitis estreptocòccica', 'Grip', 'Pneumònia', 'Altres IRA', 'Bronquiolitis','COVID-19']


@st.cache_data
def compute_correlation_matrix():
    db = Database()
    responses = db.db['responses']
    cursor = responses.find()


    db = Database()
    sivic = db.db['sivic']
    cursor = sivic.find()

    df = pd.DataFrame(list(cursor))

    schools = pd.read_csv('data/datasets/dades_correlation.csv')
    schools.drop(columns=['ciutat'], axis=1, inplace=True)
    schools.set_index('regio_sanitaria', inplace=True)


    sivic = pd.read_csv('data/datasets/SIVIC_grouped.csv')
    sivic = sivic.drop(columns=['data'], axis=1)
    sivic = sivic.groupby(['regio_sanitaria', 'diagnostic']).sum()
    sivic = sivic.reset_index()
    sivic = sivic.pivot(index='regio_sanitaria', columns='diagnostic', values= 'casos')


    schools_sivic = pd.merge(schools, sivic, on='regio_sanitaria', how='inner')

    columns_to_convert = [col for col in schools_sivic.columns if col != 'regio_sanitaria']
    schools_sivic[columns_to_convert] = schools_sivic[columns_to_convert].apply(pd.to_numeric, errors='coerce')


    #print(schools_sivic[sivic.columns])
    #print(schools_sivic[schools.columns])    
    #correlation = schools_sivic[sivic.columns].corrwith(schools_sivic[schools.columns], axis=0)


    correlation_matrix = schools_sivic.corr()
    filtered_correlation = correlation_matrix.loc[sivic.columns, [col for col in schools.columns if col != 'num_alumnes']]

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(filtered_correlation, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)

    return fig


def corr_matrix():
    return compute_correlation_matrix()

    