def f_cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales que aparece en un texto """
    text_minuscula:str=text.lower()
    cantidad_vocales=0
    for n in text_minuscula:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales      