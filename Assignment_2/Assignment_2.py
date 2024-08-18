#String Operations in Python
#=====================================

#1. Find the length of the string
string = "Hello, World!"
length = len(string)
print(length)

#2. Slice the string as per your choice 
string = "Hello, World!"
sliced_string = string[1:6]  
print(sliced_string)

#3. Concatenate two strings 
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)

#4. Convert  lower case in to uppercase character
string = "hello, world!"
uppercase_string = string.upper()
print(uppercase_string)
 
#5. Convert upper case into lower case characters
string = "HELLO, WORLD!"
lowercase_string = string.lower()
print(lowercase_string)

#6. convert the character into Unicode ( Ascii values)
character = 'A'
unicode_value = ord(character)
print(unicode_value)

#7. convert Unicode into character 
unicode_value = 65
character = chr(unicode_value)
print(character)


#8. Check whether the given "substring" exists in the string
string = "Hello, World!"
substring = "World"
exists = substring in string
print(exists)

#9. Replace the character 'k' with 'h'
string = "kite"
replaced_string = string.replace('k', 'h')
print(replaced_string)

#10. Pad the string with "x" at the end
string = "Hello"
padded_string = string.ljust(10, 'x')
print(padded_string)

#11. remove leading and trailing whitespace or specified characters from the string
string = "   Hello, World!   "
trimmed_string = string.strip()
print(trimmed_string)

#12. split the given string in to group of five characters 
string = "This is a string that needs to be split."
n = 5
groups = [string[i:i+n] for i in range(0, len(string), n)]
print(groups)

#13. count total number of words 
string = "This is a sample string with several words."
word_count = len(string.split())
print(word_count)

#14. Find the frequency of each characters in the string 
from collections import Counter

string = "hello"
frequency = Counter(string)
print(frequency)


#STDIN and File operators 
#=======================

#15. get the file name from the user 
filename = input("Enter the file name: ")
print(filename)

#16. check the file exist or not 
import os

filename = "myfile.txt"
file_exists = os.path.isfile(filename)
print(file_exists)

#Looping and File handling 
#=======================

#17. read the contents from the file 
filename = "myfile.txt"
with open(filename, 'r') as file:
    contents = file.read()
print(contents)

#18. reverse the contents from the file 
filename = "myfile.txt"
with open(filename, 'r') as file:
    contents = file.read()
reversed_contents = contents[::-1]
print(reversed_contents)

#19. Write into the file 
filename = "myfile.txt"
with open(filename, 'w') as file:
    file.write("This is a new content.")


#Math operations 
#20. convert Frequency in to percentage (continuation of 12th Question)
total_characters = len(string)
frequency_percentage = {char: (count / total_characters) * 100 for char, count in frequency.items()}
print(frequency_percentage)

#21. Perform modular arithmetic operation 
a = 10
b = 3
mod_result = a % b
print(mod_result)


#22. Find the prime numbers 
#    check the given number is prime or not 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 29
print(is_prime(number))

#print the prime numbers with the given range 
def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(primes_in_range(10, 50))

#23. Check the given two numbers are co prime or not 
import math

def are_coprime(a, b):
    return math.gcd(a, b) == 1

print(are_coprime(15, 28))

#24. find the factors for the given number ( can use python library)
import sympy

number = 28
factors = sympy.divisors(number)
print(factors)

#25. generate 10 random numbers 
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)

#26. Explore : Miller-Rabin Test (pen paper method)
"""
    The Miller-Rabin primality test is a probabilistic algorithm used to determine if a number is prime.
    It is an improvement over simpler primality tests and is particularly useful for large numbers. 
    To understand the Miller-Rabin test, it's helpful to break it down into a pen-and-paper method.

    1. Check for small divisors: Quickly eliminate numbers divisible by small primes (2, 3, 5, 7, etc.).
    2. Express n-1 as 2^r * d: Decompose n-1 into the form 2^r * d, where d is odd.
    3. Witness selection: Choose a random base 'a' between 2 and n-2.
    4. Compute x: Calculate x = a^d mod n.
    5. Test for primality:
        If x is congruent to 1 or n-1 mod n, the number is probably prime.
        Otherwise, repeat the following steps for i from 0 to r-1:
            x = (x^2) mod n
            If x is congruent to 1 mod n, the number is composite.
            If x is congruent to n-1 mod n, the number is probably prime.
    6. Repeat the test: Perform steps 3-5 multiple times with different random bases to increase confidence in the result.
"""


