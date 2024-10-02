#crear una clase alumnos con los atributos que ustedn crea por conveninte
#luego instanceasr a 4 alumnos

class alumno:
    def __init__(self,nombre,apellido,edad,DNI):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.DNI=DNI
        #metodos
    def escribir(self):
        print("estoy escribiendo")
    def tarea(self,nombre_docente):  
        print
        
jess=alumno("jess","cabana",20,70815883) 
serapio=alumno("serapio","ramos",20,705545656)
alex=alumno("alex","ramos",20,705545656)
alder=alumno("alder","ramos",20,705545656)


