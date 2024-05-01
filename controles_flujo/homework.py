### tarea 1
nombre = input("Ingresa tu nombre->")
sexo = input("Ingresa tu sexo (M para mujer, H para hombre)-> ")

if nombre and sexo:
    if (sexo == 'M' and nombre[0] < 'M') or (sexo == 'H' and nombre[0] > 'N'):
        print("Tu grupo asignado es-> A")
    else:
        print("Tu grupo asignado es -> B")