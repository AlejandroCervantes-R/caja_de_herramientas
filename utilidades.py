def validar_contrasena(contrasena,**ops):
    min_lengt = ops.get("min_lengt", 8)
    errores = []
    
    if len(contrasena) < min_lengt:
        errores.append(f"longitud minima es {min_lengt}")
    if not isinstance(contrasena, str):
        return False, "La contraseña debe ser texto"
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
    for i in range(2, numero):
        if numero < 2:
                print(f"{numero} no es primo")
                return False
        if numero % i == 0:
            print(f"{numero} no es primo")
            return False
    print(f"{numero} es primo")
    return True
def primo_hasta(n):
    if n < 2:
        print(f"{n} no es primo")
        return 
    for i in range(2, n):
        for d in range(2, i):
            if i % d == 0:
                print(f"{i} no es primo")
                break
        else:
            print(f"{i} si es primo")
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
print(validar_contrasena(12345, min_lengt=10))