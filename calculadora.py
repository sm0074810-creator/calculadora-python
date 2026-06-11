# Calculadora básica en Python
# Proyecto inicial para publicar en GitHub

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b

def potencia(a,b):
    return a ** b

def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Dato inválido. Escribe un número, por favor.")

def mostrar_menu():
    print("\n--- CALCULADORA PYTHON ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. potencia")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "6":
            print("Gracias por usar la calculadora. ¡Nos vemos!")
            break

        if opcion in ["1", "2", "3", "4","5"]:
            num1 = pedir_numero("Escribe el primer número: ")
            num2 = pedir_numero("Escribe el segundo número: ")

            if opcion == "1":
                resultado = sumar(num1, num2)
            elif opcion == "2":
                resultado = restar(num1, num2)
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
            elif opcion == "4":
                resultado = dividir(num1, num2)
            elif opcion == "5":
                resultado = potencia(num1, num2)    

            print("Resultado:", resultado)
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
