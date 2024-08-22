# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    # Manejar la división por cero
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

# Ciclo principal del programa
while True:
    # Mostrar el menú de opciones al usuario
    mostrar_menu()
    
    # Solicitar al usuario que elija una opción
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    # Verificar si el usuario desea salir
    if opcion == '5':
        print("Gracias por usar la calculadora. ¡Adiós!")
        break

    # Verificar que la opción sea válida (1-4)
    if opcion in ['1', '2', '3', '4']:
        # Solicitar al usuario que ingrese los dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Realizar la operación seleccionada
        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"El resultado de {num1} + {num2} es {resultado}")

        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es {resultado}")

        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"El resultado de {num1} * {num2} es {resultado}")

        elif opcion == '4':
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es {resultado}")

    else:
        # Mensaje de error si el usuario ingresa una opción inválida
        print("Opción inválida, por favor intente nuevamente.")