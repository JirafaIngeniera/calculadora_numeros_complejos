# La variable 'user_name' guarda el nombre ingresado por el
# usuario y se usa posteriormente para interactuar con él
user_name = input("» Ingresa tu nombre por favor: ")
print("¡Hola ", user_name, "! Bienvenido a la calculadora de números complejos.", sep = "")
# Se repite infinitamente la petición para volver más funcional la
# aplicación y en caso de error del usuario permitir el reingreso de datos
while (1):
    # La variable 'user_choice' guarda la opción ingresada por el
    # usuario y nos indica la operación a hacer por la calculadora
    user_choice = input("""» ¿Qué deseas hacer?
    • a) Suma de números complejos
    • b) Resta de números complejos
    • c) Multiplicación de números complejos
    • d) División de números complejos
    • x) Cerrar calculadora de números complejos
    Ingresa la letra de tu opción indicada: """)
    # Se recibe respuesta por el usuario y con el condicional 'if' se
    # procesa la solicitud de acuerdo a lo elegido
    if user_choice == "a":
        print("> Has elegido sumar números complejos.")
    elif user_choice == "b":
        print("> Has elegido restar números complejos.")
    elif user_choice == "c":
        print("> Has elegido multiplicar números complejos.")
    elif user_choice == "d":
        print("> Has elegido dividir números complejos.")
    elif user_choice == "x":
        print("Vale, ", user_name, ". ¡Gracias por usar la calculadora de complejos!.", sep = "")
        break
    else:
        print("× Lo siento, ", user_name, ". La opción ingresada no es válida, intenta de nuevo.", sep = "")
        continue
    # La función 'number_entry' permite mostrar el número ingresado
    # por el usuario en pantalla, recibe las partes reales e imaginarias
    # de ambos números a operar
    def number_entry(x, y):
        if x != 0:
                print(x, end = "")
                if y > 0:
                    print("+", y, "i", sep = "")
                elif y < 0:
                    print(y, "i", sep = "")
                else:
                    print(end = "\n")
        else:
                print(y, "i", sep = "")
    # Se usan bucles 'while' para evitar el ingreso de datos
    # inválidos
    # La función 'loop_first_number' recibe las partes real e imaginaria
    # del primer número complejo a operar
    def loop_first_number():
        while 1:
            # Las variables 'a' y 'b' guardan la parte real e imaginaria respectivamente
            # del primer número complejo
            global a, b
            a = int(input("» Ingresa la parte real de tu primer número complejo: "))
            b = int(input("» Ingresa la parte imaginaria de tu primer número complejo: "))
            # Se usan comparadores lógicos para mejorar la interfaz de entrega de datos
            # al usuario
            if a == 0 and b == 0:
                print("× Lo siento, ", user_name, ". El número ingresado no es válido, intenta de nuevo.", sep = "")
                continue
            else:
                print("> Se ha ingresado el número Z₁ = ", end = "")
                number_entry(a, b)
                break
    # La función 'loop_second_number' recibe las partes real e imaginaria
    # del segundo número complejo a operar
    def loop_second_number():
        while 2:
            # Las variables 'c' y 'd' guardan la parte real e imaginaria respectivamente
            # del segundo número complejo
            global c, d
            c = int(input("» Ingresa la parte real de tu segundo número complejo: "))
            d = int(input("» Ingresa la parte imaginaria de tu segundo número complejo: "))
            if c == 0 and d == 0:
                print("× Lo siento, ", user_name, ". El número ingresado no es válido, intenta de nuevo.", sep = "")
                continue
            else:
                print("> Se ha ingresado el número Z₂ = ", end = "")
                number_entry(c, d)
                break
    loop_first_number()
    loop_second_number()
    print("El resultado es: ", end = "")
    def operation_result(w, z):
        if w == 0 and z == 0:
            print(0)
        else:
            if w != 0:
                print(w, end = "")
                if z > 0:
                    if z == 1:
                        print("+", "i", sep = "")
                    else:
                        print("+", z, "i", sep = "")
                if z < 0:
                    if z == -1:
                        print("-", "i", sep = "")
                    else:
                        print(z, "i", sep = "")
            else:
                if z == 1:
                    print("i", sep = "")
                elif z == -1:
                    print("-", "i", sep = "")
                else:
                    print(z, "i", sep = "")
    if user_choice == "a": # Suma de complejos
        operation_result(a + c, b + d) 
    elif user_choice == "b": # Resta de complejos
        operation_result(a - c, b - d)  
    elif user_choice == "c": # Multiplicación de complejos
        operation_result(a * c - b * d, a * d + b * c)
    elif user_choice == "d": # División de complejos
        operation_result(float((a * c + b * d) / (c ** 2 + d ** 2)), float(b * c - a * d) / (c ** 2 + d ** 2))