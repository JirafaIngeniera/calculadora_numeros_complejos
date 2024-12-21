# La variable 'user_name' guarda el nombre ingresado por el
# usuario y se usa posteriormente para interactuar con él
print("○ CALCULADORA DE NÚMEROS COMPLEJOS v2.0 ○", "═════════════════════════════════════════", sep = "\n")
user_name = input("» Ingresa tu nombre por favor: ")
print("\n¡Hola ", user_name, "! Bienvenido a la calculadora de números complejos.", sep = "")
# Se repite infinitamente la petición para volver más funcional la
# aplicación y en caso de error del usuario permitir el reingreso de datos
while 1: # Menú principal
    # La variable 'user_choice_main_menu' guarda la opción ingresada por el usuario
    # en el menú principal y nos indica la operación a hacer por la calculadora
    user_choice_main_menu = input("""» ¿Qué deseas hacer?
    • a) Manejo de números en forma binómica
    • b) Manejo de números en forma polar
    • c) Manejo de números en forma exponencial
    • C) Abrir conversor de números complejos
    • x) Cerrar calculadora de números complejos
    Ingresa la letra de tu opción indicada: """)
    # Se recibe respuesta por el usuario y con el condicional 'if' se
    # procesa la solicitud de acuerdo a lo elegido
    if user_choice_main_menu == "a":
        print("> Has elegido manejar números en forma binómica.")
        while 2: # Manejo de complejos en forma binómica
            user_choice = input("""» ¿Qué deseas hacer?
            • a) Suma de números complejos
            • b) Resta de números complejos
            • c) Multiplicación de números complejos
            • d) División de números complejos
            • C) Abrir convertidor de números complejos
            • x) Volver al menú principal
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
                break
            else:
                print("× Lo siento, ", user_name, ". La opción ingresada no es válida, intenta de nuevo.", sep = "")
                continue
            # La función 'rectangular_form_number_entry' permite mostrar el número ingresado
            # por el usuario en pantalla, recibe las partes reales e imaginarias
            # de ambos números a operar
            def rectangular_form_number_entry(x, y):
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
            # La función 'loop_first_rectangular_number' recibe las partes real e imaginaria
            # del primer número complejo a operar
            def loop_first_rectangular_number():
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
                        rectangular_form_number_entry(a, b)
                        break
            # La función 'loop_second_rectangular_number' recibe las partes real e imaginaria
            # del segundo número complejo a operar
            def loop_second_rectangular_number():
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
                        rectangular_form_number_entry(c, d)
                        break
            loop_first_rectangular_number()
            loop_second_rectangular_number()
            print("=== El resultado es: ", end = "")
            def rectangular_operation_result(w, z):
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
            if user_choice == "a": # Suma de complejos en forma trigonométrica
                rectangular_operation_result(a + c, b + d) 
            elif user_choice == "b": # Resta de complejos en forma trigonométrica
                rectangular_operation_result(a - c, b - d)  
            elif user_choice == "c": # Multiplicación de complejos en forma trigonométrica
                rectangular_operation_result(a * c - b * d, a * d + b * c)
            elif user_choice == "d": # División de complejos en forma trigonométrica
                rectangular_operation_result(float((a * c + b * d) / (c ** 2 + d ** 2)), float(b * c - a * d) / (c ** 2 + d ** 2))
    elif user_choice_main_menu == "b": # Manejo de complejos en forma polar
        print("> Has elegido manejar números en forma polar.")
        while 3:
            user_choice = input("""» ¿Qué deseas hacer?
            • a) Multiplicación de números complejos
            • b) División de números complejos
            • c) Potenciación de números complejos
            • d) Radicalización de números complejos
            • C) Abrir convertidor de números complejos
            • x) Volver al menú principal
            Ingresa la letra de tu opción indicada: """)
            # Se recibe respuesta por el usuario y con el condicional 'if' se
            # procesa la solicitud de acuerdo a lo elegido
            if user_choice == "a":
                print("> Has elegido multiplicar números complejos.")
            elif user_choice == "b":
                print("> Has elegido dividir números complejos.")
            elif user_choice == "c":
                print("> Has elegido potencializar números complejos.")
            elif user_choice == "d":
                print("> Has elegido radicalizar números complejos.")
            elif user_choice == "x":
                print("< Regresando al menú principal...")
                break
            else:
                print("× Lo siento, ", user_name, ". La opción ingresada no es válida, intenta de nuevo.", sep = "")
                continue
            # La variable polar_form_number_entry recibe el módulo y el argumento
            # de un número, lo procesa para que sea lógico y lo imprime al usuario
            def polar_form_number_entry(x, y):
                if x < 0: # Módulos negativos
                    x *= -1
                    y += 180
                while y > 359: # Ángulos coterminales
                    y -= 360
                while y < 0: # Ángulos negativos
                    y += 360
                if user_choice == "a" or user_choice == "b":
                    print(x, " Cis ", y, "°", sep = "")
                elif user_choice == "c" or user_choice == "d":
                    print(x, " Cis ", y, "°", sep = "", end = "")
            # La función 'loop_first_polar_number' recibe el módulo y el
            # argumento del primer número complejo a operar
            def loop_first_polar_number():
                while 1:
                    # Las variables 'a' y 'b' guardan la parte real e imaginaria respectivamente
                    # del primer número complejo
                    global a, b
                    a = float(input("» Ingresa el módulo de tu primer número complejo: "))
                    if a == 0:
                        print("× Lo siento, ", user_name, ". El número ingresado no es válido, intenta de nuevo.", sep = "")
                        continue
                    else:
                        b = float(input("» Ingresa el argumento de tu primer número complejo: "))
                        print("> Se ha ingresado el número Z₁ = ", end = "")
                        polar_form_number_entry(a, b)
                        break
            # La función 'loop_second_polar_number' recibe el módulo y el
            # argumento del segundo número complejo a operar
            def loop_second_polar_number():
                while 1:
                    # Las variables 'a' y 'b' guardan la parte real e imaginaria respectivamente
                    # del primer número complejo
                    global c, d
                    c = float(input("» Ingresa el módulo de tu segundo número complejo: "))
                    if c == 0:
                        print("× Lo siento, ", user_name, ". El número ingresado no es válido, intenta de nuevo.", sep = "")
                        continue
                    else:
                        d = float(input("» Ingresa el argumento de tu segundo número complejo: "))
                        print("> Se ha ingresado el número Z₂ = ", end = "")
                        polar_form_number_entry(c, d)
                        break
            # La función 'loop_individual_polar_number' recibe el módulo y el
            # argumento de un número complejo a operar junto con el exponente
            # o el índice de la raíz de acuerdo a la operación elegida por el usuario
            def loop_individual_polar_number():
                while 1:
                    # Las variables 'a' y 'b' guardan la parte real e imaginaria respectivamente
                    # del único número complejo
                    global a, b, c
                    a = float(input("» Ingresa el módulo de tu número complejo: "))
                    if a == 0:
                        print("× Lo siento, ", user_name, ". El número ingresado no es válido, intenta de nuevo.", sep = "")
                        continue
                    else:
                        b = float(input("» Ingresa el argumento de tu número complejo: "))
                        if user_choice == "c":
                            c = int(input("» Ingresa 'n' (Z ^ n): "))
                        elif user_choice == "d":
                            c = int(input("» Ingresa 'n' (n ^ √ Z): "))
                        print("> Se ha ingresado el número Z = ", end = "")
                        polar_form_number_entry(a, b)
                        if user_choice == "c":
                            print(" elevado a la", c)
                        elif user_choice == "d":
                            print(" en la raíz", c)
                        break
            if user_choice == "a" or user_choice == "b":
                loop_first_polar_number()
                loop_second_polar_number()
            elif user_choice == "c" or user_choice == "d":
                loop_individual_polar_number()
            print("=== El resultado es: ", end = "")
            if user_choice == "d":
                print("\n", end = "")
            # La variable polar_operation_result recibe el módulo y el argumento
            # de los números ingresados ya operados, lo procesa para que sea 
            # lógico y lo imprime al usuario
            def polar_operation_result(w, z):
                if w < 0:
                    w *= -1
                    z += 180
                while z > 359:
                    z -= 360
                while z < 0:
                    z += 360
                print(w, " Cis ", z, "°", sep = "")
            if user_choice == "a": # Multiplicación de complejos en forma polar
                polar_operation_result(a * c, b + d) 
            if user_choice == "b": # División de complejos en forma polar
                polar_operation_result(a / c, b - d) 
            if user_choice == "c": # Potenciación de complejos en forma polar
                polar_operation_result(a ** c, b * c)
            if user_choice == "d": # Potenciación de complejos en forma polar
                for i in range(c): # Se muestran las raíces siendo 'k' la variable 'i' que cambia con las iteraciones
                    print("ω", i, ": ", sep = "", end = "")
                    polar_operation_result(a ** (1 / c), (b + i * 360) / c)
    elif user_choice_main_menu == "c":
        print("> Has elegido manejar números en forma exponencial.")
    elif user_choice_main_menu == "d":
        print("> Has elegido usar el conversor de números.")
    elif user_choice_main_menu == "x":
        print("Vale, ", user_name, ". ¡Gracias por usar la calculadora de complejos!.", sep = "")
        break
    else:
        print("× Lo siento, ", user_name, ". La opción ingresada no es válida, intenta de nuevo.", sep = "")
        continue
