def validar_contrasena(contrasena,**ops):
    min_length = ops.get("min_length", 8)
    errores = []
    if not isinstance(contrasena, str):
        return False, f"La contraseña debe ser texto {min_length}"
    if len(contrasena) < min_length:
        errores.append(f"no cumple longitud minima")
    if not any(c.isupper() for c in contrasena):
        errores.append("Falta mayuscula")
    if not any(c.islower() for c in contrasena):
        errores.append("Falta minuscula")
    if not any(c.isdigit() for c in contrasena):
        errores.append("Falta numero")
    if errores:
        return False, ", ".join(errores)
    return True, "Contraseña valida"
def es_primo(numero):
    if numero < 2:
        return False, f"{numero} no es primo"
    for i in range(2, numero):
        if numero % i == 0:
            return False, f"{numero} no es primo"
    return True, f"{numero} es primo"
def primo_hasta(n):
    son_primos = []
    no_primos = []
    if n < 2:
        no_primos.append(f"no hay numeros primos {n}")
    for i in range(2, n + 1):
        for d in range(2, i):
            if i % d == 0:
                no_primos.append(f"{i} no es primo")
                break
        else:
            son_primos.append(f"{i} es primo")
    return {
        "son primos": son_primos ,
        "no son primos": no_primos
    }
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
def examinador_texto(texto):
    mayusculas = []
    minusculas = []
    numeros = []
    elementos_extras = []
    for c in texto:
        if c.isupper():
            mayusculas.append(c)
        elif c.islower():
            minusculas.append(c)
        elif c.isdigit():
            numeros.append(c)
        elif c in "!@#$5^&*":
            elementos_extras.append(c)
    len(mayusculas)
    num_mayusculas = len(mayusculas)
    num_minusculas = len(minusculas)
    num_numeros = len(numeros)
    num_elementos = len(elementos_extras)
    return {
        "mayusculas": mayusculas, "numero de mayusculas": num_mayusculas,
        "minusculas": minusculas, "numero de minusculas": num_minusculas,
        "numeros": numeros, "cantidad de numeros": num_numeros,
        "elementos_extras": elementos_extras, "numero de elementos": num_elementos,
    }



