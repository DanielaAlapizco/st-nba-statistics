import streamlit as st
from streamlit_option_menu import option_menu
import requests
import pandas as pd
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter

# Define the app configuration parameters
st.set_page_config(
    page_title="NBA Stats",  # Title
    page_icon="/content/NBA ICON.webp",  # Icon #Es necesario subirlo en content
    layout="wide",  # Layout template: wide or compact
    initial_sidebar_state="expanded"  # Define whether the sidebar appears expanded or collapsed
)

# Google Sheets URL and Sheet ID
gsheetid = '1UOd0gcbuo2SspT-zKeysub8kH75F-2QE'
sheetid = '164421049'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}'
df = pd.read_csv(url)

st.markdown("""
    <style>
    .titulo-TITULO {
        font-size: 60px;
        color: #FFFFFF;
        text-align: center;
        font-weight: bold;
    }
    .texto-NOMBRE {
        color: #FFFFFF;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# Aplicación de los estilos CSS
st.markdown('<h1 class="titulo-TITULO">NBA Statistics</h1>', unsafe_allow_html=True)
st.markdown('<p class="texto-NOMBRE">Daniela Alapizco.</p>', unsafe_allow_html=True)

with open('waves.css') as f: #Es necesario subirlo en content
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#st.title('A Random App')
#st.write('Look at the pretty waves')
st.markdown('<p class="dashboard_title">A Random App</p>', unsafe_allow_html = True)
st.markdown('<p class="dashboard_subtitle">Look at the pretty waves</p>', unsafe_allow_html = True)

# Horizontal Menu
menu_selected = option_menu(None, ["Home", "Insights", 'Prediction'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
        "container": {"background-color": "#B7A6F6"},
        "icon": {"color": "#802EF2", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#88A3E2"},
        "nav-link-selected": {"background-color": "#7A577A"},
    }
)

if menu_selected=="Insights":
    st.write("The Insights page")
    # Function for player points chart
    def load_PLAYER_chart(url):
      df = pd.read_csv(url)
      df_categories = df.groupby('player_name')['pts'].sum().reset_index()
      fig1 = px.bar(df_categories, x='player_name', y='pts', color="player_name", title="Player by Points")
      st.plotly_chart(fig1, use_container_width=True)

  # Function for team profit chart
    def load_team_chart(url):
      df = pd.read_csv(url)
      df_team = df.groupby('team_abbreviation')['reb'].mean().reset_index()
      fig2 = px.pie(df_team, values='reb', names='team_abbreviation', title='Reb by Team')
      st.plotly_chart(fig2, use_container_width=True)

  # Display charts in two columns
    c1, c2 = st.columns(2)
    with c1:
      load_PLAYER_chart(url)

    with c2:
      load_team_chart(url)

if menu_selected=="Prediction":
    st.write("The Prediction Model page")
