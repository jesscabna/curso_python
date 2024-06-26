# return devuelve valores que podre hacer uso 
# crear una funcion que retorne el numero 10 ,y muestre por terminal si es par 
#def diez ():
#    return 10
#if diez () %2== 0:
 #   print("es par")
#else :
 #   print("no es par ")

 

# print solo muestra por terminal 


# return cuando queremos  que nuestra  funciion devuelva   o rwetorne un tipo de dadto  o un tipo de dato estructurado 

#  creaer una funcion queme muestre   el producto de dos numeros 

#def producto(a,b):
 #   return a*b

#print(producto(4,4))

# crear una lista que me retorne  una lista de tres numeros
#def numeros():
 #   return[ 1,2,3]
#print(numeros())

# crear una funcion  que por parametro reciba un nombre  y retorne un mensaje de vienbenida con el nombre 
#def mensaje(nombre):
 #   print(f"hola{nombre}bienvenido al salon ")

# crear  una funciobn  que reciba  poe parametro una lista  de dos numeros y me devuekva el numero menor , mostrar por teminal  el valor retornado por la funcion 
#lista=[1,2,3,4,5,6]
    
#def Min(l):
 #   minimo=l[0]
  #  for n in l :
   #     if n < minimo :
    #        minimo=n
    #return minimo

#print(Min(lista))   


# crear un  parametro que rciba como parametro el  nombre y edad de un a persona mi funcion debera  retornar un diccionario  con los datos  luego mostrar por terminal  el valor de retoerno de mi funcion  
#nombre=input("ingrese su name ->")
#edad:int=input("ingrese su edad->")
#def persona(nom,edad):
 #   return {
  #      "nombre":nom,
  #      "edad":edad
 #   }
#print(persona(nombre,edad))

#ejemplo de lambda
#saludo=lambda n,a:f"hola, {n} , {a}"
#print(saludo("ruth","castilloo"))


# crear un programa anonimo que  reciba como parametrro una lista de 5 numeros  y re3torne dos listas  una con numeros pares y otra con num eroas inpares 

#lista =[1,2,3,4,5] 
#pares=lambda l:[n for n in lista if n%2==0]
#inpares=lambda l:[n for n in lista if n%2!=0]
#print(pares(lista))
#print(inpares(lista)) 





# ejemplo  sobre clourse
#def mwnsaje(m):
 #   print(m)
#def pedir_nombre   () :
  #  nombre=input("ingrese tu nombre->")
 #   return nombre
#mensaje(pedir_nombre())


# FUNCION MAP ()

#LISTA=[4,5,7,8,9]
#nueva_lista=list(map (lambda x:x+1,lista))#por defecto retorna una lista 
#print(nueva_lista)

#FUNCION FILTER ()
#TENGO UNA LISTA  de alumnos que todos ellos aprobaron y pasas al tercer semestre ,

#problema en mi lista todos esta en el 2 semestre por lo que tendremos que crear  una solucion que cambie  el campo de semestre de 2 a 3 
lista_alumnos=[
    {
        "nombre":"anthony",
        "edad":36,
        "semestre":2




    },
    {
     "nombre":"abel",
        "edad":36,
        "semestre":2
    },
    {


         "nombre":"abel",
        "edad":80,
        "semestre":2

    },
    {

         "nombre":"aedith",
        "edad":43,
        "semestre":2

    }



]
def objeto(e):
    if "semestre"in e:
        e ["semestre"]=e["semestre"]+1
    e["especialidaad"]="APSTI"    
    return [
        e
    ]    

alumnos_actualizados=list(map(objeto,lista_alumnos))
print(alumnos_actualizados)
#haciendo uso de filter ()
lista_filtrada=list(filter(lambda x:x ["edad"]<50,lista_alumnos))
print(lista_filtrada)

 #FUNCION FILTER ()
 #devolver los numeros pares de una lista 
lista=[1,3,4,6,5,7,8,9,7]
nueva_lista=list(filter(lambda x :x%2==0,lista))
print(nueva_lista)


