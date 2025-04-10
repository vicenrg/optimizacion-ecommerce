# extraction.py (modularizado)

import numpy as np
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import inspect
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  # Para mostrar la imagen de las tablas


def configurar_pandas():
    """
    Configura la visualización de Pandas para mostrar solo 2 decimales.
    """
    pd.options.display.float_format = '{:.2f}'.format


def conectar_base_datos():
    """
    Crea y retorna una conexión a la base de datos SQLite.
    """
    return sa.create_engine('sqlite:///../data/raw/ecommerce.db')


def mostrar_tablas(con):
    """
    Muestra los nombres de las tablas y la imagen del esquema relacional.
    """
    insp = inspect(con)
    tablas = insp.get_table_names()
    print("Tablas en la base de datos:", tablas)

    img = mpimg.imread('../images/Tablas ecommerce.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def importar_tablas(con):
    """
    Importa las tablas mensuales desde la base de datos SQLite.
    """
    oct = pd.read_sql('2019-Oct', con)
    nov = pd.read_sql('2019-Nov', con)
    dic = pd.read_sql('2019-Dec', con)
    ene = pd.read_sql('2020-Jan', con)
    feb = pd.read_sql('2020-Feb', con)
    return oct, nov, dic, ene, feb


def imprimir_dimensiones(oct, nov, dic, ene, feb):
    """
    Imprime el número de registros y columnas de cada tabla mensual.
    """
    print(f"Octubre: {oct.shape[0]} filas, {oct.shape[1]} columnas")
    print(f"Noviembre: {nov.shape[0]} filas, {nov.shape[1]} columnas")
    print(f"Diciembre: {dic.shape[0]} filas, {dic.shape[1]} columnas")
    print(f"Enero: {ene.shape[0]} filas, {ene.shape[1]} columnas")
    print(f"Febrero: {feb.shape[0]} filas, {feb.shape[1]} columnas")
    total = oct.shape[0] + nov.shape[0] + dic.shape[0] + ene.shape[0] + feb.shape[0]
    print(f"\nTotal registros: {total} filas")


def guardar_tablas_csv(oct, nov, dic, ene, feb):
    """
    Guarda cada tabla mensual en un archivo CSV individual.
    """
    oct.to_csv('../data/originals/2019_Oct.csv', index=False)
    nov.to_csv('../data/originals/2019_Nov.csv', index=False)
    dic.to_csv('../data/originals/2019_Dic.csv', index=False)
    ene.to_csv('../data/originals/2020_Ene.csv', index=False)
    feb.to_csv('../data/originals/2020_Feb.csv', index=False)
    print("Tablas guardadas como CSV en '../data/originals/'")


def integrar_tablas(oct, nov, dic, ene, feb):
    """
    Une todas las tablas verticalmente y guarda el DataFrame combinado.
    Retorna tanto el DataFrame combinado (`data`) como su copia de trabajo (`df`).
    """
    data = pd.concat([oct, nov, dic, ene, feb], axis=0)
    print("Tablas unidas mediante apilación vertical")

    df = data.copy()
    print("Copia del DataFrame creada para trabajar")

    data.to_csv("../data/originals/datos_integrados.csv", index=False)
    print("DataFrame combinado guardado como 'datos_integrados.csv'")
    return data, df


def guardar_dataframe(df):
    """
    Guarda el DataFrame de trabajo en formato CSV.
    """
    df.to_csv("../data/originals/ecommerce.csv", index=False)
    print("DataFrame de trabajo guardado como 'ecommerce.csv'")


def visualizar_datos(data, df):
    """
    Muestra resumen de registros y los primeros registros del DataFrame original y el de trabajo.
    """
    print(f"\nRegistros totales tras integración: {df.shape[0]} filas y {df.shape[1]} columnas")
    print("\n--- Primeros registros del DataFrame original (data) ---")
    print(data.head())
    print("\n--- Primeros registros del DataFrame de trabajo (df) ---")
    print(df.head())


def ejecutar_proceso_extraccion():
    """
    Función principal que ejecuta el proceso completo de extracción de datos.
    """
    configurar_pandas()
    con = conectar_base_datos()
    mostrar_tablas(con)
    oct, nov, dic, ene, feb = importar_tablas(con)
    imprimir_dimensiones(oct, nov, dic, ene, feb)
    guardar_tablas_csv(oct, nov, dic, ene, feb)
    data, df = integrar_tablas(oct, nov, dic, ene, feb)
    guardar_dataframe(df)
    visualizar_datos(data, df)

# Ejecutar si se llama desde línea de comandos
# if __name__ == "__main__":
#     ejecutar_proceso_extraccion()
