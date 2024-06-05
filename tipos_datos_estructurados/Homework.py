# crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad .


#insertar al final de la lista los datos de antony. 


#eliminar de la lsita si existe los datos de abel.


#buscar y mostrar el alumno en la poscion  4 de la lista.
#lista_alumnos=[
  #  {
   #     "nombre":"abel",
    #    "apellido":"castillo",
     #   "edad":20,
    #},{
    #    "nombre":"ruth",
     #   "apellido":"morales",
      #  "edad":18,

    #},{
     #   "nombre":"flor",
      #  "apellido":"lucana ",
       # "edad":18,

    #},{
     #   "nombre":"luz",
      #  "apellido":"jimenez",
       # "edad":19,

    #},{
     #   "nombre":"antony",
      #  "apellido":"quispe",
       # "edad":25,
        
    #}
#]

#lista_alumnos.remove({
 #       "nombre":"abel",
  #      "apellido":"castillo",
   #     "edad":20,
        
#})
#indice=lista_alumnos.index({
    
 #       "nombre":"luz",
  #      "apellido":"jimenez",
   #     "edad":19,
    #})
#print(lista_alumnos[indice])


#crear  una lista de 3 diccionarios  donde tendran datos de su mascotas [nombre,edad,sexo,raza]

#tareas
#mostrar la lñsita con los 4 diccionarios
#editar el 3 registro y cambiar la edad sin modificar la lista
#mostrar la lista  original y luego la lista con  el tercer registro modificado

#dato_mascota=[
 #    {"nombre":"OZUNA",
  #   "edad":5,
   #  "sexo":"macho",
     #"raza":"pitbull"
     #},{"nombre":"blanca",
     #"edad":6,
    # "sexo":"hembra",
     #"raza":"poodle"
     #},{"nombre":"negra",
     #"edad":4,
     #"sexo":"hembra",
     #"raza":"chiwawa"
     #},{"nombre":"espritu",
     #"edad":7,
     #"sexo":"hembra",
     #"raza":"shi tzu"
     #}
     #]
#for diccionario in dato_mascota:
#    print(diccionario)
#print()
#copia_mascotas=dato_mascota.copy()
#copia_mascotas[2]["edad"]=7
#for copy in copia_mascotas:
 #   print(copy)
   

# yo como dueño de mi mascota 
# deceo ver una lista de mis mascotas 
#para tener un resumen de mi9s mascotas 


# yo como dueño de mi mascota 
# deceo actualizar la edad de mi mascota 
#para tener una lista  de mi mascota 

#yo como dueño de mis mascota
#necesito acceso a los datos de mi mascota 
# para monitorear amis mascostaS 


# 3 . un empresario de alquiler de autos desea guardar en una base de datos la informacion de sus vehiculos   ,proceso que decea automatizar con un 
# sistema informatico, las acciones que puede realizar el empresario  son ver las listas  de autos que tiene , podra tamabien actualizar la lista y agregar  un nuevo vehiculo 
######


#CASOS DE USO 

# yo como empresario de alquiler de autos .


# deceo  guardar en una base de datos informacion sobre mis  vehiculos .



# para poder visualizar mi lista de  vehiculos , actualizar y agregar .


 # PROGRAMACION M
lista_autos=[
    {
        "MARCA":"NISSAN",
        "PLACA":"WWW-23H",
        "PRECIO":30.000,
        "COLOR":"NEGRO",
    },{
        "MARCA":"TOYOTTA",
        "PLACA":"PYU-U78",
        "PRECIO":50.000,
         "COLOR":"BLANCO",
        

    },{
        "MARCA":"LAMBO",
        "PLACA":"TED-Y56 ",
        "PRECIO":18.000,
         "COLOR":"GRISS",


    },{
        "MARCA":"FERRARI",
        "PLACA":"SAP-O67",
        "PRECIO":19.000,
         "COLOR":"ROJO",

    },{
        "MARCA":"HILUX",
        "PLACA":"QZS-I78",
        "PRECIO":25.000,
         "COLOR":"PLOMO",
        
    }
]



#AGREGAR UN AUTO MAS A LA LISTA
lista_autos.append([{"MARCA" :"CHEBRO" , "PLACA ":" 876-Y67"," PRECIO":"23.000", "COLOR":"MORADO"}])
print(lista_autos)

#actualizar un dato de autos en este caso el carro NISSAN

for diccionario in lista_autos:
    print(diccionario)
    print()
copia_autos=lista_autos.copy()
copia_autos[0]["PRECIO"]=100.000 
for copy in lista_autos:
    
    print(copy)




# crear una lista de los primeros 20 numeros primos haciendo uso de conprecion

numeros_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if num != i)]
primeros_20_primos = [num for num in numeros_primos][:20]
print(primeros_20_primos)




    





























