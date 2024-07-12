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
Python incluye una inmensa cantidad de módulos y paquetes en su instalación (aún más grande es aquella desarrollada por la comunidad, de la que hablaremos más adelante), a los que se conoce como librería estándar. Ahora que sabemos cómo trabajar con ellos, sopesemos esta cuestión.
