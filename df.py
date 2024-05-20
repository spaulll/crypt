import random

def is_primitive_root(g, p):
    values = set()
    for n in range(1, p):
        values.add(pow(g, n, p))
    return len(values) == p - 1

# Choose prime number p
p = 31

# Find a primitive root g for p
for g in range(2, p):
    if is_primitive_root(g, p):
        break
else:
    raise ValueError("No primitive root found for p={}".format(p))

# Alice generates her private key a
a = random.randint(1, p-1)

# Alice computes her public key A
A = pow(g, a, p)

# Bob generates his private key b
b = random.randint(1, p-1)

# Bob computes his public key B
B = pow(g, b, p)

# Alice and Bob exchange their public keys
# Alice computes the shared secret key
alice_secret_key = pow(B, a, p)

# Bob computes the shared secret key
bob_secret_key = pow(A, b, p)

print("Prime number (p):", p)
print("Primitive root (g):", g)
print("Alice's private key:", a)
print("Alice's public key:", A)
print("Bob's private key:", b)
print("Bob's public key:", B)
print("Alice's secret key:", alice_secret_key)
print("Bob's secret key:", bob_secret_key)