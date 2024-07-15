def f_es_menor(lista):
    """funcion para saber el  umero menor de una lista"""
    menor=lista[0]
    for n in lista:
        if n <menor:
            menor=n
    return menor