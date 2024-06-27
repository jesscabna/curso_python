# CREAR UNA FUNCION QUE RECIBA POR ARGUMENTO N NUMEROS Y RETORNE UN A LISTA  CON LOS NUMEROS PARES 
def num_pares(*args):
    lista_pares=[]
    for n in args:
        if n%2==0:
            lista_pares.append(n)
            return lista_pares
print(num_pares(8,5,4,7,9,25,4,7,12))        
#return [n for in args if n%2==0]





# crear tres funciones para los siguientes .
#calcular numero menor
#calcular num ero mayor 
# calcular todos los numeros
#se le pasara por argumento n numeros
def min (*args):
    menor=args[0]
    for n in args:
        if n<menor:
            return menor
        

def max (*args):
    mayor=args[0]
    for n in args:
        if n > mayor:
            mayor=n
            return mayor 
    
def  sum (*args):
    suma=0
    for n in args :
        suma +=n
        return suma

    
    
    
valores = 4,7,8,2,1,5
print(min(*valores))
print(max(*valores))
print(sum(*valores))


#crear una lista de alumnos con los siguientes campos 
#nombre,apellido,edad,celular,email
#1. actualizar los registros con un campo mas  todos tendran el campo de programa de studio  de enfermeria...
#2. buscar el segundo reguistro  y actualizar su edad a 50 años

lista_alumnos=[
{
         "nombre":"carloncho",
        "apellido":"solis",
        "edad":35,
        "celular":"987589445",
        "email":"luciosoli@gmail.com"
    },
    {
    
          
             "nombre":"catalina",
             "apellido":"atoccsa",
             "edad":19,
            "celula":961973098,
            "Email":"catalinaatoccsa@gemail.com"
         },
         {   
         
             
             "nombre":"kiara",
             "apellido":"galindo",
             "edad":20,
            "celula":961765098,
            "Email":"kiaragalindo@gemail.com" 
        },
        {
        
              
             "nombre":"zara",
             "apellido":"saens",
             "edad":45,
            "celula":961973098,
            "Email":"zaracha@gemail.com" , 
       }
       
]
def objeto(a):
    a["programa_estudios"]="Enfermeria"
    return [
        a
    ]
otra_lista=list(map(objeto, lista_alumnos))
print(otra_lista)



print("**SEGUNDO REGUISTRO**")

def objeto(e):
        e["edad"]=50
        return [e]



lista=list(filter(objeto,lista_alumnos))
print(otra_lista[1])
