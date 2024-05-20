import random

def caesarCipher(msg, key):
    result = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

with open("msg.txt", "r") as f:
    msg = f.read()
key = random.randint(10,100)
with open("op.txt", "w") as f:
    cipherText = caesarCipher(msg, key)
    f.write("Cipher Text: " + cipherText)
    plainText = caesarCipher(cipherText, -key)
    f.write("\nPlain Text: " + plainText)