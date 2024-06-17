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

