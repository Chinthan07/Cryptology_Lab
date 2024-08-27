#/usr/bin/python

#1. Write a python script to encrypt the string using Caesar cipher.
greet='Hello World'
key=3
small=greet.lower()
alpha='abcdefghijklmnopqrstuvwxyz'
for i in small:
    if i in alpha:
        ans=ord(i)
        if(ans==ord('z')):
            updated_ascii=(ans-26)+key
            print(chr(updated_ascii))
        else:
            cipher=chr(ord(i)+key)
            print(cipher)
    else:
        print(" ")
        
        
    

#2. Write a Python script to Modify the above script to shift cipher based on user choice. 
greet=input('Enter the String: ')
key=3
small=greet.lower()
alpha='abcdefghijklmnopqrstuvwxyz'
for i in small:
    if i in alpha:
        ans=ord(i)
        if(ans==ord('z')):
            updated_ascii=(ans-26)+key
            print(chr(updated_ascii))
        else:
            cipher=chr(ord(i)+key)
            print(cipher)
    else:
        print(" ")


#3. Write a Python script to convert cipher text into uppercase characters and split the cipher into group of 5 of characters.
greet = input('Enter the String to convert and group into 5 characters: ')
key = 3
cipher_text = ""

small = greet.lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in small:
    if i in alpha:
        ans = ord(i)
        if ans + key > ord('z'):
            updated_ascii = (ans - 26) + key
        else:
            updated_ascii = ans + key
        upr = chr(updated_ascii).upper()
        cipher_text += upr
    else:
        cipher_text += i


cipher_text = cipher_text.replace(" ", "")
groups = [cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)]

for group in groups:
    print(group)



#4. Write a Python program to Find the histogram for each characters. 
from collections import defaultdict

def generate_histogram(string):
    histogram = defaultdict(int)
    
    for char in string:
        histogram[char] += 1

    for char, freq in sorted(histogram.items()):
        print(f"'{char}': {'*' * freq}")            # * represents frequency of Element 
        
input_string = input('Enter the string to display frequency: ')
generate_histogram(input_string)



#5. Write a Python script to read the contents from the file. 
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")

file_path = input('Enter the file path with extension of current working Directory: ')

read_file(file_path)


#6. Write a Python script to encrypt the contents from the file. 

def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        encrypted_content = caesar_cipher(content, key)
        
        if output_file:
            with open(output_file, 'w') as file:
                file.write(encrypted_content)
            print(f"Encrypted content has been saved to '{output_file}'.")
        else:
            print("Encrypted content:\n")
            print(encrypted_content)
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_file}' or write to '{output_file}'.")

input_file = input('Enter the input file path with extension: ')
output_file = input('Enter the output file path (or press Enter to print the encrypted content): ')
key = int(input('Enter the encryption key (number): '))

encrypt_file(input_file, output_file, key)



#7. Do validation to the python program (2) 
#   - not to accept special characters 
#   - not to accept numeric values 
#   - not to accept empty value 
#   - accept only string
#   - string should be lowercase if not convert the case 

def validate_input(greet):
    if not greet:
        print("Error: Input cannot be empty.")
        return False
    
    if not greet.isalpha():
        print("Error: Input must contain only alphabetic characters (no numbers or special characters).")
        return False

    return True

def generate_cipher(greet, key=3):
    small = greet.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ""

    for i in small:
        if i in alpha:
            ans = ord(i)
            if ans + key > ord('z'):
                updated_ascii = (ans - 26) + key
            else:
                updated_ascii = ans + key
            upr = chr(updated_ascii).upper()
            cipher_text += upr

    cipher_text = cipher_text.replace(" ", "")
    groups = [cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)]

    for group in groups:
        print(group)

greet = input('Enter the string: ')

if validate_input(greet):
    generate_cipher(greet)




#8. Write a Python program to checks if two given strings are anagrams of each other.
#example: mug, gum
#         cork, rock
#         note, tone
def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True

string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")




#9. Write a Python program to check the given string is palindrome or not
#Do not use built in functions 
#Example: MADAM 
#         RACECAR
#         LEVEL
#         CIVIC

def is_palindrome(s):
    s = s.lower()
    
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

input_string = input('Enter the string: ')

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")



#10. Write a Python program to check if a substring is present in a given string.
#Example: Understand -- stand

def is_substring_present(main_string, sub_string):
    main_len = len(main_string)
    sub_len = len(sub_string)
    
    for i in range(main_len - sub_len + 1):
        j = 0
        while j < sub_len and main_string[i + j] == sub_string[j]:
            j += 1
        
        if j == sub_len:
            return True
    
    return False

main_string = input('Enter the main string: ')
sub_string = input('Enter the substring to search for: ')

if is_substring_present(main_string, sub_string):
    print(f"'{sub_string}' is present in '{main_string}'.")
else:
    print(f"'{sub_string}' is not present in '{main_string}'.")


 
#11. Explore string module 
#   import the string module in your python script. 
#   print all the lowercase characters
#   print all the uppercase characters 
#   print all the lowercase and uppercase characters
#   print all the digits 
#  print all the punctuation symbols  
#   count the total number of punctuation symbols
 
import string

lowercase_chars = string.ascii_lowercase
print("Lowercase characters:")
print(lowercase_chars)

uppercase_chars = string.ascii_uppercase
print("\nUppercase characters:")
print(uppercase_chars)

all_letters = string.ascii_letters
print("\nLowercase and Uppercase characters:")
print(all_letters)

digits = string.digits
print("\nDigits:")
print(digits)

punctuation = string.punctuation
print("\nPunctuation symbols:")
print(punctuation)

punctuation_count = len(punctuation)
print("\nTotal number of punctuation symbols:", punctuation_count)


