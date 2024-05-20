import random

def caesarCipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

msg = input("Enter a message: ")
key = random.randint(10,100)

cipherText = caesarCipher(msg, key)
print("Encrypted Text:", cipherText)

plainText = caesarCipher(cipherText, -key)
print("Decrypted Text:", plainText)
