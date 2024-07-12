# averiguar modulos y paquetes en python

### modulos 

Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

Consideremos, por ejemplo, un archivo aritmetica.py que contenga las siguientes definiciones.
```python

#EJEMPLO 
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

##Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.

import aritmetica

print(aritmetica.sumar(7, 5))


#Una sintaxis alternativa para importar objetos desde un módulo es la siguiente.

from aritmetica import sumar

print(sumar(7, 5))

#Nótese que, en este segundo caso, no se prefija el nombre del módulo al invocar al objeto importado. Podemos importar varios objetos separándolos por comas.

from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))

#O bien, para importar todos los objetos dentro de un módulo:

from aritmetica import *

#Podemos hacer que un módulo esté visible para cualquier archivo ubicándolo en la carpeta Lib dentro del directorio de instalación de Python (p. ej. C:\Python310\Lib).

```

### paquetes 
Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.
```python

matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py

# Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))
# O bien de la siguiente.

from matematica import aritmetica

print(aritmetica.sumar(7, 5))
#  También, esta otra:

from matematica.aritmetica import sumar

print(sumar(7, 5))
```
Python incluye una inmensa cantidad de módulos y paquetes en su instalación (aún más grande es aquella desarrollada por la comunidad, de la que hablaremos más adelante), a los que se conoce como librería estándar. Ahora que sabemos cómo trabajar con ellos, sopesemos esta cuestión...


# diferencias emtre modulos y paquetes


### MODULO
Un módulo puede contener tanto declaraciones ejecutables como definiciones de funciones. Estas declaraciones están pensadas para inicializar el módulo. Se ejecutan únicamente la primera vez que el módulo se encuentra en una declaración import. [1] (También se ejecutan si el archivo se ejecuta como script.)

Cada módulo tiene su propio espacio de nombres privado, que es utilizado como espacio de nombres global por todas las funciones definidas en el módulo. De este modo, el autor de un módulo puede utilizar variables globales en el módulo sin preocuparse por choques accidentales con las variables globales de un usuario. Por otro lado, si sabes lo que estás haciendo puedes tocar las variables globales de un módulo con la misma notación que se utiliza para referirse a sus funciones, modname.itemname.

Los módulos pueden importar otros módulos. Es costumbre pero no obligatorio ubicar todas las declaraciones import al principio del módulo (o script, para el caso). Los nombres de los módulos importados, si se colocan en el nivel superior de un módulo (fuera de cualquier función o clase), se añaden al espacio de nombres global del módulo.


###  PAQUETE 

Los Paquetes son una forma de estructurar el espacio de nombres de módulos de Python usando «nombres de módulo con puntos». Por ejemplo, el nombre del módulo A.B designa un submódulo B en un paquete llamado A. Así como el uso de módulos salva a los autores de diferentes módulos de tener que preocuparse por los nombres de las variables globales de los demás, el uso de nombres de módulo con puntos evita que los autores de paquetes multimódulos, como NumPy o Pillow, tengan que preocuparse por los nombres de los módulos de los demás.

Supongamos que quieres designar una colección de módulos (un «paquete») para el manejo uniforme de archivos y datos de sonidos. Hay diferentes formatos de archivos de sonido (normalmente reconocidos por su extensión, por ejemplo: .wav, .aiff, .au), por lo que tienes que crear y mantener una colección siempre creciente de módulos para la conversión entre los distintos formatos de archivos. Hay muchas operaciones diferentes que quizás quieras ejecutar en los datos de sonido (como mezclarlos, añadir eco, aplicar una función ecualizadora, crear un efecto estéreo artificial), por lo que además estarás escribiendo una lista sin fin de módulos para realizar estas operaciones. Aquí hay una posible estructura para tu paquete (expresados en términos de un sistema jerárquico de archivos):