from utilidades import (validar_contrasena, es_primo, primo_hasta, validar_varias_contrasenas)
def menu():
    while True:
        try:
            print("--- MENU DE HERRAMIENTAS ---")
            print("1. --Validar contraseña--")
            print("2. --Verificar si un número es primo--")
            print("3. --verificar varios numeros primos--")
            print("4. --Validar varias contraseñas--")
            print("5. ------ Salir ------")
            input_usuario = int(input("Seleccione una opción: "))
            if input_usuario == 1:
                min_length = int(input("ingresa la longitud minima de la contrasena: "))
                respuesta_usuario = input("que contrasena quieres usar: ")
                print(validar_contrasena(respuesta_usuario, min_length=min_length))
                continue
            elif input_usuario == 2:
                respuesta_usuario = int(input("que numero quieres saber si es primo: "))
                print(es_primo(respuesta_usuario))
                continue
            elif input_usuario == 3:
                respuesta_usuario = int(input("hasta que numeros quieres ver los primos:"))
                print(primo_hasta(respuesta_usuario))
                continue
            elif input_usuario == 4:
                min_length = int(input("ingresa la longitud minima de las contraseñas: "))
                lista_contrasenas = []
                while True:
                    respuesta_usuario = input("ingresa la contrasena: ")
                    lista_contrasenas.append(respuesta_usuario)
                    if input("quieres agregar otra contrasena? (s/si)(cualquier otro/no): ").lower() != "s":
                        break
                print(validar_varias_contrasenas(*lista_contrasenas, min_length=min_length))
                continue
            elif input_usuario == 5:
                print("Saliendo del programa")
                break
        except ValueError:
            print("Por favor ingresa una opción válida.")
            continue
if __name__ == "__main__":
    print(menu())



