
from Crypto.Random import get_random_bytes
from split_head_body_img import split_head_body
from aes_encrypt_modes import encrypt_ecb, encrypt_cbc, encrypt_ctr
import os


def write_ppm(header: bytes, body: bytes, output_path: str) -> None:
    with open(output_path, "wb") as f:
        f.write(header + body)


root = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(root, "tux.ppm")

key = get_random_bytes(16)   # Clave de 128 bits
print(f"Clave AES (hex): {key.hex()}\n")

header, body = split_head_body(input_path)
print(f"Header: {len(header)} bytes")
print(f"Body  : {len(body)} bytes  ({len(body) // 3} píxeles)\n")


encrypted_body_cbc = encrypt_cbc(body, key)
encrypted_body_ecb = encrypt_ecb(body, key)
encrypted_body_ctr = encrypt_ctr(body, key)


out_path = os.path.join(root, f"tux_encrypted_ecb.ppm")
print(f"[ECB] → {out_path}")
write_ppm(header, encrypted_body_ecb, out_path)
out_path = os.path.join(root, f"tux_encrypted_cbc.ppm")
print(f"[CBC] → {out_path}")
write_ppm(header, encrypted_body_cbc, out_path)
out_path = os.path.join(root, f"tux_encrypted_ctr.ppm")
print(f"[CTR] → {out_path}")
write_ppm(header, encrypted_body_ctr, out_path)


