#primer ejemplo if estructurado
edad=int(input("ingrese ead"))
if edad >=18 :
    print("eres mayor de edad")
else :
    print ("eres menor de edad")


#seggundo ejemplo de if almacenado en una variable

edad_dos:int=int(input("ingrese edad"))
respuesta:str="eres mayor de edad" if edad_dos>=18 else "eres menor"  
print(respuesta)
#crear un programa que imprim a las 5 vocales

vocales="aeiou"
for n in range (0,5):
      print(vocales[n])

#crear un programa que muestre los 8 primeros numeros pares 

contador=0
for n in range (1,17):
    if n%2==0: 
      contador=1
      print (n)
##crear un programa quen pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales a  que tiene esa oracion
##OJO= SOLO LA A MINUSCULA
#oracion:str=input("porfavor eccribe una oracion")
#contador:int=0
#for n in range(0,len(oracion)):
 #   if oracion [n] =="a":
     # contador =contador+1
    #  print(f"la cantidad de letras a es es {contador}")  

## crear un programa que me cuente la cantidad de comas y me muestre  sus indices 
usuario=input("ingrese una oraciopn")
contador:int=0
for n in range(0,len(usuario)):
    if usuario [n] ==",":
        contador=contador+1
        print(f"la cantidad de comas que tengo es {contador}")


