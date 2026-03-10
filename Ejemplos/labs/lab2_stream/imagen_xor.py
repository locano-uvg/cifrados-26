import io
import base64
from PIL import Image ## pip install pillow


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


def xor_binario(texto_binario, llave_binario):
    # Paso 3: Aplicar XOR entre la llave y la palabra
    resultado_xor = ''.join(str(int(bit_texto) ^ int(bit_llave)) for bit_texto, bit_llave in zip(texto_binario, llave_binario))
    return resultado_xor

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Leer la imagen en formato binario
        image_binary = image_file.read()

        # Convertir la imagen binaria a base64
        image_base64 = base64.b64encode(image_binary).decode("utf-8")

    return image_base64

def base64_to_binary(base64_data):
    # Decodificar la cadena base64 a bytes
    binary_data = base64.b64decode(base64_data)

    # Obtener la representación binaria como cadena de bits
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    return binary_string


def binary_to_base64(binary_data):
    binary_bytes = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')
    base64_result = base64.b64encode(binary_bytes).decode("utf-8")
    return base64_result

def base64_to_image(base64_data, output_path):
    image_data = base64.b64decode(base64_data)
    with open(output_path, 'wb') as image_file:
        image_file.write(image_data)





image_path = r'Ejemplos/labs/lab2/assets/imagen1.jpg'
base64_representation = image_to_base64(image_path)
print("Base64 de la imagen:\n", base64_representation)


binario_64 = base64_to_binary(base64_representation)
print("Base64 de la imagen:\n", binario_64)
input()



# Convertir la clave a una lista de números ASCII
clave = input("Ingrese la clave para cifrar la imagen: ")
ascii_llave = string_a_ascii(clave)
llave_binario = ''
for x in ascii_llave:
    llave_binario += numero_a_binario(x)

if len(llave_binario) < len(binario_64):
    llave_binario = llave_binario * (len(binario_64) // len(llave_binario)) + llave_binario[:len(binario_64) % len(llave_binario)] 

texto_cifrado_xor = xor_binario(binario_64, llave_binario)

print("xor de la imagen:\n", texto_cifrado_xor)


# Convertir el resultado a base64
result_base64 = binary_to_base64(texto_cifrado_xor)

# Guardar el resultado como una imagen
output_image_path = "Ejemplos/labs/lab2/assets/imagen_xor.png"
base64_to_image(result_base64, output_image_path)

print("Imagen guardada en:", output_image_path)


