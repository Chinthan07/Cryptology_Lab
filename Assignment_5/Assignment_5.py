#1. Write a Python Program to perform brute force attack on the cipher text “dvvkzecfssprkkve"

ciphertext = "dvvkzecfssprkkve"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for shift in range(1, 26):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            original_pos = alphabet.index(char)
            new_pos = (original_pos - shift) % 26
            decrypted_text += alphabet[new_pos]
        else:
            decrypted_text += char

    print(f"Shift {shift}: {decrypted_text}")



#2. Write a Python program to use brute force attack to decipher the message. 
#Assume Affine cipher was used and "ab" is encrypted as "GL". Find the value of keys. 
#XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS
ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in range(1, 26):
    for b in range(0, 26):
        if (a % 2 != 0) and (a % 13 != 0):
            decrypted_text = ""
            for a_inv in range(1, 26):
                if (a * a_inv) % 26 == 1:
                    for char in ciphertext:
                        if char.isalpha():
                            y = alphabet.index(char)
                            x = (a_inv * (y - b)) % 26
                            decrypted_text += alphabet[x]
                        else:
                            decrypted_text += char

                    if decrypted_text.startswith("AB"):
                        print(f"a = {a}, b = {b}: {decrypted_text}")
                    break


#3. Encrypt the plain text using Rail Fence cipher 

plaintext = "YOURPLAINTEXT"
num_rails = 3
rail = ['' for _ in range(num_rails)]
direction = -1
row = 0

for char in plaintext:
    rail[row] += char
    if row == 0 or row == num_rails - 1:
        direction *= -1
    row += direction

ciphertext = "".join(rail)
print(f"Ciphertext: {ciphertext}")



#4. Decrypt the cipher using Rail Fence
#AAIUJ SIHBE KTEAO TEADE SNUTF EAEMR TAHSA
#RHROA YHNFO AITTE EHCBO FVCAT RNMNS NUTFE
#RASHL WFHLN HIUJS IHTKS OEHNI FISAE FNTIG
#RMRSO LSTIS OKIEH PEOE
ciphertext = "AAIUJSIHBEKTEAOTEADESNUTFEAEMRTAHSARHROAYHNFOAITTEEHCBOFVCATRNMNSNUTFERASHLWFHLNHIUJSIHTKSOEHNIFISAEFNTIGRMRSOLSTISOKIEHPEOE"
num_rails = 3
rail_len = len(ciphertext)

rail = [['\n' for _ in range(rail_len)] for _ in range(num_rails)]

direction = None
row, col = 0, 0

for i in range(rail_len):
    if row == 0:
        direction = 1  
    elif row == num_rails - 1:
        direction = -1  

    rail[row][col] = '*'
    col += 1
    row += direction

index = 0
for r in range(num_rails):
    for c in range(rail_len):
        if rail[r][c] == '*' and index < rail_len:
            rail[r][c] = ciphertext[index]
            index += 1

decrypted_text = ""
row, col = 0, 0
for i in range(rail_len):
    if row == 0:
        direction = 1
    elif row == num_rails - 1:
        direction = -1

    decrypted_text += rail[row][col]
    col += 1
    row += direction

print(f"Decrypted text: {decrypted_text}")
