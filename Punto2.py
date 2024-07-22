def invertir_cadena(cadena):
    fila = []
    cadena_invertida = " "
    
    for caracter in cadena:
        fila.append(caracter)
    
    while fila:
        caracter = fila.pop()
        cadena_invertida += caracter
    
    return cadena_invertida

cadena_original = input("Ingrese una cadena de caracteres: ")
cadena_invertida = invertir_cadena(cadena_original)
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")



