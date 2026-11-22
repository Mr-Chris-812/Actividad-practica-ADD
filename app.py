import numpy as np
import pandas as pd


def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    return df["pm25_value"].to_numpy(dtype=float)


def limpiar_nulos(datos):
    resultado = []
    for x in datos:
        if not np.isnan(x):
            resultado.append(x)
    return np.array(resultado)


def filtrar_anomalias(datos):
    resultado = []
    for x in datos:
        if x >= 0 and x <= 1000:
            resultado.append(x)
    return np.array(resultado)


def calcular_estadisticas(datos):
    return {
        "media": float(np.mean(datos)),
        "mediana": float(np.median(datos)),
        "maximo": float(np.max(datos)),
        "minimo": float(np.min(datos)),
        "desviacion_tipica": float(np.std(datos)),
    }


def generar_reporte(metricas, ruta_destino):
    pd.DataFrame([metricas]).to_csv(ruta_destino, index=False)
    return True
