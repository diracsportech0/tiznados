import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from mplsoccer import (VerticalPitch, Pitch, create_transparent_cmap,
                       FontManager, arrowhead_marker, Sbopen)

#from Home_page import name_club, id_club
from etl import df #df_tipo1, df_tipo2
from functions import barras_apiladas

#url_powerbi = '<iframe title="Plataforma Dirac v1.1" width="900" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiOWM0YmNkMGEtMzc4Ni00MTI4LTk0OGEtZmFhNzc5NTZiYTkxIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>'
#st.markdown(url_powerbi, unsafe_allow_html=True)
colA, colB, colC = st.columns([5, 6, 2])
with colA:st.title('🎖️ MI CLUB')
with colB:pass
with colC:st.image('logo-piad.png', use_column_width=True)
#----------------------
#st.title(f'⚽ {name_club}')
#df = df[df['etapa'] != 'provincial'] #estamos obviando los partidos de la provincial

df_matches = pd.read_excel('Matches.xlsx')

#------------ 1. MENU LATERAL
menu_miclub = ['Videos','Estadísticas']
choice2 = st.sidebar.radio("Submenú - Miclub", menu_miclub, 0)

if choice2 == 'Estadísticas':
    barras_apiladas(df, 'Fase', 'output', "Acierto por fases")

if choice2 == 'Videos':
    df_matches = df_matches.dropna(subset=['video'])
    #rivales = df_matches['match_filter'].values
    etapa = set(df_matches['Etapa'].values)

    etapa_select = st.sidebar.multiselect(
        "Elige la etapa",
        etapa,
        etapa)
    #partidos_select = st.sidebar.multiselect(
    #    "Elige el rival",
    #    rivales,
    #    rivales)
    df_matches = df_matches[df_matches['Etapa'].isin(etapa_select)]
    urls_match = df_matches['video'].values

    #df_matches = df_matches[df_matches['match_filter'].isin(partidos_select)]
    n_matches = df_matches.shape[0]
    n_columns = 3
    for i in range(0, n_matches, n_columns):
        cols = st.columns(n_columns)
        for j in range(n_columns):
            if i + j < n_matches:
                cols[j].video(urls_match[i + j], muted=0)