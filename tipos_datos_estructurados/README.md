# tipos de datos estructurados (TDA - Tipo de datos abstractos )
```python
#lista - sus valores o elementos se pueden actualizar
lista=["abel",20,5,2,5,False,["texto" ,.2]]
#tupla - sus valores o elemntos no pueden ser modificados o eliminados 
Tupla=("abel",20,5,.2,False,[])
#diccionario u objetos 
#los diccionaarios almacenan los datos con clave :valor 

diccionario={"nombre":"antonio","edad":15,"sexo":"false"}


```
-[!TIP]
-**OBSERVACION:** que los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados.

```python
lista_alumnos=[
,{
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]


    },{
        "nombre":"ruth",
        "edad":13
        "amigos":["flor,rocio"]


    }

    


]
```
## metodos
### 1. convertir texto a lista 
```python
#metodo list separa un texto por comas
texto="hola"
list(texto)
#["h","o","l","a",]
#metodo split  trozea un texto
texto="hola como estan alumnos de tercero"
texto.split(",")


## "".join se encarga de unir textos en una sola lista

texto_largo="hola como estan bienvenidos al salon de clases"
nueva_lista=texto_largo.split(" ")
print (" ".join(nueva_lista ))
```

### 2. agregar elementos al final de una lista
```python
#metodo apped - es el metodo que me permite agrega elementos al final de una lista.
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]


# metodo insert - es el metodo que me permite agregar elementos en cualquier ubicacion de mi  lista
lista-nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"jessu")
```
### 3. eliminar un elemto de una lista
```python
## metodo pop - es el metodo que elimina el ultimo elemnto de una lista es el contrario de append.si esque no le asignas ningun indice automaticamente te elimina el ultimo

lista-nombres=["edith","ruth","luz"]
lista_nombres.pop()

## primera manera - metodo remove - este metodo elimina por el nombre que coincida en un elemento 
lista-nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")
# segunda opcion - metodo pop- al pasarle por parametros un  in dice esten lo eliminara de la lista 
ista-nombres=["edith","ruth","luz"]
lista_nombres.pop(0)

```
### buscar elemento de una lista 
```python
lista-nombres=["edith","ruth","luz"]
lista_nombres.index("ruth")
print(lista_nombres[indice])


