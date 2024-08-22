Lenguaje de Bicicletas: Sintaxis y Léxico
Introducción
El lenguaje de bicicletas está diseñado para interactuar con un inventario de bicicletas, permitiendo agregar, consultar, y realizar cálculos sobre el desgaste y mantenimiento de las bicicletas. La estructura del lenguaje sigue una sintaxis simple y clara, utilizando un conjunto definido de palabras clave y operadores.

Léxico
El léxico del lenguaje está compuesto por varios tipos de tokens que representan palabras clave, operadores y otros elementos sintácticos. A continuación se detallan los principales tokens utilizados:

Palabras clave:

color: Define el color de una bicicleta.
type: Define el tipo de bicicleta.
wear: Define el desgaste inicial de la bicicleta en porcentaje.
print: Imprime la información de una bicicleta especificada.
distance: Calcula el desgaste adicional basado en la distancia recorrida.
maintenance: Calcula la distancia restante antes del próximo mantenimiento.
owner: Asigna un propietario a una bicicleta.
inventory: Verifica si una bicicleta está en el inventario.
Operadores:

=: Asignación de valores a variables (como bicicletas).
:: Separa las claves de los valores en la definición de una bicicleta.
,: Separa múltiples parámetros dentro de una declaración.
;: Finaliza una sentencia.
{ y }: Delimitan los parámetros de una declaración.
Identificadores (ID): Representan nombres de variables, en este caso, nombres de bicicletas o propietarios.

Números (NUMBER): Representan valores numéricos, como el desgaste (wear) o las distancias recorridas.

Cadenas de texto (STRING): Representan valores textuales como el nombre del propietario o el tipo de bicicleta.

Comentarios (COMMENT): Se identifican con // y permiten añadir anotaciones en el código que no son ejecutadas.

Sintaxis
La sintaxis del lenguaje es estructurada y se compone de sentencias que siguen un patrón definido. Aquí se describen algunas de las operaciones clave:

Asignación de una bicicleta al inventario:

css
Copiar código
<nombre_bicicleta> = color:"<color>", type:"<tipo>", wear:<desgaste>;
Ejemplo:

css
Copiar código
bici1 = color:"rojo", type:"montaña", wear:10;
Este ejemplo agrega una bicicleta roja de montaña con un desgaste inicial del 10% al inventario.

Imprimir información de una bicicleta:

arduino
Copiar código
print {<nombre_bicicleta>};
Ejemplo:

arduino
Copiar código
print {bici1};
Esto imprime la información detallada de bici1, incluyendo el color, tipo, desgaste y propietario (si lo tiene).

Calcular el desgaste después de una distancia:

php
Copiar código
distance {<nombre_bicicleta>, <distancia>};
Ejemplo:

Copiar código
distance {bici1, 50};
Esto calcula y muestra el desgaste de bici1 después de recorrer 50 km adicionales.

Calcular la distancia restante para el próximo mantenimiento:

php
Copiar código
maintenance {<nombre_bicicleta>, <distancia>};
Ejemplo:

Copiar código
maintenance {bici1, 300};
Esto calcula la distancia restante que bici1 puede recorrer antes de necesitar mantenimiento, tomando en cuenta una distancia recorrida de 300 km.

Asignar un propietario a una bicicleta:

php
Copiar código
owner {<nombre_bicicleta>, "<nombre_propietario>"};
Ejemplo:

arduino
Copiar código
owner {bici1, "Juan"};
Esto asigna a "Juan" como propietario de bici1.

Verificar si una bicicleta está en el inventario:

php
Copiar código
inventory {<nombre_bicicleta>};
Ejemplo:

Copiar código
inventory {bici1};
Esto verifica si bici1 está presente en el inventario y muestra la información de la misma si está disponible.
