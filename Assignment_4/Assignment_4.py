#1. Write a Python program to reverse the content of the string.
#Do not use built in 

input_string = "Cryptology"
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string

print(f"Reversed string: {reversed_string}")


#2. Create a program that performs basic string compression using the counts of repeated characters.
# For example, the string “aabcccccaaa” would become “a2b1c5a3”.
input_string = "aabcccccaaa"
compressed = ""
count = 1

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        compressed += input_string[i - 1] + str(count)
        count = 1

compressed += input_string[-1] + str(count)

print(f"Compressed string: {compressed}")


#3. Get the Caesar cipher from the user. Decrypt the cipher 
cipher_text = input('Enter the Cipher Text: ');
shift = 3  
decrypted_text = ""

for char in cipher_text:
    if char.isalpha():
        shift_base = ord('a')  if char.islower() else ord('A')
        decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
        decrypted_text += decrypted_char
    else:
        decrypted_text += char  

print(f"Decrypted text: {decrypted_text}")


#4. Get the cipher encrypted using shift cipher. Identify the key used to encrypt using brute force 
#   ie all the values in the key space 

plain_text = input('Enter the Plain text: ')

for shift in range(26):  
    decrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            decrypted_text += char

    print(f"Shift {shift}: {decrypted_text}")
    if shift == 3:
        print(f"Correct Key for Shift Cipher is: {decrypted_text}")


#5. Find the k value , Provided cipher text and plain text 
plain_text = input('Enter the Plain text: ')
cipher_text = input('Enter the Cipher text: ')
key = (ord(cipher_text[0]) - ord(plain_text[0])) % 26  

print(f"Key used for encryption: {key}")


#6. Encrypt and decrypt the string using Atbash cipher 
input_text = input('Enter Plain text: ')
encrypted_text = ""
decrypted_text = ""

for char in input_text:
    if char.isalpha():
        shift_base = ord('a') if char.islower() else ord('A')
        encrypted_char = chr(shift_base + (25 - (ord(char) - shift_base)))
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print(f"Encrypted text (Atbash): {encrypted_text}")

# Decryption is the same as encryption for Atbash cipher
for char in encrypted_text:
    if char.isalpha():
        shift_base = ord('a') if char.islower() else ord('A')
        decrypted_char = chr(shift_base + (25 - (ord(char) - shift_base)))
        decrypted_text += decrypted_char
    else:
        decrypted_text += char

print(f"Decrypted text (Atbash): {decrypted_text}")


#7. Encrypt and decrypt using Affine cipher 
#        add validation
input_text = "hello"
a = 5  # Multiplicative key (must be coprime with 26)
b = 8  # Additive key
encrypted_text = ""
decrypted_text = ""

# Encryption: E(x) = (a * x + b) % 26
for char in input_text:
    if char.isalpha():
        shift_base = ord('a') if char.islower() else ord('A')
        x = ord(char) - shift_base
        encrypted_char = chr((a * x + b) % 26 + shift_base)
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print(f"Encrypted text (Affine): {encrypted_text}")

# Decryption: D(y) = a_inv * (y - b) % 26
# Calculate a_inv (modular multiplicative inverse of a under mod 26)
a_inv = 0
for i in range(26):
    if (a * i) % 26 == 1:
        a_inv = i
        break

for char in encrypted_text:
    if char.isalpha():
        shift_base = ord('a') if char.islower() else ord('A')
        y = ord(char) - shift_base
        decrypted_char = chr((a_inv * (y - b)) % 26 + shift_base)
        decrypted_text += decrypted_char
    else:
        decrypted_text += char

print(f"Decrypted text (Affine): {decrypted_text}")
