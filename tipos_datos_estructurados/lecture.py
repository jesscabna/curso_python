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




