import base64

def convertir_ascii_a_binario(numero):
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

    if len(binario) < 8:
        binario = binario.rjust(8, '0')
    return binario

def convertir_unicode_a_binario(numero):
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

    if len(binario) < 6:
        binario = binario.rjust(6, '0')
    return binario

def convertir_binario_a_base10(binario):
    base_10 = 0
    for i in range(len(binario)):
        base_10 += int(binario[i]) * (2 ** (len(binario) - i - 1))
    return base_10
    
def obtner_caracter_base64(numero):
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    return caracteres[numero]

def palabra_a_base64(palabra):
    # Paso 2: Convertir caracteres a su representación numérica ASCII
    accii_nums = []
    for char in palabra:
        if ord(char) > 127:
            raise ValueError('La palabra contiene caracteres no ASCII')
        else:
            accii_nums.append(ord(char))

    # Paso 3: Convertir números ASCII a binario
    listado_binarios = []
    for num in accii_nums:
        listado_binarios.append(convertir_ascii_a_binario(num))

    # Paso 4: Agrupar en bloques de 6 bits
    binario = ''.join(listado_binarios)
    bloques_6bits = []
    for i in range(0, len(binario), 6):
        bloque = binario[i:i+6]
        if len(bloque) < 6:
            bloque = bloque.ljust(6, '0')
        bloques_6bits.append(bloque)

    # Paso 5: Convertir bloques de 6 bits a Base64
    base64 = []
    for bloque in bloques_6bits:
        base10 = convertir_binario_a_base10(bloque)
        base64.append(base10)

    # Paso 6: Obtener el carácter en Base64
    caracters_base64 = []
    for x in base64:
        caracters_base64.append(obtner_caracter_base64(x))
    
    return ''.join(caracters_base64)

def base64_a_palabra(palabra_base64):
    # Paso 2: Convertir caracteres Base64 a su representación numérica
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    numeros_base64 = []
    for char in palabra_base64:
        numeros_base64.append(caracteres.index(char))

    # Paso 3: Convertir números Base64 a binario
    listado_binarios = []
    for num in numeros_base64:
        listado_binarios.append(convertir_unicode_a_binario(num))

    # Paso 4: Agrupar en bloques de 6 bits
    binario = ''.join(listado_binarios)
    bloques_8bits = []
    for i in range(0, len(binario), 8):
        bloque = binario[i:i+8]
        if len(bloque) < 8:
            bloque = bloque.ljust(8, '0')
        bloques_8bits.append(bloque)

    # Paso 5: Convertir bloques de 8 bits a Base64
    base10 = []
    for bloque in bloques_8bits:
        base10.append(convertir_binario_a_base10(bloque))

    # Paso 6: Obtener el carácter en Base64
    caracteres_ascii = []
    for x in base10:
        caracteres_ascii.append(chr(x))
    
    return ''.join(caracteres_ascii)

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
base64_resultado = palabra_a_base64(palabra)
print(f'Palabra en Base64: {base64_resultado}')
palabra_resultado = base64_a_palabra(base64_resultado)
print(f'Palabra original: {palabra_resultado}')
