#1. Assume you intercepted the following ciphertext. Using a statistical attack, find the plaintext
#"XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVX-LQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW" 
from collections import Counter

def get_char_frequency(ciphertext):
    frequency = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    
    sorted_freq = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_freq

def decrypt_ciphertext(ciphertext, freq_mapping):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            decrypted_text.append(freq_mapping.get(char, char))  
        else:
            decrypted_text.append(char)  
    return ''.join(decrypted_text)

ciphertext = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVX-LQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"

frequency_sorted = get_char_frequency(ciphertext)

cipher_freq_order = [item[0] for item in frequency_sorted]  # Most frequent letters in ciphertext
english_freq_order = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 
                      'l', 'u', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'f', 
                      'z', 'x', 'j', 'k', 'q', 'w']  # Most frequent letters in English

freq_mapping = {}
for i in range(min(len(cipher_freq_order), len(english_freq_order))):
    freq_mapping[cipher_freq_order[i]] = english_freq_order[i]

decrypted_text = decrypt_ciphertext(ciphertext, freq_mapping)

print("Ciphertext:", ciphertext)
print("\nFrequency sorted:", frequency_sorted)
print("\nDecrypted text:", decrypted_text)


#2. Write a Python script to encrypt using Rail Fence (Zig zag ) with three rows and with key (ONE).
def rail_fence_encrypt(plaintext, num_rails):
    rail = [['\n' for _ in range(len(plaintext))]
            for _ in range(num_rails)]
    
    direction_down = False
    row, col = 0, 0
    
    for char in plaintext:
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        
        rail[row][col] = char
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    ciphertext = []
    for i in range(num_rails):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                ciphertext.append(rail[i][j])
    
    return "".join(ciphertext)

plaintext = input('Enter the Plaintext: ')
num_rails = int(input('Enter the rails required: '))
ciphertext = rail_fence_encrypt(plaintext, num_rails)
print(f"Ciphertext: {ciphertext}")


#3. Write a python script to encrypt columnar transposition 
import math

def columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    
    columns = ['' for _ in range(num_cols)]
    
    for i, char in enumerate(plaintext):
        column_index = i % num_cols
        columns[column_index] += char
    
    sorted_columns = [x for _, x in sorted(zip(key, columns))]
    
    ciphertext = ''.join(sorted_columns)
    
    return ciphertext

plaintext = input('Enter Plain Text: ')
key = input('Enter the Key (word): ')
ciphertext = columnar_transposition_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")


#4. Write a Python script to decrypt Rail Fence Cipher 
def rail_fence_decrypt(ciphertext, num_rails):
    rail = [['\n' for _ in range(len(ciphertext))]
            for _ in range(num_rails)]
    
    direction_down = None
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == num_rails - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == num_rails - 1:
            direction_down = False
        
        result.append(rail[row][col])
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    return "".join(result)

ciphertext = input('Enter the Cipher text: ')
num_rails = int(input('Enter the rails required: '))
plaintext = rail_fence_decrypt(ciphertext, num_rails)
print(f"Decrypted text: {plaintext}")
