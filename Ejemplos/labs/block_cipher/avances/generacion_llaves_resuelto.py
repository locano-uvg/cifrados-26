import secrets


def generate_des_key() -> bytes:
    return secrets.token_bytes(8)


def generate_3des_key(key_option: int = 2) -> bytes:
    if key_option not in (2, 3):
        raise ValueError("key_option debe ser 2 o 3")
    return secrets.token_bytes(key_option * 8)


def generate_aes_key(key_size: int = 256) -> bytes:
    if key_size not in (128, 192, 256):
        raise ValueError("key_size debe ser 128, 192 o 256")
    return secrets.token_bytes(key_size // 8)


def generate_iv(block_size: int = 8) -> bytes:
    return secrets.token_bytes(block_size)