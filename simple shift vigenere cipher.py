def simple_shift_vigenere_encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.upper()
    
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
            
        # Convert letter to number (0-25)
        p = ord(plaintext[i]) - ord('A')
        # Get shift value from key (cycling through key array)
        k = key[i % len(key)]
        
        # Encrypt: (p + k) mod 26
        c = (p + k) % 26
        
        ciphertext += chr((c % 26) + ord('A'))
    
    return ciphertext

def simple_shift_vigenere_decrypt(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.upper()
    
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
            
        # Convert letter to number (0-25)
        c = ord(ciphertext[i]) - ord('A')
        # Get shift value from key (cycling through key array)
        k = key[i % len(key)]
        
        # Decrypt: (c - k + 26) mod 26
        p = (c - k + 26) % 26
        
        plaintext += chr((p % 26) + ord('A'))
    
    return plaintext

if __name__ == "__main__":
    plaintext = "VIGENERECIPHER"
    key = [5, 13, 2, 7]  
    
    print("Simple Shift Vigenere Cipher (Numeric Key)")
    print("----------------------------------------")
    print(f"\nPlaintext: {plaintext}")
    print(f"Key: {key}")
    
    encrypted = simple_shift_vigenere_encrypt(plaintext, key)
    print(f"\nEncrypted: {encrypted}")
    
    decrypted = simple_shift_vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")