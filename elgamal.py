import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def random_prime(a, b):
    while True:
        n = random.randint(a, b)
        if is_prime(n):
            return n

def generate_key(q):
    key = random.randint(random.randint(1, q), q)
    while gcd(q, key) != 1:
        key = random.randint(random.randint(1, q), q)
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# Choose two prime numbers, p and q
p = random_prime(10, 100)
q = random_prime(10, 100)

# Compute n = p * q
n = p * q

# Calculate Euler's totient function, phi(n)
phi_n = (p - 1) * (q - 1)

# Select a random integer e, such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
e = random.randint(1, phi_n)
while gcd(e, phi_n) != 1:
    e = random.randint(1, phi_n)

# Compute d, the modular multiplicative inverse of e modulo phi(n)
d = multiplicative_inverse(e, phi_n)

# Select a random integer g, such that 1 < g < n-1
g = random.randint(1, n - 1)
while not is_prime(g):
    g = random.randint(1, n - 1)

# Generate a random integer x, such that 1 < x < q
x = generate_key(q)

# Compute y = g^x mod n
y = power(g, x, n)

# Public key is (e, n) and private key is (d, p, q, x)
public_key = (e, n)
private_key = (d, p, q, x)

print("Public Key:", public_key)
print("Private Key:", private_key)

# Encryption
message = int(input("Enter a message: "))
k = generate_key(q)  # Choose a random integer k
a = power(g, k, n)
b = (message * power(y, k, n)) % n
cipher_text = (a, b)

print("Encrypted Message:", cipher_text)

# Decryption
a, b = cipher_text
s = power(a, x, n)
s_inv = multiplicative_inverse(s, n)
decrypted_message = (b * s_inv) % n

print("Decrypted Message:", decrypted_message)