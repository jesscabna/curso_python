precio=30.00 
fecha="17/04/2024"
while True :
    print("\nHORARIOS   DISPONIBLES ")   
    print("1.  3.OO PM -  4.00 pm")  
    print("2.  6.00 pm -  7.00 pm") 
    print("3.  8.00 pm -  10.00 pm")
    print("4.salir")
    opcion=int(input("QUE HORARIO DECEA ALQUILAR ->?"))
    if opcion ==1:
        print(f"MUY BIEN ALQUILO A HORAS  [3. 00 PM - 4. 00  pm] \nFECHA : {fecha}\nPRECIO A PAGAR : {precio}")

          
    if opcion == 2:
        print(f"MUY BIEN ALQUILO A HORAS [6. 00 pm -  7. 00 PM ]\nFECHA : {fecha}\nPRECIO A PAGAR : {precio}") 
    if opcion == 3 :
        print(f"MUY BIEN ALQUILO A HORAS [8. 00 PM - 10. 00 pm]\nFECHA :{fecha}\nPRECIO A PAGAR ES:{precio}")
        
    if opcion == 4 :
        print("\tMUCHAS GRACIAS POR TU VISITA  VUELVA PRONTO A NUESTRO GRASS SINTETICO ")
        break