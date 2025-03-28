import pandas as pd

def obtener_tarifa(prefectura, municipio, tamano):
    tarifas_df = pd.read_csv('data/tarifas.csv')
    tarifa = tarifas_df[(tarifas_df['Prefectura'] == prefectura) &
                        (tarifas_df['Municipio'] == municipio)][tamano].values[0]
    return tarifa

def obtener_tiempo_entrega(prefectura, municipio):
    tiempos_df = pd.read_csv('data/tiempos_entrega.csv')
    tiempo_regular = tiempos_df[(tiempos_df['Prefectura'] == prefectura) &
                                (tiempos_df['Municipio'] == municipio)]['Regular'].values[0]
    tiempo_express = tiempos_df[(tiempos_df['Prefectura'] == prefectura) &
                                (tiempos_df['Municipio'] == municipio)]['Express'].values[0]
    return tiempo_regular, tiempo_express
