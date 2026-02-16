import random
def createKey(size):
    key = []
    for i in range(size):
        key.append(random.randint(0,256))
    return key

def createKey2(size):
    key = []
    for i in range(size):
        # append a random bit (0 or 1) to the key
        key.append(bytes([random.randint(0,1)]))
    return key

def cypherText(text, keystream):
    ciphertext = []
    for i in range(len(text)):
        print(f"Texto: {text[i]} - Keystream: {keystream[i]} ")
        print(f"Texto XOR Keystream: {text[i] ^ keystream[i]}")
        ciphertext.append(text[i] ^ keystream[i])
    return ciphertext

def decypherText(ciphertext, keystream):
    text = []
    for i in range(len(ciphertext)):
        text.append(ciphertext[i] ^ keystream[i])
    return text

text = input("Introduce el texto a cifrar: ")
text_to_bytes = text.encode()
print("Texto a bytes: ", text_to_bytes)

# keystream = createKey(len(text_to_bytes))
# keystream = bytes(keystream)
keystream = createKey2(len(text_to_bytes))
print("Keystream: ", keystream)


ciphertext = cypherText(text_to_bytes, keystream)
print("Texto cifrado: ", ciphertext)
print("-"*50)

decyphertext = decypherText(ciphertext, keystream)
print("Texto descifrado: ", bytes(decyphertext).decode())
print("-"*50)

