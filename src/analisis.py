# 04_analisis.py (modularizado)

# # ANÁLISIS EXPLORATORIO DE LOS DATOS (EDA)

# ---
# ## 1. IMPORTAR PAQUETES
# ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Configuraciones para la visualización
pd.options.display.float_format = '{:.2f}'.format
sns.set_theme(style="whitegrid")

# Cargar el DataFrame desde pickle
def load_data(path):
    """Carga los datos desde un archivo pickle."""
    return pd.read_pickle(path)

# Cargar los datos
df = load_data("../data/processed/ecommerce_transformado.pkl")


# ---
# ## 2. ANALIZAR EL CUSTOMER JOURNEY
# ---

def calculate_event_percentages(df):
    """Calcula los porcentajes de diferentes eventos en el customer journey."""
    eventos = df.evento.value_counts()

    # Calcular los porcentajes
    porcentaje_view = (eventos['view'] / eventos.sum()) * 100
    porcentaje_cart_sobre_view = (eventos['cart'] / eventos['view']) * 100
    porcentaje_remove_sobre_cart = (eventos['remove_from_cart'] / eventos['cart']) * 100
    porcentaje_purchase_sobre_cart = (eventos['purchase'] / eventos['cart']) * 100

    # Crear el DataFrame con los valores
    data = {
        'kpi': ['visualizaciones', 'carrito', 'abandono', 'compra'],
        'valor': [100, porcentaje_cart_sobre_view, porcentaje_remove_sobre_cart, porcentaje_purchase_sobre_cart],
    }
    kpis = pd.DataFrame(data)
    
    return kpis, porcentaje_view, porcentaje_cart_sobre_view, porcentaje_remove_sobre_cart, porcentaje_purchase_sobre_cart

# Calcular los KPIs
kpis, porcentaje_view, porcentaje_cart_sobre_view, porcentaje_remove_sobre_cart, porcentaje_purchase_sobre_cart = calculate_event_percentages(df)

# Mostrar resultados
print(f"Porcentaje de visualizaciones (view) sobre el total de eventos: {porcentaje_view:.2f}%")
print(f"Porcentaje de productos añadidos al carrito (cart) sobre el total de visualizaciones (view): {porcentaje_cart_sobre_view:.2f}%")
print(f"Porcentaje de productos sacados del carrito (remove_from_cart) sobre añadidos al carrito (cart): {porcentaje_remove_sobre_cart:.2f}%")
print(f"Porcentaje de productos comprados (purchase) sobre añadidos al carrito (cart): {porcentaje_purchase_sobre_cart:.2f}%")
print(kpis)

def funnel_analytics(eventos, color_sequence, title, kpis_data):
    """Crea un gráfico tipo funnel para analizar los eventos."""
    fig = go.Figure(go.Funnel(
        y=kpis_data['kpi'],
        x=kpis_data['valor'].round(2),
        marker={'color': color_sequence},
        opacity=0.3,
        textinfo="value+percent initial"
    ))
    fig.update_layout(title=title)
    fig.show()

def funnel_analytics_1(evento):
    """Realiza el análisis del funnel para la relación entre visualizaciones, carritos y compras."""
    eventos = df.evento.value_counts()

    # Calcular los porcentajes
    porcentaje_cart_sobre_view = (eventos['cart'] / eventos['view']) * 100
    porcentaje_purchase_sobre_cart = (eventos['purchase'] / eventos['cart']) * 100
    
    kpis = pd.DataFrame({'kpi':['visualizaciones', 'carrito', 'compra'],
                         'valor':[100, porcentaje_cart_sobre_view, porcentaje_purchase_sobre_cart]})

    funnel_analytics(eventos, ['red', 'blue', 'green'], 
                     "- Porcentaje de productos añadidos al carrito sobre el total de visualizaciones <br>- Porcentaje de productos comprados sobre añadidos al carrito", 
                     kpis)

funnel_analytics_1(df.evento)


def funnel_analytics_2(evento):
    """Realiza el análisis del funnel para la relación entre abandonos y compras en el carrito."""
    eventos = df.evento.value_counts()

    # Calcular los porcentajes
    porcentaje_remove_sobre_cart = (eventos['remove_from_cart'] / eventos['cart']) * 100
    porcentaje_purchase_sobre_cart = (eventos['purchase'] / eventos['cart']) * 100
    
    kpis = pd.DataFrame({'kpi':['carrito', 'abandono', 'compra'],
                         'valor':[100, porcentaje_remove_sobre_cart, porcentaje_purchase_sobre_cart]})

    funnel_analytics(eventos, ['red', 'blue', 'green'], 
                     "- Porcentaje de productos sacados del carrito sobre añadidos al carrito <br>- Porcentaje de productos comprados sobre añadidos al carrito", 
                     kpis)

funnel_analytics_2(df.evento)


# ---
# ## 3. ANÁLISIS DE FACTURACIÓN Y EVENTOS
# ---

def monthly_revenue(df):
    """Calcula la facturación total y media por mes."""
    facturacion_por_mes = df.loc[df.evento == 'purchase'].groupby('mes').precio.sum()
    facturacion_media = facturacion_por_mes.mean()
    
    return facturacion_por_mes, facturacion_media

facturacion_por_mes, facturacion_media = monthly_revenue(df)
print(f"Facturación por mes: \n{facturacion_por_mes}\n")
print(f"Facturación media por mes: {facturacion_media:.2f}\n")

def event_per_session(df):
    """Calcula la media de cada evento por sesión."""
    eventos_por_sesion = df.groupby(['sesion', 'evento'], observed=True).producto.count().unstack().fillna(0)
    media_eventos_sesion = eventos_por_sesion.mean()
    
    orden = ['view', 'cart', 'remove_from_cart', 'purchase']
    media_eventos_sesion = media_eventos_sesion.reindex(orden)
    
    return media_eventos_sesion

media_eventos_sesion = event_per_session(df)
print("Media de eventos por sesión (ordenados):")
print(media_eventos_sesion)
print("\nSe deben incrementar la media de visualizaciones, carritos y compras por sesión y disminuir los abandonos de carrito.")

def events_by_hour(df):
    """Calcula los eventos por hora y genera un gráfico de la distribución."""
    eventos_por_hora = df.groupby(['hora', 'evento'], observed=True).size().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 6))
    for evento in eventos_por_hora.columns:
        plt.plot(eventos_por_hora.index, eventos_por_hora[evento], label=evento)
    
    plt.title("Total de eventos por hora", fontsize=16)
    plt.xlabel("Hora", fontsize=12)
    plt.ylabel("Cantidad de eventos", fontsize=12)
    plt.xticks(range(0, 24))  
    plt.legend(title="Eventos", fontsize=10)
    plt.grid(alpha=0.3)
    
    return eventos_por_hora

eventos_por_hora = events_by_hour(df)
print("Total de eventos por hora:\n", eventos_por_hora)


def purchase_rate_by_hour(df):
    """Calcula y muestra la tasa de compras sobre visitas por hora."""
    eventos_por_hora['compras_visitas'] = eventos_por_hora['purchase'] / eventos_por_hora['view'] * 100
    eventos_por_hora = eventos_por_hora[['view', 'cart', 'remove_from_cart', 'purchase', 'compras_visitas']]

    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        x=eventos_por_hora.index, 
        y=eventos_por_hora['compras_visitas'],  
        marker='o',  
        color='blue',  
        label='Compras sobre visitas (%)'
    )
    plt.title("Porcentaje de Compras sobre Visitas por Hora", fontsize=16)
    plt.xlabel("Hora", fontsize=12)
    plt.ylabel("Porcentaje (%)", fontsize=12)
    plt.xticks(range(0, 24))  
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)

purchase_rate_by_hour(df)
