# Running Key Vigenere Cipher Implementation

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def running_key_vigenere_encrypt(plaintext, running_key):
    ciphertext = ""
    # Extract only letters from the running key
    key_stream = ''.join(char for char in running_key.upper() if char.isalpha())
    plaintext = plaintext.upper()
    
    # Check if key is long enough
    if len(key_stream) < sum(c.isalpha() for c in plaintext):
        raise ValueError("Running key is too short for the plaintext")
    
    key_index = 0
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
        
        p = letter_to_number(plaintext[i])
        k = letter_to_number(key_stream[key_index])
        c = (p + k) % 26
        
        ciphertext += number_to_letter(c)
        key_index += 1
    
    return ciphertext

def running_key_vigenere_decrypt(ciphertext, running_key):
    plaintext = ""
    # Extract only letters from the running key
    key_stream = ''.join(char for char in running_key.upper() if char.isalpha())
    ciphertext = ciphertext.upper()
    
    # Check if key is long enough
    if len(key_stream) < sum(c.isalpha() for c in ciphertext):
        raise ValueError("Running key is too short for the ciphertext")
    
    key_index = 0
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
        
        # Convert to numbers (0-25)
        c = letter_to_number(ciphertext[i])
        k = letter_to_number(key_stream[key_index])
        
        # Decrypt: (c - k + 26) mod 26
        p = (c - k + 26) % 26
        
        plaintext += number_to_letter(p)
        key_index += 1
    
    return plaintext

if __name__ == "__main__":
    plaintext = "TORA TORA TORA"
    running_key = "AND GOD SAID LET THERE BE LIGHT"
    
    print("Running Key Vigenere Cipher")
    print("--------------------------")
    print(f"\nPlaintext: {plaintext}")
    print(f"Running Key: {running_key}")
    
    encrypted = running_key_vigenere_encrypt(plaintext, running_key)
    print(f"\nEncrypted: {encrypted}")
    
    decrypted = running_key_vigenere_decrypt(encrypted, running_key)
    print(f"Decrypted: {decrypted}")