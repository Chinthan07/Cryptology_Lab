# 1. Write a Python script that takes two integers as input and calculates their GCD using the Euclidean algorithm. 
#    Based on the result, determine whether these numbers are co-prime.
#    If they are co-prime, print a message indicating that they can be used in cryptographic key generation; otherwise, print a message that they are not suitable.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_coprime(a, b):
    if gcd(a, b) == 1:
        print(f"{a} and {b} are co-prime and can be used in cryptographic key generation.")
    else:
        print(f"{a} and {b} are not co-prime and are not suitable for cryptographic key generation.")

# Taking two integers as input
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
check_coprime(a, b)



# 2. Write a python script to take two integer values (number (n) and modulo (m)) from the user and find the modular inverse using extended Euclidean algorithm. 
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse(n, m):
    gcd, x, _ = extended_gcd(n, m)
    if gcd != 1:
        print(f"Modular inverse does not exist for {n} mod {m}.")
    else:
        print(f"The modular inverse of {n} mod {m} is {x % m}.")

# Taking input for n and m
n = int(input("Enter number (n): "))
m = int(input("Enter modulo (m): "))
modular_inverse(n, m)


# 3. Write a Python script that generates a random binary number of length 100. The output should be a string of 100 binary digits (0s and 1s).
#    After generating the binary sequence, implement a function to check whether any subsequence of digits repeats itself within the sequence.

import random

def generate_binary_string(length):
    return ''.join(random.choice('01') for _ in range(length))

def check_repeated_subsequence(binary_str):
    seen = set()
    for i in range(len(binary_str)):
        for j in range(i + 1, len(binary_str) + 1):
            subsequence = binary_str[i:j]
            if subsequence in seen and len(subsequence) > 1:
                print(f"Repeated subsequence found: {subsequence}")
                return True
            seen.add(subsequence)
    print("No repeated subsequences found.")
    return False

# Generate a random binary sequence of length 100
binary_sequence = generate_binary_string(100)
print(f"Generated binary sequence: {binary_sequence}")

# Check for repeated subsequences
check_repeated_subsequence(binary_sequence)


# 4. Write a Python script that performs the Golomb test to the numbers provided below. 
#                    101011001010
#                    111111000000
#    The script should
#           - Perform and print the results of the three Golomb tests on the sequence.
#           - Print a message indicating whether the sequence passes the Golomb tests or not.

def golomb_test(sequence):
    # Test 1: Equal number of 0s and 1s (or difference by at most 1)
    ones = sequence.count('1')
    zeros = sequence.count('0')
    test1 = abs(ones - zeros) <= 1

    # Test 2: Runs test (number of runs of each length should be as expected)
    runs = {'0': [], '1': []}
    current_char = sequence[0]
    current_run_length = 1

    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            current_run_length += 1
        else:
            runs[current_char].append(current_run_length)
            current_char = sequence[i]
            current_run_length = 1
    runs[current_char].append(current_run_length)

    max_run_length = max(len(runs['0']), len(runs['1']))
    test2 = all(len(runs[c]) >= max_run_length // 2 for c in runs)

    # Test 3: Runs of the same length are evenly distributed
    run_lengths_0 = set(runs['0'])
    run_lengths_1 = set(runs['1'])
    test3 = run_lengths_0 == run_lengths_1

    # Print results
    print(f"Test 1 (Equal 0s and 1s): {'Passed' if test1 else 'Failed'}")
    print(f"Test 2 (Runs test): {'Passed' if test2 else 'Failed'}")
    print(f"Test 3 (Even distribution of run lengths): {'Passed' if test3 else 'Failed'}")

    if test1 and test2 and test3:
        print("The sequence passes all Golomb tests.")
    else:
        print("The sequence does not pass the Golomb tests.")

# Sequences to test
sequences = ["101011001010", "111111000000"]

for seq in sequences:
    print(f"\nTesting sequence: {seq}")
    golomb_test(seq)
