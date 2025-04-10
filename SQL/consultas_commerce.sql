CREATE DATABASE ecommerce;
USE ecommerce;
SELECT * FROM ecommerce_transformado;


-- Verificar el número total de registros
SELECT 
    COUNT(*) AS total_registros
FROM 
    ecommerce_transformado;
    
/*------------------------------------------------------------------------*/

-- Verificar las primeras 10 filas de la tabla
SELECT 
    * 
FROM 
    ecommerce_transformado
LIMIT 10;

/*------------------------------------------------------------------------*/

-- Verificar las columnas de la tabla y su tipo de datos
DESCRIBE ecommerce_transformado;

/*------------------------------------------------------------------------*/

-- Contar el número de eventos distintos en la tabla
SELECT 
    COUNT(DISTINCT evento) AS total_eventos_distintos
FROM 
    ecommerce_transformado;

/*------------------------------------------------------------------------*/
-- Obtener el número de usuarios únicos
SELECT 
    COUNT(DISTINCT usuario) AS total_usuarios
FROM 
    ecommerce_transformado;

/*------------------------------------------------------------------------*/
-- Verificar los diferentes tipos de eventos registrados
SELECT 
    DISTINCT evento
FROM 
    ecommerce_transformado;

/*------------------------------------------------------------------------*/
-- Contar cuántos registros hay por cada tipo de evento
SELECT 
    evento,
    COUNT(*) AS cantidad_eventos
FROM 
    ecommerce_transformado
GROUP BY 
    evento
ORDER BY 
    cantidad_eventos DESC;

/*------------------------------------------------------------------------*/

-- Verificar el rango de fechas en el dataset (fecha mínima y máxima)
SELECT 
    MIN(date) AS fecha_minima, 
    MAX(date) AS fecha_maxima
FROM 
    ecommerce_transformado;

/*------------------------------------------------------------------------*/
-- Verificar el número de sesiones únicas
SELECT 
    COUNT(DISTINCT sesion) AS total_sesiones
FROM 
    ecommerce_transformado;
    
/*------------------------------------------------------------------------*/
-- Verificar los valores únicos de la columna festivo
SELECT 
    DISTINCT festivo
FROM 
    ecommerce_transformado;

/*------------------------------------------------------------------------*/
-- Contar el número de registros por cada día de la semana
SELECT 
    DAYOFWEEK(date) AS dia_semana,
    COUNT(*) AS cantidad_eventos
FROM 
    ecommerce_transformado
GROUP BY 
    dia_semana
ORDER BY 
    dia_semana ASC;

/*------------------------------------------------------------------------*/
-- Verificar los usuarios que tienen más eventos registrados
SELECT 
    usuario,
    COUNT(*) AS cantidad_eventos
FROM 
    ecommerce_transformado
GROUP BY 
    usuario
ORDER BY 
    cantidad_eventos DESC
LIMIT 10;

/*------------------------------------------------------------------------*/
-- Obtener el precio promedio de los productos comprados
SELECT 
    AVG(precio) AS precio_promedio
FROM 
    ecommerce_transformado
WHERE 
    evento = 'purchase';

/*------------------------------------------------------------------------*/
-- Obtener los productos más visualizados (eventos "view")
SELECT 
    producto,
    COUNT(*) AS cantidad_vistas
FROM 
    ecommerce_transformado
WHERE 
    evento = 'view'
GROUP BY 
    producto
ORDER BY 
    cantidad_vistas DESC
LIMIT 10;

/*------------------------------------------------------------------------*/
-- Verificar cuántos productos fueron eliminados del carrito
SELECT 
    producto,
    COUNT(*) AS cantidad_sacados_carrito
FROM 
    ecommerce_transformado
WHERE 
    evento = 'remove_from_cart'
GROUP BY 
    producto
ORDER BY 
    cantidad_sacados_carrito DESC
LIMIT 10;

/*------------------------------------------------------------------------*/

-- ¿Cuáles son los productos más vendidos?
SELECT 
    producto,
    COUNT(DISTINCT CASE WHEN evento = 'purchase' THEN sesion END) AS cantidad_compras
FROM 
    ecommerce_transformado
WHERE 
    evento = 'purchase'
GROUP BY 
    producto
ORDER BY 
    cantidad_compras DESC
LIMIT 10;
    
 /*------------------------------------------------------------------------*/   
    
-- ¿Cuál es el importe total gastado por cada cliente?    
SELECT 
    usuario,
    SUM(CASE WHEN evento = 'purchase' THEN precio END) AS total_gastado
FROM 
    ecommerce_transformado
GROUP BY 
    usuario
ORDER BY 
    total_gastado DESC;
    
 /*------------------------------------------------------------------------*/  

-- ¿Los clientes repiten compras en los siguientes meses?
SELECT 
    usuario,
    COUNT(DISTINCT YEAR(date) * 12 + MONTH(date)) AS meses_comprando
FROM 
    ecommerce_transformado
WHERE 
    evento = 'purchase'
GROUP BY 
    usuario
HAVING 
    meses_comprando > 1;
    
 /*------------------------------------------------------------------------*/     
    
-- ¿Existen productos que no se venden?
SELECT 
    producto
FROM 
    ecommerce_transformado
GROUP BY 
    producto
HAVING 
    SUM(CASE WHEN evento = 'purchase' THEN 1 ELSE 0 END) = 0;
    
 /*------------------------------------------------------------------------*/ 
    
-- ¿Hay relación entre el precio del producto y su volumen de ventas?    
SELECT 
    producto,
    AVG(precio) AS precio_promedio,
    COUNT(DISTINCT CASE WHEN evento = 'purchase' THEN sesion END) AS cantidad_compras
FROM 
    ecommerce_transformado
WHERE 
    evento = 'purchase'
GROUP BY 
    producto
ORDER BY 
    cantidad_compras DESC;
    
/*------------------------------------------------------------------------*/     
    
-- ¿Hay productos que se saquen recurrentemente del carrito?    
SELECT 
    producto,
    COUNT(DISTINCT CASE WHEN evento = 'remove_from_cart' THEN sesion END) AS veces_sacado
FROM 
    ecommerce_transformado
WHERE 
    evento = 'remove_from_cart'
GROUP BY 
    producto
ORDER BY 
    veces_sacado DESC
LIMIT 10;

/*------------------------------------------------------------------------*/ 

-- ¿Cuántos productos añade un cliente al carrito en promedio?
SELECT 
    usuario,
    COUNT(DISTINCT CASE WHEN evento = 'cart' THEN producto END) AS productos_añadidos_carrito
FROM 
    ecommerce_transformado
GROUP BY 
    usuario
ORDER BY 
    productos_añadidos_carrito DESC;
    
/*------------------------------------------------------------------------*/ 
    
-- ¿Cuántos productos elimina un cliente del carrito en promedio?
SELECT 
    usuario,
    COUNT(DISTINCT CASE WHEN evento = 'remove_from_cart' THEN producto END) AS productos_sacados_carrito
FROM 
    ecommerce_transformado
GROUP BY 
    usuario
ORDER BY 
    productos_sacados_carrito DESC;
    
/*------------------------------------------------------------------------*/     
    
  -- ¿Qué días de la semana tienen más compras? 
   SELECT 
    DAYOFWEEK(date) AS dia_semana,
    COUNT(DISTINCT CASE WHEN evento = 'purchase' THEN sesion END) AS compras
FROM 
    ecommerce_transformado
WHERE 
    evento = 'purchase'
GROUP BY 
    dia_semana;
    
    


    
    


