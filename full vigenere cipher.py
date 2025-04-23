# Full Vigenere Cipher Implementation

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def generate_full_vigenere_table():
    table = []
    for i in range(26):
        # Each row is the alphabet shifted by i positions
        row = [number_to_letter((j + i) % 26) for j in range(26)]
        table.append(row)
    return table

def full_vigenere_encrypt(plaintext, key):
    table = generate_full_vigenere_table()
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper()
    
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
            
        # Get row index from key letter
        row = letter_to_number(key[i % len(key)])
        # Get column index from plaintext letter
        col = letter_to_number(plaintext[i])
        
        # Use tabular lookup to find ciphertext letter
        ciphertext += table[row][col]
    
    return ciphertext

def full_vigenere_decrypt(ciphertext, key):
    table = generate_full_vigenere_table()
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
            
        # Get row index from key letter
        row = letter_to_number(key[i % len(key)])
        
        # Find the column where the table matches the ciphertext letter
        col = 0
        for j in range(26):
            if table[row][j] == ciphertext[i]:
                col = j
                break
        
        plaintext += number_to_letter(col)
    
    return plaintext

if __name__ == "__main__":
    plaintext = "Vigenere Cipher"
    key = "SPICE"
    
    print("Full Vigenere Cipher")
    print("-------------------")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    table = generate_full_vigenere_table()
    print("\nVigenere Table (first 5x5 section):")
    print("  | A B C D E")
    print("--+----------")
    for i in range(5):
        row_label = number_to_letter(i)
        print(f"{row_label} | {' '.join(table[i][:5])}")
    print("...\n")
    
    encrypted = full_vigenere_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = full_vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")