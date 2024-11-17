import random
while True: 
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    number = int(input("¿Cuántos caracteres debe tener tu contraseña? "))

    contrasena = ""

    for i in range(number):
        contrasena += random.choice(caracteres)

    print("Tu contraseña es:", contrasena)

    salir = input("Deseas salir?(si/no)")
    if salir == "si":
        print("¡Hasta luego!")
        break
