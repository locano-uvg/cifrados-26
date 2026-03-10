from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_ecb(body: bytes, key: bytes) -> bytes:
    # ECB: cada bloque de 16 bytes se encripta de forma independiente
    # bloques de píxeles idénticos → ciphertext idéntico → patrones visibles
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(body, AES.block_size))
    return encrypted[:len(body)]   


def encrypt_cbc(body: bytes, key: bytes) -> bytes:
    # CBC: cada bloque se XOR con el ciphertext anterior antes de encriptar
    # IV aleatorio → los patrones desaparecen, resultado parece ruido
    cipher = AES.new(key, AES.MODE_CBC)   # IV aleatorio por defecto
    encrypted = cipher.encrypt(pad(body, AES.block_size))
    return encrypted[:len(body)]


def encrypt_ctr(body: bytes, key: bytes) -> bytes:
    # CTR: convierte AES en cifrado de flujo, encripta un contador y XOR con el plaintext
    # no necesita padding, opera byte a byte → tamaño de salida igual al de entrada
    cipher = AES.new(key, AES.MODE_CTR, nonce=b"")   # nonce vacío → counter de 128 bits
    return cipher.encrypt(body)
