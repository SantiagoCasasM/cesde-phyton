contadorerr = 0
for i in range (1,4):
    password = int(input("Por favor escriba la clave correcta: "))
    if password == 123:
        print("Bienvenido mi capo")
    else:
        print("Clave incorrecta")
        contadorerr = contadorerr + 1
        print(f"Llevas de intentos: {contadorerr}")

if contadorerr == 3:
    print("Lo intentaste 3 veces, Bloqueado 24h")