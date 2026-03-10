def string_a_ascii(palabra):
    accii_nums = []
    for char in palabra:
        if ord(char) > 127:
            raise ValueError('La palabra contiene caracteres no ASCII')
        else:
            accii_nums.append(ord(char))

    return accii_nums

def numero_a_binario(numero):
    """
    Transforma un número base 10 a binario.

    Parámetros:
    numero: int > 0

    Retorna:
    str: representación en binario del número
    """
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

    # Completar con ceros a la izquierda para que tenga 8 bits
    while len(binario) < 8:
        binario = '0' + binario
    return binario


def transformar_a_base10(binario):
    """
    Transforma un número binario a base 10.

    Parámetros:
    binario: str

    Retorna:
    int: representación en base 10 del número
    """
    base_10 = 0
    for i in range(len(binario)):
        base_10 += int(binario[i]) * (2 ** (len(binario) - i - 1))
    return base_10


def xor_binario(texto_binario, llave_binario):
    # Paso 3: Aplicar XOR entre la llave y la palabra
    resultado_xor = ''.join(str(int(bit_texto) ^ int(bit_llave)) for bit_texto, bit_llave in zip(texto_binario, llave_binario))
    return resultado_xor

def binario_a_texto(binario):
    """
    Transforma un número binario a texto.

    Parámetros:
    binario: str

    Retorna:
    str: representación en texto del número binario
    """
    texto = ''
    for i in range(0, len(binario), 8):
        texto += chr(transformar_a_base10(binario[i:i + 8]))
    return texto

# Paso 2: Transformar la llave a binario
llave = input("Ingrese la llave: ")
ascii_llave = string_a_ascii(llave)
llave_binario = ''
for x in ascii_llave:
    llave_binario += numero_a_binario(x)

# Entrada de la palabra
palabra = input("Ingrese la palabra: ")
ascii_palabra = string_a_ascii(palabra)
palabra_binario = ''
for x in ascii_palabra:
    palabra_binario += numero_a_binario(x)

# Complementar la llave con la misma longitud que la palabra usando la llave
if len(llave_binario) < len(palabra_binario):
    llave_binario = llave_binario * (len(palabra_binario) // len(llave_binario)) + llave_binario[:len(palabra_binario) % len(llave_binario)] 

texto_cifrado_xor = xor_binario(palabra_binario, llave_binario)


# Paso 4: Mostrar el nuevo texto cifrado con XOR
print(f'\nPalabra en binario: {palabra_binario}')
print(f'Llave en binario: {llave_binario}')
print(f'Binario cifrado con XOR: {texto_cifrado_xor}')
print(f'Text cifrado con XOR: {binario_a_texto(texto_cifrado_xor)}')

