import streamlit as st
import pandas as pd
import os

# Verificar si los archivos existen antes de cargarlos
if not os.path.exists('data/tarifas.csv') or not os.path.exists('data/tiempos_entrega.csv'):
    st.error("❌ Error: No se encontraron los archivos de datos. Verifica que `data/tarifas.csv` y `data/tiempos_entrega.csv` estén en el repositorio.")
else:
    # Cargar datos de tarifas y tiempos de entrega
    tarifas_df = pd.read_csv('data/tarifas.csv')
    tiempos_df = pd.read_csv('data/tiempos_entrega.csv')

    # Interfaz de Streamlit
    st.title("Calculador de Tarifas de Envío - Kuroneko Yamato")

    prefectura = st.selectbox("Seleccione la prefectura de destino", tarifas_df['Prefectura'].unique())
    municipios = tarifas_df[tarifas_df['Prefectura'] == prefectura]['Municipio'].unique()
    municipio = st.selectbox("Seleccione el municipio de destino", municipios)

    tamanos = ["60", "80", "100", "120", "140", "160", "180", "200"]
    tamano = st.selectbox("Seleccione el tamaño del paquete", tamanos)

    if st.button("Calcular"):
        tarifa = tarifas_df[(tarifas_df['Prefectura'] == prefectura) &
                            (tarifas_df['Municipio'] == municipio)][tamano].values[0]

        tiempo_regular = tiempos_df[(tiempos_df['Prefectura'] == prefectura) &
                                    (tiempos_df['Municipio'] == municipio)]['Regular'].values[0]
        tiempo_express = tiempos_df[(tiempos_df['Prefectura'] == prefectura) &
                                    (tiempos_df['Municipio'] == municipio)]['Express'].values[0]

        st.write(f"**Tarifa de envío:** ¥{tarifa}")
        st.write(f"**Tiempo de entrega regular:** {tiempo_regular} días")
        st.write(f"**Tiempo de entrega exprés:** {tiempo_express} días")
