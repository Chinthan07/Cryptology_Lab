
import math

#1. Write a python script to get the binary values from the user and perform XOR operation. 
def xor_operation(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    xor_result = num1 ^ num2
    
    return bin(xor_result)[2:].zfill(len(bin1))

binary1 = input("Enter first binary value: ")
binary2 = input("Enter second binary value: ")

if len(binary1) != len(binary2):
    print("Both binary values must be of the same length.")
else:
    result = xor_operation(binary1, binary2)
    print(f"The XOR result is: {result}")


#2. Write a Python script that implements a simple 4-bit LFSR. The initial state of the register and the tap positions should be user inputs. 
#   Simulate 10 steps of the LFSR, displaying the state of the register at each step.

def lfsr(seed, taps, steps):
    state = seed
    print(f"Initial state: {state}")
    
    for step in range(steps):
        feedback_bit = 0
        for tap in taps:
            feedback_bit ^= int(state[tap - 1])
        
        state = str(feedback_bit) + state[:-1]
        
        print(f"Step {step + 1}: {state}")

initial_state = input("Enter the initial state (4 bits): ")

tap_positions = list(map(int, input("Enter the tap positions as space-separated integers (e.g., 2 3  bits of 2 and 3 will be XORed): ").split()))

lfsr(initial_state, tap_positions, 10)


#3. Write a report on attacks on LFSR. Explain any one attack in detail. 

######### Refer Document file  LFSR (Microsoft Word)


#BONUS POINT:
#4.  write a python script to break hill cipher (2X2) using known plain text attack. 
#	Known Plaintext: "MEET"

# Known plaintext and corresponding ciphertext
plaintext = "MEET"
ciphertext = "URRG"
# Convert letters to numbers (A=0, B=1, ..., Z=25)
P = [
    [ord(plaintext[0]) - ord('A'), ord(plaintext[1]) - ord('A')],
    [ord(plaintext[2]) - ord('A'), ord(plaintext[3]) - ord('A')]
]

C = [
    [ord(ciphertext[0]) - ord('A'), ord(ciphertext[1]) - ord('A')],
    [ord(ciphertext[2]) - ord('A'), ord(ciphertext[3]) - ord('A')]
]

# Calculate the determinant of P (mod 26)
det_P = (P[0][0] * P[1][1] - P[0][1] * P[1][0]) % 26

# Check if gcd(det_P, 26) == 1
if math.gcd(det_P, 26) != 1:
    print(f"Determinant {det_P} is not coprime with 26; cannot break Hill cipher.")
else:
    print(f"Determinant {det_P} is coprime with 26; proceeding to find the key.")

    # Function to find modular inverse
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    # Find the modular inverse of the determinant (mod 26)
    inv_det_P = mod_inverse(det_P, 26)

    if inv_det_P is None:
        raise ValueError("No modular inverse exists for the determinant.")

    # Inverse of P (manual calculation)
    P_inv = [
        [(P[1][1] * inv_det_P) % 26, (-P[0][1] * inv_det_P) % 26],
        [(-P[1][0] * inv_det_P) % 26, (P[0][0] * inv_det_P) % 26]
    ]

    # Normalize negative values
    P_inv = [[(val + 26) % 26 for val in row] for row in P_inv]

    # Calculate the key matrix K
    K = [
        [
            (C[0][0] * P_inv[0][0] + C[0][1] * P_inv[1][0]) % 26,
            (C[0][0] * P_inv[0][1] + C[0][1] * P_inv[1][1]) % 26
        ],
        [
            (C[1][0] * P_inv[0][0] + C[1][1] * P_inv[1][0]) % 26,
            (C[1][0] * P_inv[0][1] + C[1][1] * P_inv[1][1]) % 26
        ]
    ]

    # Display the key matrix
    print("Key Matrix:")
    for row in K:
        print(' '.join(chr(num + ord('A')) for num in row))