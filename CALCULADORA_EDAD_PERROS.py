while True:
    edadhumana = int(input("¿Cuántos años tienes?"))

    if edadhumana <= 2: 
        edadperro = edadhumana * 10.5

    else:
        edadperro = 2 * 10.5 + (edadhumana - 2)*4

    print("Tu edad de perro es aproximadamente de", edadperro, "años.")
    salir = input("Deseas salir?(si/no)")
    if salir == "si":
        print("¡Hasta luego!")
        break
