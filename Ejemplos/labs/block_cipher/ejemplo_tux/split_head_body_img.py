def split_head_body(image_path: str) -> tuple[bytes, bytes]:
    with open(image_path, "rb") as f:
        data = f.read()
    # PPM tiene un header de 3 líneas: formato, dimensiones, max color
    header_end = 0
    for _ in range(3):
        header_end = data.index(b"\n", header_end) + 1
    return data[:header_end], data[header_end:]