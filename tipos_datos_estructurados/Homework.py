# crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad .


#insertar al final de la lista los datos de antony. 


#eliminar de la lsita si existe los datos de abel.


#buscar y mostrar el alumno en la poscion  4 de la lista.
lista_alumnos=[
    {
        "nombre":"abel",
        "apellido":"castillo",
        "edad":20,
    },{
        "nombre":"ruth",
        "apellido":"morales",
        "edad":18,

    },{
        "nombre":"flor",
        "apellido":"lucana ",
        "edad":18,

    },{
        "nombre":"luz",
        "apellido":"jimenez",
        "edad":19,

    },{
        "nombre":"antony",
        "apellido":"quispe",
        "edad":25,
        
    }
]

lista_alumnos.remove({
        "nombre":"abel",
        "apellido":"castillo",
        "edad":20,
        
})
indice=lista_alumnos.index({
    
        "nombre":"luz",
        "apellido":"jimenez",
        "edad":19,
    })
print(lista_alumnos[indice])


#crear  una lista de 3 diccionarios  donde tendran datos de su mascotas [nombre,edad,sexo,raza]

#tareas
#mostrar la lñsita con los 4 diccionarios
#editar el 3 registro y cambiar la edad sin modificar la lista
#mostrar la lista  original y luego la lista con  el tercer registro modificado

dato_mascota=[
     {"nombre":"OZUNA",
     "edad":5,
     "sexo":"macho",
     "raza":"pitbull"
     },{"nombre":"blanca",
     "edad":6,
     "sexo":"hembra",
     "raza":"poodle"
     },{"nombre":"negra",
     "edad":4,
     "sexo":"hembra",
     "raza":"chiwawa"
     },{"nombre":"espritu",
     "edad":7,
     "sexo":"hembra",
     "raza":"shi tzu"
     }
     ]
for diccionario in dato_mascota:
    print(diccionario)
print()
copia_mascotas=dato_mascota.copy()
copia_mascotas[2]["edad"]=7
for copy in copia_mascotas:
    print(copy)
   

# yo como dueño de mi mascota 
# deceo ver una lista de mis mascotas 
#para tener un resumen de mi9s mascotas 


# yo como dueño de mi mascota 
# deceo actualizar la edad de mi mascota 
#para tener una lista  de mi mascota 

#yo como dueño de mis mascota
#necesito acceso a los datos de mi mascota 
# para monitorear amis mascostaS 

