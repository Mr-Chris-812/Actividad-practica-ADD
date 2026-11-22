"""Tests de la practica RA1 (NumPy + TDD). Usan la muestra dummy.csv."""
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from app import (
    cargar_datos,
    limpiar_nulos,
    filtrar_anomalias,
    calcular_estadisticas,
    generar_reporte,
)

RUTA_DUMMY = Path(__file__).resolve().parent.parent / "dummy.csv"


def test_cargar_datos_devuelve_ndarray():
    datos = cargar_datos(RUTA_DUMMY)
    assert isinstance(datos, np.ndarray)
    assert datos.shape == (6,)
    assert np.isnan(datos).sum() == 1


def test_limpiar_nulos_elimina_nan():
    entrada = np.array([15.2, np.nan, -5.0, 45.8, 1200.5, 22.1])
    salida = limpiar_nulos(entrada)
    assert not np.isnan(salida).any()
    assert len(salida) == 5


def test_filtrar_anomalias_descarta_negativos_y_mayores_de_1000():
    entrada = np.array([15.2, -5.0, 45.8, 1200.5, 22.1])
    salida = filtrar_anomalias(entrada)
    np.testing.assert_array_equal(salida, [15.2, 45.8, 22.1])


def test_filtrar_anomalias_conserva_limites():
    entrada = np.array([0.0, 1000.0, -0.1, 1000.1])
    salida = filtrar_anomalias(entrada)
    np.testing.assert_array_equal(salida, [0.0, 1000.0])


def test_calcular_estadisticas_con_datos_validos():
    validos = np.array([15.2, 45.8, 22.1])
    kpi = calcular_estadisticas(validos)
    assert isinstance(kpi, dict)
    assert kpi["media"] == pytest.approx(27.7)
    assert kpi["mediana"] == pytest.approx(22.1)
    assert kpi["maximo"] == pytest.approx(45.8)
    assert kpi["minimo"] == pytest.approx(15.2)
    assert kpi["desviacion_tipica"] == pytest.approx(13.1048, abs=1e-3)


def test_pipeline_completo_sobre_dummy():
    datos = cargar_datos(RUTA_DUMMY)
    datos = filtrar_anomalias(limpiar_nulos(datos))
    kpi = calcular_estadisticas(datos)
    assert kpi["media"] == pytest.approx(27.7)


def test_generar_reporte_escribe_csv(tmp_path):
    destino = tmp_path / "reporte.csv"
    metricas = {"media": 27.7, "mediana": 22.1, "maximo": 45.8,
                "minimo": 15.2, "desviacion_tipica": 13.1}
    assert generar_reporte(metricas, destino) is True
    leido = pd.read_csv(destino)
    assert leido.loc[0, "media"] == pytest.approx(27.7)
    assert set(leido.columns) == set(metricas)
