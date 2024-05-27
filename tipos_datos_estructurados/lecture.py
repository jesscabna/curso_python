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
