# Proyecto1Estructura

## Participantes:

- Dante Faña Badia - 2015-6079
- Lorna Flerida Espinosa Cuello - 2014-5845


## Como correrlo:

- Insertar <nombre_folder>/<nombre_tarea>. 
    Ex. db/tarea0

## Mejoras intermedias

1. Si los archivos son iguales, no se ejecutan las demás comparaciones y se asume que tiene un score de plagio de 
   100%, esto hace que para algunos casos el tiempo cambie de algoritmo de O(N^2 * M * P) a O(N^2).
2. Eliminación de los cálculos duplicados: eliminando el tiempo constante de T(n), obtendremos el mismo resultado pero 
   sacrificamos algunas informaciones del reporte. El impacto es que ejecutamos 3 veces O(M * P) disminuyendo el string 
   e igualando las funciones y variables solo lo tendremos que ejecutar una vez y tendremos el score de plagio más real 
   con solo un O(M * P).
3. Solamente limpiar y equalizar funciones y variables una vez, asi se reduce el tiempo de ejecución de T(n).
4. Usando memoizacion sacrificamos espacio pero ahorramos en tiempo de lectura del archivo, asi que solo leímos 
   una vez un unico archivo.
5. Usando memoizacion sacrificamos espacio pero ahorramos en tiempo de cálculo de similaridad, asi que solo calculamos 
   una vez y no calculamos A con B y B con A, solo A con B y luego usamos el mismo calculo.
   
