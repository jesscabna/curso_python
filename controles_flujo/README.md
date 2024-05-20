#controles de flujo 
**Todos los programas trabajan atravez de instruciones ordenadas.**

**existen maneras de ronper con el flujo normalde los programas creando.**
**repeticiones** de instrucciones

##decisiones 
### la sentencia if 
la sentencia de decision de python es "if" en su escritura debemos añadir una .
**exprecion de comparacion **
terminando con ":" al final de la linea 
`else - elif `
>ejemplo :

```python


if True :
print("es verdad")
```

##ejemplo 2
ejemplo de if estructurado
```python
edad=int(input("ingrese ead"))
 if edad >=18 :
    print("eres mayor de edad")
 else :
    print ("eres menor de edad)   


 ```
## ejemplo 3
if en una variable 
```python
edad_dos:int=int(input("ingrese edad"))
respuesta="eres mayor de edad" if edad_dos>=18 else "eres menor" 
```


 ##ciclos

  son los controles de flujo que repiten codigo y sintaxis es la siguiente 

 > para FOR 
 ```python
 for n in range(1,11)
    print(n)
```
##el enumerate consume mas memoria ... sirve para oraciones largas ( ejecuta mas rapido) y (demora en oraciones pequeñas es mas lento).

### while
es un mecanismo que usa `python` para repetir instrucciones ,de esta sentencia es : `mientras se cumpla la condicion has algo `

```python
condicion =True
while condicion :
   eval=input("desea continuar[S/N]:")
   if eval == "S":
      print("CONTINUAS EN EL BUCLE ")
      continue
   else : 
      print("se termino el programa ")
      condicion=False
      break
```   
while termina con la intervencion de terceros mientras que for tiene un rango como tambien se usa para recorrer listaas.
< la funcion `upper` siempre convierte la minuscula en  mayuscula
< la funcion `lower` en minuscula.


