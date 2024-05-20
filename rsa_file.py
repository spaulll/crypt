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

def key_gen():
    p = prime(100, 1000)
    q = prime(100, 1000)
    ic(p, q)
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

def encrypt(e, n, msg):
    return (msg ** e) % n

def decrypt(d, n, cipher):
    return (cipher ** d) % n

def read_message_from_file(filename):
    try:
        with open(filename, 'r') as file:
            msg = int(file.readline().strip())
            return msg
    except ValueError:
        print("Error: Non-integer value found in the file.")
        exit(1)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        exit(1)

filename = "msg.txt"
msg = read_message_from_file(filename)
e, d, n = key_gen()
ic(e, d, n)
cipher = encrypt(e, n, msg)
plain = decrypt(d, n, cipher)
ic(cipher, plain)
