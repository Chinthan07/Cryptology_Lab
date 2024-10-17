# 1. Write a Python script to encrypt columnar transposition using keyword. 

def columnar_transposition_encrypt(plaintext, keyword):
    matrix = ['' for _ in range(len(keyword))]
    key_order = sorted(list(enumerate(keyword)), key=lambda x: x[1])
    key_indices = [item[0] for item in key_order]

    idx = 0
    for i in range(len(plaintext)):
        matrix[idx] += plaintext[i]
        idx = (idx + 1) % len(keyword)

    ciphertext = ''.join([matrix[key_indices.index(i)] for i in range(len(keyword))])

    return ciphertext

plaintext = input('Enter the Plain Text: ')
keyword =input('Enter the Key: ')
ciphertext = columnar_transposition_encrypt(plaintext, keyword)
print(f"Ciphertext: {ciphertext}")


# 2. Write a Python script to encrypt double columnar transposition. 

def double_columnar_transposition_encrypt(plaintext, keyword1, keyword2):
    intermediate_ciphertext = columnar_transposition_encrypt(plaintext, keyword1)
    
    ciphertext = columnar_transposition_encrypt(intermediate_ciphertext, keyword2)
    
    return ciphertext

plaintext = input('Enter the Plain Text: ')
keyword1 = input('Enter Key 1: ')
keyword2 = input('Enter Key 2: ')
ciphertext = double_columnar_transposition_encrypt(plaintext, keyword1, keyword2)
print(f"Ciphertext: {ciphertext}")


# 3. Write a Python script to encrypt the message “She is listening” using the 6-character keyword “PASCAL” with Vigenere cipher.

def vigenere_encrypt(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    ciphertext = ""

    for i in range(len(plaintext)):
        if plaintext[i].upper() in alphabet:
            shift = alphabet.index(keyword_repeated[i].upper())
            new_char = alphabet[(alphabet.index(plaintext[i].upper()) + shift) % 26]
            if plaintext[i].isupper():
                ciphertext += new_char
            else:
                ciphertext += new_char.lower()
        else:
            ciphertext += plaintext[i]

    return ciphertext

plaintext = "She is listening"
keyword = "PASCAL"
ciphertext = vigenere_encrypt(plaintext, keyword)
print(f"Ciphertext: {ciphertext}")


# 4. Write a Python script to encrypt and decrypt Hill cipher

import numpy as np

def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def matrix_mod_inv(matrix, modulus):
    # Calculate the determinant of the matrix
    det = int(np.round(np.linalg.det(matrix))) % modulus
    # Find the modular inverse of the determinant
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under modulo", modulus)

    # Calculate the adjugate matrix
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)  # Padding with 'X' if needed

    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = [ord(char) - 65 for char in plaintext[i:i+n]]
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join([chr(int(num) + 65) for num in encrypted_block])

    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    inverse_key_matrix = matrix_mod_inv(key_matrix, 26)  # Calculate modular inverse matrix
    plaintext = ""

    for i in range(0, len(ciphertext), n):
        block = [ord(char) - 65 for char in ciphertext[i:i+n]]
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext += ''.join([chr(int(num) + 65) for num in decrypted_block])

    return plaintext

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plaintext = input('Enter the Plain Text: ')
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print(f"Decrypted Text: {decrypted_text}")


# Bonus Point:
# 5. Write a Python script to perform Kasiski test. 

import re
from collections import Counter

def kasiski_test(ciphertext):
    sequences = {}
    for i in range(len(ciphertext) - 3):
        seq = ciphertext[i:i+3]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]

    repeated_sequences = {k: v for k, v in sequences.items() if len(v) > 1}

    distances = []
    for positions in repeated_sequences.values():
        distances.extend([positions[i] - positions[i-1] for i in range(1, len(positions))])

    gcds = Counter([gcd(dist, 26) for dist in distances])
    most_common_gcd = gcds.most_common(1)[0][0]

    return most_common_gcd

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

ciphertext = "TEXTENCRYPTEDWITHREPEATEDPATTERNS"
key_length = kasiski_test(ciphertext)
print(f"Estimated Key Length: {key_length}")
