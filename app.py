import streamlit as st
from scraper import obtener_tarifa_zona

st.title("📦 Calculador de Tarifas de Envío - Kuroneko Yamato")

peso = st.number_input("Peso (kg):", min_value=0.1, step=0.1)
origen = st.text_input("Zona de Origen:")
destino = st.text_input("Zona de Destino:")

if st.button("Calcular Tarifa"):
    if peso and origen and destino:
        tarifa = obtener_tarifa_zona(peso, origen, destino)
        st.success(f"💰 Tarifa estimada: {tarifa}")
    else:
        st.error("⚠️ Por favor, ingrese todos los datos.")
