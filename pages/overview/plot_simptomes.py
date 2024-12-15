import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_simptomes():
    schools = pd.read_csv('../../data/datasets/dades.csv', sep=';', encoding='latin1')
    
    schools['timestamp'] = pd.to_datetime(schools['timestamp'], format='%d/%m/%Y')
    
    columns_to_exclude = ['be', 'regular', 'malament', 'classe', 'num_alumnes']
    schools_filtered = schools.drop(columns=columns_to_exclude)
    
    schools_grouped = schools_filtered.groupby('timestamp').sum().reset_index()
    
    fig = px.line(schools_grouped, x='timestamp', y=schools_grouped.columns[1:], 
                  title="Evolució dels símptomes a Catalunya", 
                  labels={"timestamp": "Data", "value": "Casos"},
                  template="plotly_dark")
    
    return fig


def plot_be_regular_malament():
    schools = pd.read_csv('../../data/datasets/dades.csv', sep=';', encoding='latin1')
    
    schools['timestamp'] = pd.to_datetime(schools['timestamp'], format='%d/%m/%Y')
    
    #specific_day = '14/02/2024'
    specific_day = '20/02/2024'
    schools_day = schools[schools['timestamp'].dt.date == pd.to_datetime(specific_day).date()]
    
    be_sum = schools_day['be'].sum()
    regular_sum = schools_day['regular'].sum()
    malament_sum = schools_day['malament'].sum()
    
    category_sums = [be_sum, regular_sum, malament_sum]
    categories = ['Bé', 'Regular', 'Malament']
    
    fig, ax = plt.subplots(figsize=(2, 2))
    sns.set_theme(style="whitegrid")
    
    ax.pie(category_sums, labels=categories, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette("Set2", len(category_sums)))
    
    ax.set_title(f'Estat diari dels nens')
    plt.tight_layout()

    
    return fig