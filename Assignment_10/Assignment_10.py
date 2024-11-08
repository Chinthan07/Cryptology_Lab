#1. Write a Python script to list all the prime numbers from 1 to 100 using Sieve of Eratosthenes.

def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

prime_numbers = sieve_of_eratosthenes(100)
print(prime_numbers)



#2. Write a Python script to implement RSA algorithm using build in functions (both encryption and decryption)
import random
from math import gcd

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

 # Miller-Rabin test
def is_prime(n, k=5): 
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_number(length=8):
    p = 4
    while not is_prime(p, 5):
        p = generate_prime_candidate(length)
    return p

# RSA Key generation
def generate_keys(keysize=8):
    e = d = n = 0

    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)
    while q == p:
        q = generate_prime_number(keysize)

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)

    d = modinv(e, phi)

    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

# RSA Encryption
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

# RSA Decryption
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)
public, private = generate_keys(8)  
message = "Hello"
print("Original Message:", message)

encrypted_msg = encrypt(public, message)
print("Encrypted Message:", encrypted_msg)

decrypted_msg = decrypt(private, encrypted_msg)
print("Decrypted Message:", decrypted_msg)



#3. Write a Python script to implement RSA algorithm with out using build in functions (both encryption and decryption)
import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys():
    p = 61  
    q = 53  
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)  

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

public_key, private_key = generate_keys()

message = "HELLO"
ciphertext = encrypt(public_key, message)
print(f'Encrypted: {ciphertext}')

decrypted_message = decrypt(private_key, ciphertext)
print(f'Decrypted: {decrypted_message}')
