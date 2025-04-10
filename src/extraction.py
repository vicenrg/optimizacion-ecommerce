# 01_extraction.py (modularizado)


import numpy as np
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import inspect
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # Para cargar y mostrar la imagen

# Función para configurar pandas
def configurar_pandas():
    pd.options.display.float_format = '{:.2f}'.format 

# Función para crear la conexión a la base de datos
def conectar_base_datos():
    return sa.create_engine('sqlite:///../data/raw/ecommerce.db')

# Función para mostrar las tablas de la base de datos
def mostrar_tablas(con):
    insp = inspect(con)
    tablas = insp.get_table_names()
    print(tablas)

     # Cargar y mostrar la imagen de las tablas
    img = mpimg.imread('../images/Tablas ecommerce.png')
    plt.imshow(img)
    plt.axis('off')  # Para ocultar los ejes
    plt.show()

# Función para importar las tablas de la base de datos
def importar_tablas(con):
    oct = pd.read_sql('2019-Oct', con)
    nov = pd.read_sql('2019-Nov', con)
    dic = pd.read_sql('2019-Dec', con)
    ene = pd.read_sql('2020-Jan', con)
    feb = pd.read_sql('2020-Feb', con)
    return oct, nov, dic, ene, feb

# Función para imprimir las dimensiones de las tablas
def imprimir_dimensiones(oct, nov, dic, ene, feb):
    print(f"Total de registros y columnas en la tabla de Octubre: {oct.shape[0]} filas y {oct.shape[1]} columnas")
    print(f"Total de registros y columnas en la tabla de Noviembre: {nov.shape[0]} filas y {nov.shape[1]} columnas")
    print(f"Total de registros y columnas en la tabla de Diciembre: {dic.shape[0]} filas y {dic.shape[1]} columnas")
    print(f"Total de registros y columnas en la tabla de Enero: {ene.shape[0]} filas y {ene.shape[1]} columnas")
    print(f"Total de registros y columnas en la tabla de Febrero: {feb.shape[0]} filas y {feb.shape[1]} columnas")
    print(f"\nTotal de registros en todas las tablas: {oct.shape[0] + nov.shape[0] + dic.shape[0] + ene.shape[0] + feb.shape[0]} filas")

# Función para guardar tablas en CSV
def guardar_tablas_csv(oct, nov, dic, ene, feb):
    oct.to_csv('../data/originals/2019_Oct.csv', index=False)
    nov.to_csv('../data/originals/2019_Nov.csv', index=False)
    dic.to_csv('../data/originals/2019_Dic.csv', index=False)
    ene.to_csv('../data/originals/2020_Ene.csv', index=False)
    feb.to_csv('../data/originals/2020_Feb.csv', index=False)
    print("Las tablas han sido guardadas en archivos CSV exitosamente en 'data/originals/'")

# Función para integrar las tablas
def integrar_tablas(oct, nov, dic, ene, feb):
    data = pd.concat([oct, nov, dic, ene, feb], axis=0)
    print("Las tablas han sido unidas con apilación vertical")

    # Creamos una copia del DataFrame
    df = data.copy()
    print("Se ha creado una copia del DataFrame data para trabajar")

    # Guardamos el DataFrame integrado en un CSV
    data.to_csv("../data/originals/datos_integrados.csv", index=False)
    print("Las tablas han sido integradas y guardadas en 'data/originals/' con el nombre 'datos_integrados.csv'")
    return df

# Función para guardar el DataFrame de trabajo
def guardar_dataframe(df):
    df.to_csv("../data/originals/ecommerce.csv", index=False)
    print("El DataFrame de trabajo ha sido guardado en 'data/originals/' con el nombre 'ecommerce.csv'")

# Función para mostrar los primeros registros de los DataFrames
def visualizar_datos(data, df):
    print(f"\nTotal de registros y columnas en el DataFrame despues de la Integración: {df.shape[0]} filas y {df.shape[1]} columnas")
    print("\n----------------------------------------------------------------------")
    print("Visualizamos los primeros registros del DataFrame original 'data'")
    print(data)

    print("\n----------------------------------------------------------------------")
    print("Visualizamos los primeros registros del DataFrame de trabajo 'df'")
    print(df)
