#ejercicio 1 :
## escribir un programa que que pregunte al usuario  su edad y muestre por pantalla si es mayor o menor

edad=int(input("ingrese edad pliss: "))
if  edad < 18 :
    print("eres menor de edad ")
if edad > 18 :
    print("eres mayor de edad ")   


## Ejercicio 2 :
## escribir un programa que almacene la cadena de caracteres contraseña en una variable , y pregunte al usuaRIO  por contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas .

contra:str=(input("ingrese contraseña pliss :"))
contraseña ="jessJESSjessJESS"
if  contraseña == contra :
    print("contraseña coincide ")
else :
    print("contraseña no coincide ")    

## ejercicio 3 :
## escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas

numero=int(input("ingrese numero pliss:"))
for i in range(numero,-1,-1):
    print(i , end=",")

    