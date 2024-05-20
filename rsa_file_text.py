from math import gcd
from random import randint
from icecream import ic

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(a, b):
    while True:
        n = randint(a, b)
        if is_prime(n):
            return n

def text_to_int(message):
    # Simple encoding using ASCII values
    return [ord(char) for char in message]

def int_to_text(encoded_message):
    # Simple decoding from ASCII values
    return ''.join([chr(code) for code in encoded_message])

def key_gen():
    p = prime(10, 100)
    q = prime(10, 100)
    if p == q:
        q = prime(100, 1000)
    n = p * q
    fi_n = (p - 1) * (q - 1)
    i = 0
    while True:
        e = randint(fi_n//2, fi_n)
        if gcd(e, fi_n) == 1:
            d = (1 + (i * fi_n))/e
            i += 1
            if (d - int(d)) == 0:
                return e, int(d), n

def encrypt(e, n, message):
    encoded_message = text_to_int(message)
    encrypted_message = [(char ** e) % n for char in encoded_message]
    return encrypted_message

def decrypt(d, n, encrypted_message):
    decrypted_message = [(char ** d) % n for char in encrypted_message]
    decoded_message = int_to_text(decrypted_message)
    return decoded_message

def read_message_from_file(filename):
    try:
        with open(filename, 'r') as file:
            message = file.read().strip()
            print(f"Content of {filename}: ", message)
            return message
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        exit(1)

filename = "msg.txt"
message = read_message_from_file(filename)
e, d, n = key_gen()

encrypted_message = encrypt(e, n, message)
decrypted_message = decrypt(d, n, encrypted_message)
print(f"Encrypted message: {encrypted_message}")
print(f"Dcrypted message: {decrypted_message}")
output_file = "op.txt"
with open (output_file, "w") as f:
    f.write("Encrypted msg: " + str(encrypted_message) + "\nDecrypted msg: " + decrypted_message)
    print(f"Data has been stored to {output_file}")
