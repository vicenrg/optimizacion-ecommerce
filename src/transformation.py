# 03_transformation.py (modularizado)

import numpy as np
import pandas as pd
import holidays
import re
from sqlalchemy import create_engine


def configurar_pandas():
    """
    Configura la visualización de Pandas para mostrar solo 2 decimales.
    """
    pd.options.display.float_format = '{:.2f}'.format


def cargar_datos(ruta="../data/processed/ecommerce_cleaning.pkl"):
    """
    Carga el dataset limpio desde un archivo pickle.
    """
    df = pd.read_pickle(ruta)
    print(f"Datos cargados correctamente desde {ruta}")
    return df


def extraer_componentes_fecha(df):
    """
    Extrae componentes de la fecha y crea nuevas columnas relacionadas con la fecha.
    """
    df['date'] = df['fecha'].dt.date
    df['año'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    df['dia'] = df['fecha'].dt.day
    df['hora'] = df['fecha'].dt.hour
    df['minuto'] = df['fecha'].dt.minute
    df['segundo'] = df['fecha'].dt.second
    df = df.set_index('fecha')
    df['date'] = pd.to_datetime(df['date'])
    print("Componentes de la fecha extraídos correctamente")
    return df


def agregar_festivos(df):
    """
    Agrega una columna 'festivo' que indica si el día es festivo o no (1 si es festivo, 0 si no lo es).
    """
    festivo_ru = holidays.RU(years=2020)
    print("Días festivos en Rusia:", festivo_ru)

    df['festivo'] = df['date'].apply(lambda x: 1 if x in festivo_ru else 0)

    # Mostrar registros que coinciden con fechas festivas
    print(f"\nRegistros en cada fecha festiva: \n{df.query('festivo == 1').date.value_counts().sort_index()}")
    return df

    # Filtrar las filas donde la columna 'festivo' sea igual a 1
    print(f"\nRegistros en día de fiesta:")
    display(df.query('festivo == 1'))


def agregar_indicadores_exogenos(df):
    """
    Agrega indicadores exógenos como Black Friday y San Valentín.
    """
    # Agregar indicador para Black Friday
    df['black_friday'] = 0
    df.loc['2019-11-29', 'black_friday'] = 1

    # Agregar indicador para San Valentín
    df['san_valentin'] = 0
    df.loc['2020-02-14', 'san_valentin'] = 1

    print(f"{df['black_friday'].value_counts()}")
    print(f"{df['san_valentin'].value_counts()}")
    return df


def reordenar_variables(df):
    """
    Reordena las variables del DataFrame según el orden deseado.
    """
    variables = df.columns.to_list()
    orden = ['usuario', 'sesion', 'categoria', 'evento', 'producto', 'precio']
    resto_var = [nombre for nombre in variables if nombre not in orden]

    df = df[orden + resto_var]
    print("Variables reordenadas correctamente")
    return df


def guardar_datos(df, ruta_pickle="../data/processed/ecommerce_transformado.pkl", ruta_csv="../data/originals/ecommerce_transformado.csv"):
    """
    Guarda el DataFrame transformado en formato pickle y CSV.
    """
    df.to_pickle(ruta_pickle)
    df.to_csv(ruta_csv, index=False)
    print(f"El DataFrame ha sido guardado en '{ruta_pickle}' y '{ruta_csv}'")


def guardar_en_sql(df, ruta_db="mysql+pymysql://root:MySQL.2025@localhost/ecommerce"):
    """
    Guarda el DataFrame en una base de datos SQL.
    """
    engine = create_engine(ruta_db)
    df.to_sql('ecommerce_transformado', con=engine, index=False, if_exists='replace')
    print(f"El DataFrame ha sido guardado en la base de datos SQL en la tabla 'ecommerce_transformado'")


def ejecutar_proceso_transformacion():
    """
    Función principal que ejecuta el proceso completo de transformación de datos.
    """
    df = cargar_datos()
    df = extraer_componentes_fecha(df)
    df = agregar_festivos(df)
    df = agregar_indicadores_exogenos(df)
    df = reordenar_variables(df)
    guardar_datos(df)
    guardar_en_sql(df)

# Ejecutar si se llama desde línea de comandos
# if __name__ == "__main__":
#     ejecutar_proceso_transformacion()







