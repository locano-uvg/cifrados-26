from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import io

def aes_encrypt_image(input_image_path, output_image_path, key):
    # Cargar la imagen
    with open(input_image_path, "rb") as f:
        image_data = f.read()

    # Cifrado AES en modo ECB
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(image_data, AES.block_size))

    # Guardar la imagen cifrada
    with open(output_image_path, "wb") as f:
        f.write(ciphertext)

# Ejemplo de uso
key = get_random_bytes(16)  # Clave de 128 bits
# Transcribir la clave a hexadecimal
print('key:', key.hex().encode('utf-8'))
file_name =  r'lab3/problema1/ECB/mr-increible.jpeg'
file_name_encrypted = file_name.split('.')[0] + "_encrypted_image.jpeg"
# Cifrar imagen
aes_encrypt_image(file_name, file_name_encrypted, key)
