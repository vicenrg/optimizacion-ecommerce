from src.cleaning import analisis_columnas, analisis_valores, formateo_variables
import pandas as pd

# Ruta del archivo original
ruta_entrada = "data/originals/ecommerce.csv"
ruta_salida = "data/processed/ecommerce_limpio.pkl"

# Cargar datos
df = pd.read_csv(ruta_entrada)

# Análisis del DataFrame
df_analisis_columnas = analisis_columnas(df)
df_analisis_valores = analisis_valores(df)

# Formateo y corrección de variables
df_formateo_variables = formateo_variables(df)
print(df_formateo_variables)

