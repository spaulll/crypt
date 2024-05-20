import random

def complement(n):
    result = 0
    while n != 0:
        result = result * 10 + 9
        n //= 10
    return result

def enCrypt(msg, key):
    a = msg + key
    b = a << 2
    c = complement(b) - b
    d = c | key
    e = c & key
    f = d - e
    return f

def deCrypt(cipher, key):
    a = cipher | key
    b = cipher & key
    c = a - b
    d = complement(c) - c
    e = d >> 2
    f = e - key
    return f

msg = int(input("Enter a number: "))
key = random.randint(3, 999)
cipher = enCrypt(msg, key)
print("Cipher text is: ", cipher)
plainT = deCrypt(cipher, key)
print("Decrypted text is: ", plainT)