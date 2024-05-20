import random

def rand_key(n):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''
    for i in range(n):
        key += alpha[random.randint(0,51)]
    return key

def encrypt(msg, key):
    cipher_text = ''
    for i in range(0, len(msg)):
        char = msg[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_base = ord('A') if key[i].isupper() else ord('a')
            cipher_text += chr(((ord(char) - base) + (ord(key[i]) - key_base)) % 26 + base)
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    decrypt_text = ''
    for i in range(0, len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_base = ord('A') if key[i].isupper() else ord('a')
            decrypt_text += chr(((ord(char) - base) - (ord(key[i]) - key_base)) % 26 + base)
        else:
            decrypt_text += char
    return decrypt_text


with open("msg.txt","r") as f:
    msg = f.read()

key = rand_key(len(msg))
if len(msg) == len(key):
    cipher_text = encrypt(msg, key)
    print(cipher_text)
    plainT = decrypt(cipher_text, key)
    print(plainT)
    with open("op.txt", "w") as f:
        f.write("Cipher text: " + cipher_text)
        f.write("\nPlain Text: " + plainT)
    