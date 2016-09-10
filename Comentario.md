# Master universitario en periodismo de investigación, datos y visualización
## El periodista como programador
### Caso práctico - Examen extraordinario 9 septiembre 2016 - Modelo B

####Comentario

Para este ejercicio he aplicado dos soluciones:

#####Menú desplegable
Para el menú desplegable he utilizado Jquery. Concretamente, he utilizado una función en la que oculto los submenus y cuando el ratón pasa por encima del menú, mediante Hover, este se despliega. Concretamente, añade clases de CSS a la etiqueta ul para que sea none (desparezca) u aparezca (block).

####Gráfico
Por el tiempo y la duración del ejercicio he creído conveniente usar Google Charts. Concretamente, tal y como se me pide un gráfico de líneas. De haber tenido más tiempo hubiese utilizado D3.

En este caso, he pasado la variable datos de JavaScript por new google.visualization.arrayToDataTable y he añadido las dos columnas necesarias para los datos. El CSV tiene toda la información en dos lineas. Por ello, hay que trans ponerlos y mediante una sentencia for ir añadiendo la información mediante addRows.

