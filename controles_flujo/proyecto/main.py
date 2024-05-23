fecha="23/05/2024"
precio=30.00
grass:list=[]
reserva=f"""
\tGRASS SINTETICO
HORARIOS DISPONIBLES:
1.  4.30 p.m a 5.00 p.m
2.  5.00p.m a 6.00 p.m
3.  7.00 p.m a 8.00 p.m
4.  9.00 p.m a 10.00 p.m
5.  12.00 a.m a 2.00 a.m
6.  3.00 a.m a 6.00 a.m
 """

while True:
    print(reserva)
    opcion=input("Ingrese la opcion del horario que desea reservar: ")
    if opcion == "1":
        print("SU RESERVA FUE EXITOSA ")
    elif opcion == "2":
        print("SU RESERVA FUE EXITOSA")
    elif opcion == "3":
        print("SU RESERVA FUE EXITOSA")
    elif opcion == "4":
        print("SU RESERVA FUE EXITOSA")
    elif opcion == "5":
        print("SU RESERVA FUE EXITOSA")
    elif opcion == "6":
        print("\tSU RESERVA FUE EXITOSA")
    break

reserva=input("DECEA CONSULTAR RESERVA  ?->")
if reserva == "no":
      print(f"{opcion}")
      


print("CONSULTA DE RESERVA:")
if opcion == "1":
        print(f" HORA: [4 .30 p.m a 5.00 p.m ]\nPRECIO:{precio}\nFECHA:{fecha} ")
if opcion == "2":
        print(f"HORA: [5.00 p.m a 6.00 p.m ]\nPRECIO:{precio}\nFECHA:{fecha}  ")
if opcion == "3":
        print(f"HORA: [7.00 p.m a 8.00 p.m ]\nPRECIO:{precio}\nFECHA:{fecha}")
if opcion == "4":
        print(f"HORA: [9.00 p.m a 10.00 p.m ]\nPRECIO:{precio}\nFECHA:{fecha}")
if opcion == "5":
        print(f"HORA: [12.00 a.m a 2.00 a.m ]\nPRECIO:{precio}\nFECHA:{fecha}")
if opcion == "6":
        print(f"HORA: [3.00 a.m a 6.00 a.m ]\nPRECIO:{precio}\nFECHA:{fecha}")
    