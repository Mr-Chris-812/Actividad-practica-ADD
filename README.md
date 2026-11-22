# Calidad del aire (PM2.5) con NumPy · Práctica RA1

Sistema modular de procesamiento de mediciones de partículas PM2.5, desarrollado con **NumPy** siguiendo la metodología **TDD** (Test-Driven Development) y un flujo de control de versiones con **Git**.

Proyecto de la actividad práctica de Análisis de Datos (RA1) · Ecosistema Python y NumPy.

> **Estado actual: Fase roja**
> Las funciones están definidas pero sin implementar (`NotImplementedError`). Los 7 tests fallan, que es el comportamiento esperado en esta fase.

## Objetivo

Procesar de forma masiva datos de sensores ambientales que contienen valores perdidos (`NaN`) y mediciones físicamente imposibles (negativas o superiores a 1000), aplicando máscaras booleanas y funciones estadísticas de NumPy.

## Dataset

Estructura basada en las exportaciones públicas de mediciones PM2.5 de la red [OpenAQ](https://openaq.org). El archivo `dummy.csv` es una muestra representativa con casos límite deliberados:

| timestamp        | location  | pm25_value |
|------------------|-----------|------------|
| 2026-11-19 00:00 | Station_A | 15.2       |
| 2026-11-19 01:00 | Station_A | *(vacío)*  |
| 2026-11-19 02:00 | Station_A | -5.0       |
| 2026-11-19 03:00 | Station_A | 45.8       |
| 2026-11-19 04:00 | Station_A | 1200.5     |
| 2026-11-19 05:00 | Station_A | 22.1       |

## Estructura del proyecto

```
├── app.ipynb        # Cuaderno principal: contiene la lógica y genera app.py
├── app.py           # Módulo generado desde el cuaderno (%%writefile)
├── dummy.csv        # Muestra de datos para las pruebas
├── pytest.ini       # Configuración de pytest
├── .gitignore
├── test/
│   └── test_app.py  # Pruebas unitarias
└── README.md
```

## Requisitos e instalación

- Python 3.10 o superior
- NumPy, Pandas, pytest e ipykernel (para ejecutar el cuaderno)

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS
python -m pip install numpy pandas pytest ipykernel
```

## Ejecución

1. Abre `app.ipynb` y ejecuta la celda `%%writefile app.py`. Esto genera el módulo `app.py`.
2. Ejecuta las pruebas:

```bash
python -m pytest test/test_app.py
```

En esta fase las pruebas **deben fallar** con `NotImplementedError`: confirman que los tests detectan la ausencia de implementación.


## Funciones

| Función | Requisito | Entrada | Salida | Estado |
|---------|-----------|---------|--------|--------|
| `cargar_datos(ruta)` | RF-01 | Ruta de un CSV | `np.ndarray` con la serie `pm25_value` | Pendiente |
| `limpiar_nulos(datos)` | RF-02 | `np.ndarray` | Array sin valores `NaN` | Pendiente |
| `filtrar_anomalias(datos)` | RF-03 | `np.ndarray` | Array sin valores `< 0` ni `> 1000` | Pendiente |
| `calcular_estadisticas(datos)` | RF-04 | `np.ndarray` validado | `dict` con media, mediana, máximo, mínimo y desviación típica | Pendiente |
| `generar_reporte(metricas, ruta)` | RF-05 | `dict` y ruta de destino | `True` tras escribir el CSV | Pendiente |

## Restricciones de diseño

- **Pandas** solo se usa para leer el CSV inicial y exportar el informe final. Todo el procesamiento intermedio es NumPy.
- **Programación funcional modular**, sin clases (no se usa POO).
- El código vive en un cuaderno Jupyter y se exporta a `app.py` con `%%writefile`, de modo que pytest lo consume de forma transparente.

## Metodología TDD y flujo Git

El desarrollo sigue el ciclo rojo, verde y refactor. Cada fase está marcada con un commit y una etiqueta:

| Fase | Tag | Descripción | Estado |
|------|-----|-------------|--------|
| Roja | `fase-roja` | Funciones con `raise NotImplementedError`; los 7 tests fallan | Fase actual |
| Verde | `fase-verde` | Implementación básica (con bucles) que supera los tests | Pendiente |
| Refactor | `refactorizado` | Sustitución de bucles por vectorización NumPy, tests en verde | Pendiente |

Para ver el historial:

```bash
git log --oneline --decorate
```

## Decisiones previstas

- **Límites incluidos:** los valores `0` y `1000` se consideran válidos. Solo se descartan los estrictamente menores que 0 o mayores que 1000.
- **Desviación típica poblacional:** se usa `np.std` con su valor por defecto (`ddof=0`).
- **Valores `float`:** las métricas se convierten a `float` nativo de Python para que el diccionario no contenga tipos de NumPy y se exporte limpiamente a CSV.
