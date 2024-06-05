texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]

texto_largo="hola como estan bienvenidos al salon de clases"
nueva_lista=texto_largo.split(" ")
print (" ".join(nueva_lista ))



###index para buscar un elemento en una lista
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

# crear un programa que recibe una lista desordenada y muestre por terminal la lista ordenada y la lsita previa a ser ordenada
lista=[4,76,1,3,6,8,2]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)


# crar una lista de numeros enteros del siguiente texto 
texto="1,4,8,9,6"
convertir=texto.split(",")
print(convertir)




# otra manera  de realizar 
texto="1,4,8,9,6"
nueva_lista =[]
for n in texto.split(","):
    nueva_lista.append(int(n))
    print(nueva_lista)

# aplicando la tecnica vlc - valor bucle y condicion      
texto="1,4,8,9,6"
nueva_lista =[int (n) for n in texto.split(",") if int(n)
              %2==0]
print(nueva_lista)


#diccionario por comptrencion 
lista_amigos=["abel","anthoni","edith","ruth"]
diccionario={}
for _,v in  enumerate(lista_amigos):
 diccionario[v]=len(v)
 print(diccionario)
 
 
 #aplicando el vlc
 lista_amigos=["abel","anthoni","edith","ruth"]
 diccionario={amigo:len(amigo) for amigo in lista_amigos}
 print(diccionario)

