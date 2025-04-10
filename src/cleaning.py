# 02_cleaning.py (modularizado)

import numpy as np
import pandas as pd
import re

# Configurar visualización de pandas
pd.options.display.float_format = '{:.2f}'.format

# --------------------------------------------------
# Funciones de limpieza
# --------------------------------------------------

# Función para importar el dataset limpio desde CSV
def cargar_datos(ruta="../data/originals/ecommerce.csv"):
    df = pd.read_csv(ruta)
    print(f"Datos cargados correctamente desde {ruta}")
    return df

# Función para mostrar información general del DataFrame
def analizar_dataframe(df):
    print("- Información general del DataFrame:")
    df.info()
    print(f"\n- Filas y columnas: {df.shape[0]} filas, {df.shape[1]} columnas")
    print(f"- Índice: {df.index}")
    print(f"- Columnas: {df.columns.tolist()}\n")
    print(f"- Registros duplicados: {df.duplicated().sum()}\n")
    print(f"- Valores únicos por columna:\n{df.nunique()}\n")
    print(f"- Valores nulos por columna:\n{df.isnull().sum()}\n")

# Función para limpiar nombres de columnas y eliminar innecesarias
def limpiar_columnas(df):
    df = df.drop(columns=['index', 'category_code', 'brand'], errors='ignore')
    df.columns = [re.sub(r'[^\w\s]', '', col).lower().strip(' _').replace(' ', '_') for col in df.columns]
    df.rename(columns={
        'event_time': 'fecha',
        'event_type': 'evento',
        'product_id': 'producto',
        'category_id': 'categoria',
        'price': 'precio',
        'user_id': 'usuario',
        'user_session': 'sesion'
    }, inplace=True)
    print("Columnas renombradas y limpiadas correctamente")
    return df

# Función para convertir tipos de datos
def convertir_tipos(df):
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce').dt.tz_localize(None)
    df['evento'] = df['evento'].astype('category')
    print("Conversión de tipos completada")
    print(df.info())
    return df

# Función para eliminar registros con nulos
def eliminar_nulos(df):
    print(f"- Valores nulos por columna:\n{df.isnull().sum()}\n")
    print(f"- Registros antes de eliminar nulos: {df.shape[0]}")
    inicial = df.shape[0]
    df = df.dropna()
    final = df.shape[0]
    print(f"Eliminados {inicial - final} registros con valores nulos")
    print(f"Registros después de eliminar nulos: {df.shape[0]}")
    print(f"\n- Valores nulos por columna:\n{df.isnull().sum()}")
    return df

# Función para eliminar precios negativos o cero
def eliminar_precios_invalidos(df):
    print(f"- Cantidad de registros con precio menor o igual a 0: {df[df.precio <= 0].shape[0]}") 
    print(f"\nFrecuencia de los productos con precio <= 0: {df[df.precio <= 0].producto.value_counts().head(10)}")
    print(f"\n- Número de registros antes de eliminar precios <= 0: {df.shape[0]}")
    inicial = df.shape[0]
    df = df[df['precio'] > 0]
    final = df.shape[0]
    print(f"Eliminados {inicial - final} registros con precio <= 0")
    print(f"- Número de registros después de eliminar precios <= 0: {df.shape[0]}")
    return df

# Función para guardar el DataFrame limpio
def guardar_datos(df, ruta_pickle="../data/processed/ecommerce_cleaning.pkl", ruta_csv="../data/processed/ecommerce_cleaning.csv"):
    df.to_pickle(ruta_pickle)
    df.to_csv(ruta_csv, index=False)
    print(f"Datos guardados en '{ruta_pickle}' y '{ruta_csv}'")

# Función principal de limpieza
def ejecutar_proceso_limpieza():
    df = cargar_datos()
    analizar_dataframe(df)
    df = limpiar_columnas(df)
    df = convertir_tipos(df)
    df = eliminar_nulos(df)
    df = eliminar_precios_invalidos(df)
    guardar_datos(df)

# Ejecutar si se llama desde línea de comandos
if __name__ == "__main__":
    ejecutar_proceso_limpieza()
