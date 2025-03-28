import streamlit as st
import pandas as pd
from scraper import obtener_tarifa, obtener_tiempo_entrega

# Cargar datos de tarifas y tiempos de entrega
tarifas_df = pd.read_csv('data/tarifas.csv')
tiempos_df = pd.read_csv('data/tiempos_entrega.csv')

# Título de la aplicación
st.title("Calculador de Tarifas de Envío - Kuroneko Yamato")

# Selección de prefectura y municipio
prefectura = st.selectbox("Seleccione la prefectura de destino", tarifas_df['Prefectura'].unique())
municipios = tarifas_df[tarifas_df['Prefectura'] == prefectura]['Municipio'].unique()
municipio = st.selectbox("Seleccione el municipio de destino", municipios)

# Selección de tamaño de paquete
tamanos = ["60", "80", "100", "120", "140", "160", "180", "200"]
tamano = st.selectbox("Seleccione el tamaño del paquete", tamanos)

# Botón para calcular tarifa y tiempo de entrega
if st.button("Calcular"):
    tarifa = obtener_tarifa(prefectura, municipio, tamano)
    tiempo_regular, tiempo_express = obtener_tiempo_entrega(prefectura, municipio)
    st.write(f"**Tarifa de envío:** ¥{tarifa}")
    st.write(f"**Tiempo de entrega regular:** {tiempo_regular} días")
    st.write(f"**Tiempo de entrega exprés:** {tiempo_express} días")
