
from PIL import Image # pip install pillow
import numpy as np

def apply_xor_to_images(image_path_original, image_path_key, output_path):
    # Abrir las imágenes
    original_image = Image.open(image_path_original)
    key_image = Image.open(image_path_key)

    # Asegurarse de que ambas imágenes tengan el mismo tamaño
    key_image = key_image.resize(original_image.size)

    # Convertir imágenes a escala de grises y arrays de NumPy
    original_array = np.array(original_image)  # Convertir a escala de grises
    key_array = np.array(key_image)  # Convertir a escala de grises

     # Verificar si las imágenes tienen el mismo número de canales
    if original_array.shape[2] != key_array.shape[2]:
        raise ValueError("Ambas imágenes deben tener el mismo número de canales.")

    # Aplicar la operación XOR píxel a píxel
    xor_array = np.bitwise_xor(original_array, key_array)

    # Crear una nueva imagen a partir del array resultante
    xor_image = Image.fromarray(xor_array.astype(np.uint8))

    # Guardar la imagen resultante
    xor_image.save(output_path)
    print(f"Imagen resultante guardada en: {output_path}")


# Ejemplo de uso
image_path_original =  r'Ejemplos/labs/lab2/assets/imagen3.jpg'
image_path_key =  r'Ejemplos/labs/lab2/assets/imagen4.jpg'
output_path =  r'Ejemplos/labs/lab2/assets/imagen3_merge4.jpg'

apply_xor_to_images(image_path_original, image_path_key, output_path)
