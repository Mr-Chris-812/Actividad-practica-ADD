import numpy as np
import pandas as pd


def cargar_datos(ruta):
    """RF-01: lee el CSV con pandas y devuelve la columna pm25_value como ndarray."""
    df = pd.read_csv(ruta)
    return df["pm25_value"].to_numpy(dtype=float)


def limpiar_nulos(datos):
    """RF-02: elimina los NaN con una mascara booleana."""
    return datos[~np.isnan(datos)]


def filtrar_anomalias(datos):
    """RF-03: descarta valores fisicamente imposibles (< 0 o > 1000)."""
    mascara = (datos >= 0) & (datos <= 1000)
    return datos[mascara]


def calcular_estadisticas(datos):
    """RF-04: KPI con funciones nativas de NumPy. Devuelve un dict de Python."""
    return {
        "media": float(np.mean(datos)),
        "mediana": float(np.median(datos)),
        "maximo": float(np.max(datos)),
        "minimo": float(np.min(datos)),
        "desviacion_tipica": float(np.std(datos)),
    }


def generar_reporte(metricas, ruta_destino):
    """RF-05: convierte el dict en DataFrame y lo guarda como CSV."""
    pd.DataFrame([metricas]).to_csv(ruta_destino, index=False)
    return True
