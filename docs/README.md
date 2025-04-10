
### PROYECTO DE DATA ANALYTICS 'Ecommerce' - ETL - EDA
Este proyecto tiene como objetivo enseñar las bases de un flujo completo de análisis de datos: desde la adquisición de datos (ETL), el análisis exploratorio (EDA), la descripción estadística, hasta la creación de dashboards en Power BI o Tableau.


### FORMULACIÓN DE PREGUNTAS DE INVESTIGACIÓN
## KPIS
* Visitas
* Conversión
* Frecuencia de compra
* Ticket medio
* Tasa abandono carrito
* LTV

## ENTIDADES Y DATOS
* Usuarios
* Clientes
* Sesiones
* Eventos
* Productos

## PREGUNTAS SEMILLA
# Sobre el customer journey
* ¿Cómo es un proceso típico de compra?  
* ¿Cuántos productos se ven, se añaden al carro, se abandonan y se compran de media en cada sesión?  
* ¿Cómo ha sido la tendencia de estos indicadores en los últimos meses?  

# Sobre los clientes
* ¿Cuántos productos compra cada cliente?
* ¿Cuánto se gasta cada cliente?
* ¿Hay "mejores clientes" que haya que identificar y tratar de forma diferente?
* ¿Los clientes repiten compras en los siguientes meses?
* ¿Cual es el LTV medio de un cliente?
* ¿Podemos diseñar campañas personalizas al valor del cliente?

# Sobre los productos
* ¿Cuales son los productos más vendidos?
* ¿Hay productos que no se venden?
* ¿Existe relación entre el precio del producto y su volumen de ventas?
* ¿Hay productos que se visiten pero no se compren?
* ¿Hay productos que se saquen recurrentemente del carrito?
* ¿Se podrían hacer recomendaciones personalizadas de productos para cada cliente?


### OBJETIVOS
- Trabajamos sobre una base de datos .db(SQLite) de un Ecommerce de Rusia del sector cosmetico.
- Crear estructura de directorios y entorno
- Aplicar un proceso de ETL sobre el conjunto de datos 
     - Crear estructura de directorios y entorno
     - Realizar la extracción (carga y preparación de los datos).
     - Realizar la limpieza de datos.
     - Realizar la transformación de los datos
- Realizar un análisis exploratorio de los datos.
- Generar estadísticas descriptivas.
- Crear visualizaciones y dashboards interactivos.
- Organizar el proyecto en un repositorio estructurado.
- Gestionar entornos reproducibles con `environment.yml`.



## 1. CREAR ESTRUCTURA DE DIRECTORIOS Y ENTORNO --> 00_project.ipynb
📦 ecommerce
│── 📁 docs/                        # Documentación del proyecto
│   ├── requirements.txt            # Librerías necesarias (pip)
│   ├── environment.yml             # Dependencias en formato Conda
│   ├── README.md                   # Descripción general del proyecto
│
│── 📁 data/                        # Datos del proyecto
│   ├── 📁 raw/                     # Datos sin procesar (descargados de fuentes externas)
│   ├── 📁 processed/               # Datos limpios y transformados
│   ├── 📁 originals/               # Copias originales de datos clave
│   ├── 📁 validation/              # Conjuntos de datos para validación
│
│── 📁 notebooks/                   # Jupyter Notebooks organizados
│   ├── 00_project.ipynb            # Notebook con estructura de directorios y entorno
│   ├── 01_extraction.ipynb         # Notebook con la extracción, carga de datos y preparación del DataFrame
│   ├── 02_cleaning.ipynb           # Notebook con la limpieza de datos
│   ├── 03_transformation.ipynb     # Notebook con la transformación de datos
│   ├── 04_analysis.ipynb           # Notebook con el análisis exploratorio de datos
│
│── 📁 src/                         # Código fuente en Python
│   ├── __init__.py                 # Permite tratar la carpeta como un módulo
│   ├── 01_extraction.py            # Extracción, carga de datos y preparación del DataFrame
│   ├── 02_cleaning.py              # Limpieza de datos
│   ├── 03_transformation.py        # Transformación de datos
│   ├── 04_analysis.py              # Análisis exploratorio de datos
│   ├── 📁 utils/                   # Funciones auxiliares y reutilizables
│
│── 📁 dashboards/                  # Paneles de visualización
│   ├── 📁 powerbi/                 # Dashboards de Power BI (.pbix)
│   ├── 📁 tableau/                 # Dashboards de Tableau
│
│── 📁 images/                      # Imagenes del proyecto      
│
│── main.py                         # Archivo principal para ejecutar el proyecto
│── .gitignore                      # Archivos a ignorar en Git


# Creación de directorios para el proyecto
''' Crear proyecto y estructura de directorios en la carpeta 'PROYECTOS'
conda update conda -y
conda clean -y --all
PROYECTO="ecommerce"
mkdir -p "$PROYECTO"/docs && touch "$PROYECTO"/docs/README.md
mkdir -p "$PROYECTO"/data/{raw,processed,originals,validation}
mkdir -p "$PROYECTO"/notebooks && touch "$PROYECTO"/notebooks/{00_project.ipynb,01_extraction.ipynb,02_cleaning.ipynb,03_transformation.ipynb,04_analysis.ipynb}
mkdir -p "$PROYECTO"/src/utils && touch "$PROYECTO"/src/{__init__.py,01_extraction.py,02_cleaning.py,03_transformation.py,04_analysis.py}
mkdir -p "$PROYECTO"/dashboards/{powerbi,tableau}
mkdir -p "$PROYECTO"/images
touch "$PROYECTO"/{.gitignore,main.py}

# Creación de entorno para el proyecto
'''Crear un nuevo entorno e instalar los paquetes en Conda // Instalacion del entorno y kernel en la ubicación del entorno
conda update conda
conda clean -y --all
ENTORNO="ecommerce"
conda deactivate 
conda env remove -y -n $ENTORNO
conda create -y -n $ENTORNO numpy pandas matplotlib seaborn statsmodels scikit-learn scipy sqlalchemy jupyter jupyter_client
conda activate $ENTORNO
conda install -y -c conda-forge plotly pyjanitor scikit-plot jupyter_contrib_nbextensions
pip install pipreqs
python -m ipykernel install --sys-prefix --name $ENTORNO --display-name "Python ($ENTORNO)"
jupyter kernelspec list
'''

# Exportar librería y dependencias, archivo environment.yml
- conda env export > environment.yml --> Exportar archivo
- conda env create -f environment.yml --> Instalar todos los paquetes y configurar el entorno con el mismo nombre y dependencias especificadas en el archivo.



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
- Relaion de productos con muchas vistas y pocas compras


## 6. CONCLUSIONES
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


