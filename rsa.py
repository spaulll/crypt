from math import gcd
from random import randint

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
  p = prime(10, 100)
  q = prime(10, 100) 

  
  if p == q:
    q = prime(10, 100)

  n = p * q
  fi_n = (p - 1) * (q - 1)
  i = 0
  while True:
    e = randint(2, fi_n)
    if gcd(e, fi_n) == 1:
      d = (1 + (i * fi_n))/e
      i += 1
      if(d - int(d)) == 0:
        return e, int(d), n
       
def encrypt(e, n, msg):
  return (msg ** e) % n

def decrypt(d, n, cipher):
  return (cipher ** d) % n

def main():
  e, d, n = key_gen()

  msg = int(input("Enter a number: "))
  cipher = encrypt(e, n, msg)
  print("Cipher Text: ", cipher)
  plain = decrypt(d, n, cipher)
  print("Plain Text: ", plain)

if __name__ == '__main__':
  main()