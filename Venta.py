def menu():
    print("\n~~Venta de entradas~~\n")
    print("1.-Calcular descuento y perdida por ticket.")
    print("2.-Salir\n")
while True:
    menu()
    opcion = input("Seleccione su opción: ")
    if opcion == "1":
        edad = int(input("\nIngrese la edad del cliente: "))
        precio_base = 10000
        if edad <5:
            descuento = 0
            print("Los niños menores de 5 años no pueden comprar tickets.\n")
        elif edad >=5 and edad <=14:
            descuento = 35
        elif edad >=15 and edad <=19:
            descuento = 25
        elif edad >=20 and edad <=45:
            descuento = 10
        elif edad >=46 and edad <=65:
            descuento = 25
        else:
            descuento = 35
        descuento_ap = (precio_base * descuento)/100
        precio_descuento = precio_base - descuento_ap
        perdida_ticket = precio_base - precio_descuento
        print(f"\nEl descuento aplicado para este boleto es de {descuento}%.")
        print(f"La pérdida por venta de este ticket es de ${perdida_ticket}.")
    elif opcion == "2":
        print("\nHas salido exitosamente, hasta luego.\n")
        break
    else:
        print("Ingrese una opción válida.\n")
        #este código posee estructura simple
