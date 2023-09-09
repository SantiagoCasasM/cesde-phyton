##JAMES ESTRADA
##SANTIAGO CASAS MESA
## HASTA EXPLICADITO SE LO COLOCO, MÁS FACIL NO SE PUEDE PROFE.

# Definimos el diccionario con las opciones del menú
menu = {
    1: "Buscar en el diccionario",
    2: "Agregar elemento",
    3: "Eliminar elemento",
    4: "Salir"
}

# Diccionario
libreria_Elantiguo = {"libro": "Lobo Estepario",
                      "autor": "Herman Hess"}

# Función para mostrar el menú
def mostrar_menu():
    print("=== Menú Libreria La Antiguedad===")
    for opcion, descripcion in menu.items():
        print(f"{opcion}. {descripcion}")

# Función para buscar en el diccionario
def buscar_en_diccionario():
    clave = input("Introduce la clave a buscar: ")
    if clave in libreria_Elantiguo:
        print(f"Valor encontrado: {libreria_Elantiguo[clave]}")
    else:
        print("La clave no existe en el diccionario.")

# While para mostrar el loop principal
while True:
    mostrar_menu()
    
    # Obtenemos la selección del usuario
    seleccion = input("Seleccione una opción: ")
    
    # Verificamos si la selección es un número válido
    if seleccion.isdigit():
        seleccion = int(seleccion)
        
        # Realizamos acciones según la selección
        if seleccion == 1:
            print("Has seleccionado: Buscar en el diccionario")
            buscar_en_diccionario()
        elif seleccion == 2:
            print("Has seleccionado: Agregar elemento")
            clave = input("Introduce la clave: ")
            valor = input("Introduce el valor: ")
            libreria_Elantiguo[clave] = valor
            print("Elemento agregado al diccionario.")
        elif seleccion == 3:
            print("Has seleccionado: Eliminar elemento")
            clave = input("Introduce la clave a eliminar: ")
            if clave in libreria_Elantiguo:
                del libreria_Elantiguo[clave]
                print("Elemento eliminado del diccionario.")
            else:
                print("La clave no existe en el diccionario.")
        elif seleccion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Selección no válida. Introduce un número válido.")
    else:
        print("Selección no válida. Introduce un número válido.")
