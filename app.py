import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Titre de l'application
st.title('Analyse des ventes e-commerce')
st.markdown("Cette application permet d'explorer les ventes d'un site e-commerce.")

#Importation des données
upload_file=st.file_uploader('Importer un fichier CSV', type='csv')
if upload_file:
    data=pd.read_csv(upload_file)
    st.write('Aperçu des données:',data.head())
else:
    data=None

#Exploration des données
st.subheader("Exploration des données")
if data is not None:
    if st.checkbox('Afficher les statistiques descriptive'):
        st.write(data.describe())
else:
    st.warning("Veuillez importer un fichier pour afficher les statistiques.")

#Visualisation des données
st.subheader("Visualisation des données")
if data is not None:
    column=st.selectbox("Sélectionner une colonne pour le graphique", data.columns)
    if st.button("Générer le graphique"):
        fig, ax=plt.subplots()
        data[column].value_counts().plot(kind='bar',ax=ax)
        st.pyplot(fig)
else:
    st.warning("Veuillez importer un fichier avant de générer un graphique.")

# Exercice 1: Ajout d'un filtre temporel
from datetime import date

st.date_input('Filter les ventes par date',date.today())

# Exercice 2: Graphiques interactifs avec plotly
import plotly.express as px

if data is not None:
    fig = px.bar(data, x=column)
    st.plotly_chart(fig)
else:
    st.warning("Veuillez importer un fichier avant de générer un graphique.")

# Exercice 3: Enregistrement des données modifiées

if data is not None:
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button('Télécharger les données', csv, 'données_modifiées.csv', 'text/csv')
else:
    st.warning("Veuillez importer un fichier avant de télécharger les données.")