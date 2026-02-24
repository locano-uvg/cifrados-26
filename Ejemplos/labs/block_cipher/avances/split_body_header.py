import numpy as np
from PIL import Image
# Ejemplo de cómo procesar una imagen manteniendo el header
def process_image(image_path: str) -> tuple[bytes, bytes]:
    """
    Separa el header y los datos de píxeles de una imagen.
    """
    with Image.open(image_path) as img:
        # Convertir a RGB si es necesario
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Obtener datos de píxeles
        pixel_data = img.tobytes()
        
        # Obtener información del header
        header_info = {
            'mode': img.mode,
            'size': img.size
        }
        
        return header_info, pixel_data