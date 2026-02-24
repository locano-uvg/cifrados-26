from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import io

def aes_decrypt_image(input_image_path, output_image_path, key):
    # Cargar la imagen cifrada
    with open(input_image_path, "rb") as f:
        ciphertext = f.read()

    # Descifrado AES en modo ECB
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_image_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Guardar la imagen descifrada
    with open(output_image_path, "wb") as f:
        f.write(decrypted_image_data)

# Ejemplo de uso
key = input("Ingrese la clave AES (debe ser 16, 24 o 32 bytes): ").encode('utf-8')
# Transcribir la clave a bytes
key = bytes.fromhex(key.decode('utf-8'))
print('key:', key)
file_name =  r'lab3/problema1/CBC/ayno.decripted.jpeg'
file_name_encrypted = file_name.split('.')[0] + "_encrypted_image.jpeg"
# Descifrar imagen
aes_decrypt_image(file_name_encrypted, file_name, key)
