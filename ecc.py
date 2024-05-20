# from point_ecc import gen_point
from random import randint

def inverse_mod(y, m):
    i = 0
    while True:
        if ((y * i) % m == 1):
            return i
        i += 1

def pointAdd(p: list, q: list, m: int, a):
    if p == q:
        l = ((3 * ((p[0]) ** 2) + a) * inverse_mod(2 * p[1], m)) % m

    if p != q:
        l = ((q[1] - p[1]) * inverse_mod(q[0] - p[0], m)) % m

    x3 = ((l ** 2) - p[0] - q[0]) % m
    y3 = (l * (p[0] - x3) - p[1]) % m
    return [x3,y3]


def pointMul(n: int, p: list, m: int, a: int):
    r = []
    if n == 2:
        return pointAdd(p, p, m, a)
    if n > 2:
        r = pointAdd(p, p, m, a)
        for i in range(n-2):
            r = pointAdd(r, p, m, a)
        return r

def encryption(G, pB, msg, m, a):
    k = randint(2,10)  
    c1 = pointMul(k, G, m , a)
    c2 = pointAdd(msg, pointMul(k, pB, m, a), m, a)
    return [c1, c2]

def decryption(cipher, nB, m , a):
    x = cipher[1]
    y = pointMul(nB, cipher[0], m, a)
    y[1] = -y[1]
    return pointAdd(x, y, m, a)


G = list(map(int, input("Enter the cordinates of G(separated by <space>): ").strip().split()))[:2]

m = int(input("Enter the modulas: "))
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

n = randint(2,10)              #Public key of A
nA = randint(2,n)              #Private key of a
pA = pointMul(nA, G, m, a)

n = randint(2,10)              #Public key of A
nB = randint(2,n)              #Private key of b
pB = pointMul(nB, G, m, a)

msg = list(map(int, input("Enter the message cordinates (separated by <space>): ").strip().split()))[:2]
print(f"Message cordinate is: {msg}")

cipher = encryption(G, pB, msg, m, a)
print(f"Cipher text is: {cipher}")

pT = decryption(cipher, nB, m , a)
print(f"Decrypted text is: {pT}")