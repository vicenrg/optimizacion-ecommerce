
### PROYECTO DE DATA ANALYTICS 'Ecommerce' - ETL - EDA
Este proyecto de Data Science tiene como objetivo analizar el rendimiento de un eCommerce mediante técnicas de análisis exploratorio, visualización de datos y modelado, con el fin de extraer insights relevantes para la toma de decisiones empresariales.

### TECNOLOGÍAS UTILIZADAS
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Power BI
- Jupyter Notebooks
- VS Code
- Conda
- MySQL Workbench
- GitHub

### OBJETIVO
Analizar los datos transaccionales para realizar acciones que incrementen visitas, conversiones y ticket medio, y por tanto incrementar la facturación global del ecommerce.

Para conseguir estos objetivos trabajamos sobre las siguientes palancas operativas:
* Customer journey: cómo podemos optimizar cada uno de los pasos del proceso
* Clientes: cómo podemos usar la info disponible de los clientes para optimizar las campañas que realicemos
* Productos: cómo podemos optimizar el catálogo de productos e identificar de manera personalizada qué productos tenemos que poner delante de cada cliente

### FORMULACIÓN DE PREGUNTAS DE INVESTIGACIÓN
## KPIS
* Visitas
* Conversión
* Frecuencia de compra
* Ticket medio
* Tasa abandono carrito

## ENTIDADES Y DATOS
* Usuarios
* Clientes
* Sesiones
* Eventos
* Productos

## PREGUNTAS A RESPONDER
# Sobre el customer journey
* ¿Cómo es un proceso típico de compra?  
* ¿Cuántos productos se ven, se añaden al carro, se abandonan y se compran de media en cada sesión?  
* ¿Cómo ha sido la tendencia de estos indicadores en los últimos meses?  

# Sobre los clientes
* ¿Cuántos productos compra cada cliente?
* ¿Cuánto se gasta cada cliente?
* ¿Hay "mejores clientes" que haya que identificar y tratar de forma diferente?
* ¿Los clientes repiten compras en los siguientes meses?
* ¿Podemos diseñar campañas personalizas al valor del cliente?

# Sobre los productos
* ¿Cuales son los productos más vendidos?
* ¿Hay productos que no se venden?
* ¿Existe relación entre el precio del producto y su volumen de ventas?
* ¿Hay productos que se visiten pero no se compren?
* ¿Hay productos que se saquen recurrentemente del carrito?
* ¿Se podrían hacer recomendaciones personalizadas de productos para cada cliente?

### TRABAJOS A REALIZAR
- Trabajamos sobre una base de datos .db(SQLite) de un Ecommerce de Rusia del sector cosmetico.
- Creacion de repositorio en GitHub.
- Crear estructura de directorios y entorno.
- Aplicar un proceso de ETL sobre el conjunto de datos.
     - Crear estructura de directorios y entorno.
     - Realizar la extracción (carga y preparación de los datos).
     - Realizar la limpieza de datos.
     - Realizar la transformación de los datos
- Realizar un análisis exploratorio de los datos.
- Generar estadísticas descriptivas.
- Crear visualizaciones y dashboards interactivos.
- Organizar el proyecto en un repositorio estructurado.
- Gestionar entornos reproducibles con `environment.yml`.

## 1. CREAR ESTRUCTURA DE DIRECTORIOS Y ENTORNO --> 00_project.ipynb
- Creación de directorios para el proyecto
- Creación de entorno para el proyecto
- Exportar librería y dependencias, archivo environment.yml

## 2. EXTRACCIÓN CARGA Y PREPARACIÓN DE LOS DATOS --> 01_extraction.ipynb
- Importación de librerías
- Importación de datos
     * Conexión a la base de datos
     * Visualización de las tablas de la base de datos
     * Importación de las tablas de la base de datos
     * Guardar las tablas en .csv
     * Integración de las tablas con apilación vertical
     * Guardar DataFrame original como datos_integrados.csv
     * Hacer una copia del DataFrame original y guardarla como ecommerce.csv
- Visualización de los datos

## 3. LIMPIEZA DE DATOS --> 02_cleaning.ipynb
- Importación de librerías
- Entendiendo el significado de las variables
- Importación de datos
- Análisis del DataFrame
- Formateo y corrección de variables
- Convertir tipos de datos
- Análisis de nulos
- Análisis variables cuantitativas

## 4. TRANSFORMACIÓN DE DATOS --> 03_transformation.ipynb
- Importación de librerías
- Creación de nuevas variables
- Reordenar las variables
- Guardar datos en .pkl y .csv

## 5. ANÁLISIS DE DATOS --> 04_analisis.ipynb
- Importación de librerías
- Analizar la variable eventos
- Facturación media por mes
- Media de cada evento por sesión
- Visualizaciones de eventos por hora
- Porcentaje de compras sobre visistas por hora
- Analisis semanal de los eventos
- Analisis diario de los eventos
- Analisis por dia y hora de las compras
- Como se distribuyen los clientes con respecto al gasto total
- Como se distribuyen los clientes con relación a la frecuencia de compra
- Cuantos productos de media compra un cliente en cada compra
- Cuales son los clientes que mas han comprado
- Cual es la supervivivencia de los clientes
- Cuales son los productos mas vendidos
- Relacion entre el precio y el volumen de ventas
- Productos que se eliminan del carrito
- Cuales son los productos mas vistos
- Relacion de productos con muchas vistas y pocas compras

## 6. CONCLUSIONES
# Información obtenida:
En cada sesión, de media:

* KPIs por sesión: Se ven 2.2 productos
* KPIs por sesión: Se añaden 1.3 productos al carrito
* KPIs por sesión: Se eliminan 0.9 productos del carrito
* KPIs por sesión: Se compran 0.3 productos
* Recurrencia: el 10% de los clientes vuelve a comprar tras el primer mes
* Conversión: 60% de añadir al carrito sobre visualizaciones
* Conversión: 22% de compra sobre añadidos a carrito
* Conversión: 13% de compra sobre visualizaciones
* Facturación media mensual: 125.000€

# Acciones a realizar:
* Revisar las campañas de publicidad y retargeting para concentrar la inversión en franjas entre las 9 y las 13 y entre las 18 y las 20
* Concentrar la inversión del período navideño y post-navideño en la semana del black friday
* Preconfigurar la home con los productos identificados en los análisis como más vistos y más comprados.
* Trabajar sobre los productos con alta tasa de abandono de carrito.
* Trabajar sobre los productos muy vistos pero poco comprados.
* La compra mediana incluye 5 productos, incrementar este ratio mediante la recomendación.
* El 90% de los clientes sólo hace una compra.
* Crear una newsletter periódica para incrementar la frecuencia de visita.
* Campañas promocionales sobre los eventos y las fechas que mas ventas se realizan.
* Crear un programa de fidelización para conseguir que los clientes vuelvan a comprar.

## 7. SQL
- Carga de datos transformados desde 03_transformation.ipynb creando una conexión a SQL
- Querys o consultas sobre las 'PREGUNTAS A RESPONDER'
- Se guarda Script SQL en la carpeta correspondiente del proyecto con el nombre consultas_ecommerce.sql

## 8. DASHBOARDING
- Se crea un dashboard en Power Bi donde se muestran los insights obtenidos a traves de los KPIs más importantes
- Se guarda el dashboard en la estrucutra de directorios con el nombre ecommerce.pbix

![Dashboard1](https://github.com/vicenrg/optimizacion-ecommerce/blob/c17b0cde54fa29e53933faed63687e3af71d2b5c/images/Dashboard%201.png)

![Dashboard1](https://github.com/vicenrg/optimizacion-ecommerce/blob/9921cefd739c7e7baf540cd6623be359f6a7aa59/images/Dashboard%202.png)

![Dashboard1](https://github.com/vicenrg/optimizacion-ecommerce/blob/9921cefd739c7e7baf540cd6623be359f6a7aa59/images/Dashboard%202.png)

![Dashboard1](https://github.com/vicenrg/optimizacion-ecommerce/blob/9921cefd739c7e7baf540cd6623be359f6a7aa59/images/Dashboard%202.png)









