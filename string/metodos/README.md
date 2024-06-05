  ## METODOS EN PYTHON
 # Numero
```python
len(154788)
# devuelve una camtidad de digitos 
# 6

```
## texto 
```python
len("hola mundo")

# devuelve la camtidad de caracteres 
# el espacio cuemta tambien co0mo un caracter 
# 10
```
## listas 
```python
len["h","o"," ","a"]
 # devuelve la cantidad de elementos
 #el espacio cuenta atmbiern como un caracter
 # 4
  ```

 

# numeros 
```python 
len (154788 )
#devuelve la cantidad de digitos 
#6 
```

# texto 
```python 
len ("hola mundo ")
#devuelve la cantidad de caracteres 
# el espacio cuenta también como un carácter 
# 10
```
# listas 

```python 
len (  ["h","o"," ","a"] )
# devuelve la cantidad dd elementos 
# el espacio cuenta también como un carácter 
#4
```

## TUPLAS


# El método count().
```python 
#cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.

l = [1, 1, 1, 3, 5]
print(l.count(1)) #3
```
# El método index() .
```python 
#busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.

l = [7, 7, 7, 3, 5]
print(l.index(5)) #4

#En el caso de no encontrarse, se devuelve un ValueError.

l = [7, 7, 7, 3, 5]
#print(l.index(35)) #Error! ValueError

```
# El método index().
 ```python 
 #también acepta un segundo parámetro opcional, que indica a partir de que índice empezar a buscar el objeto.

l = [7, 7, 7, 3, 5]
print(l.index(7, 2)) #2
```

## DICCIONARIO 

# El método clear().
```python 
 #elimina todo el contenido del diccionario.

d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}
```
# El método get() .
```python 
#nos permite consultar el value para un key determinado. 

d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

```
# El método items() .
```python 
#devuelve una lista con los keys y values del diccionario. 
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a
```
# El método keys().
```python 
# devuelve una lista con todas las keys del diccionario.

d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']
```
# El método values() .
```python
# devuelve una lista con todos los values o valores del diccionario.

d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

```
El método pop().
```python 
# busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. 
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}

```


#NUMÉRICO 

#  int(x).

```python 

#convierte la variable x en número entero

x = 4.56
int(x)

 
```

# float (x).


```python 


#float(x): convierte la variable x en número real

x = 3 
float(x)

```

## LISTAS 

# metodo  append().

```python

lista = [1,2,3,4,5]
lista.append(6)
lista

[1, 2, 3, 4, 5, 6]


```

# metodo clear()
```python 

#Vacía todos los ítems de una lista:

lista.clear()
lista

[]

```

# El método sort() 
```python 
#ordena los elementos de menos a mayor por defecto.

l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]

```

#  El método remove()
```python 

# recibe como argumento un objeto y lo borra de la lista.

l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]

``
 
 


