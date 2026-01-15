def validar_contrasena(contrasena):
    pass
def es_primo(numero):
    for i in range(2, numero):
        if numero < 2:
                print(f"{numero} no es primo")
        if numero % i == 0:
            print(f"{numero} no es primo")
            return False
    print(f"{numero} es primo")
    return True
def primo_hasta(n):
    for i in range(2, n):
        if n < 2:
            print(f"{n} no es primo")
            continue
        if i % n == 0:
            print(f"{i} no es primo")
            continue
        print(f"{i} es primo")  
def validar_varias_contrasenas(*contrasenas, **ops):
    min_length = ops.get('min_length', 8)
    contrasenas_no_validas = []
    contras_validas = []
    for contrasena in contrasenas:
        if not isinstance(contrasena, str):
            print(f"{contrasena} no es una cadena de texto")
            continue
        elif len(contrasena) < min_length:
            print(f"{contrasena} no cumple con el minimo de caracteres")
            contrasenas_no_validas.append(contrasena)
            continue
        elif not any(c.isupper() for c in contrasena):
            print(f"{contrasena} no tiene mayusculas")
            contrasenas_no_validas.append(contrasena)
            continue
        elif not any(c.islower() for c in contrasena):
            print(f"{contrasena} no tiene minusculas")
            contrasenas_no_validas.append(contrasena)
            continue
        elif not any(c.isdigit() for c in contrasena):
            print(f"{contrasena} no tiene numeros")
            contrasenas_no_validas.append(contrasena)
            continue
        contras_validas.append(contrasena)
    return {
        "contrasenas_validas": contras_validas,
        "numero de contrasenas validas": len(contras_validas),
        "contrasenas_no_validas": contrasenas_no_validas,
        "numero de contrasenas no validas": len(contrasenas_no_validas)
    }
print(primo_hasta(5))