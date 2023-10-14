parqueadero = {}
tarifas = {
    'moto': 10,
    'carro': 20,
    'bicicleta': 5
}

# Función para ingresar un vehículo al parqueadero
def ingresar_vehiculo():
    placa = input("Ingrese la placa del vehículo: ")
    tipo = input("Ingrese el tipo de vehículo (moto, carro o bicicleta): ")
    if tipo in tarifas:
        if placa not in parqueadero:
            parqueadero[placa] = tipo
            print(f"Vehículo con placa {placa} ingresado al parqueadero.")
        else:
            print("¡Error! Este vehículo ya está en el parqueadero.")
    else:
        print("¡Error! Tipo de vehículo no válido.")

# Función para sacar un vehículo del parqueadero y calcular el costo
def sacar_vehiculo():
    placa = input("Ingrese la placa del vehículo a sacar: ")
    if placa in parqueadero:
        tipo = parqueadero.pop(placa)
        costo = tarifas[tipo]
        print(f"Vehículo con placa {placa} sacado del parqueadero. Costo: ${costo}")
    else:
        print("¡Error! Este vehículo no está en el parqueadero.")

# Función para mostrar el estado actual del parqueadero
def mostrar_parqueadero():
    print("\nVehículos en el parqueadero:")
    for placa, tipo in parqueadero.items():
        print(f"Placa: {placa}, Tipo: {tipo}")

# Menú principal
while True:
    print("\n*************************************************")
    print("\nBIENVENIDO AL SISTEMA PARQUEADEROS EL RAYON FIJO")
    print("\n*************************************************")
    print("1. INGRESAR VEHICULO")
    print("2. SACAR VEHICULO")
    print("3. VER VEHICULOS EN EL PARQUEADERO")
    print("2. SALIR DEL SISTEMA")
    print("\n*************************************************")
    opcion = input("SELECCIONE UNA OPCION (SOLO SE ADMITEN NUMEROS): ")

    if opcion == "1":
        ingresar_vehiculo()
    elif opcion == "2":
        sacar_vehiculo()
    elif opcion == "3":
        mostrar_parqueadero()
    elif opcion == "4":
        print("Gracias por usar el sistema de parqueadero. ¡Hasta luego!")
        break
    else:
        print("¡Opción no válida! Por favor, seleccione una opción válida.")
