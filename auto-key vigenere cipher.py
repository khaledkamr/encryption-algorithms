# Auto-Key Vigenere Cipher Implementation

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def auto_key_vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper()
    
    # Track the auto-key (starts with the provided key)
    auto_key = key
    
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
        
        # If we need more key material, add plaintext characters
        if i >= len(auto_key):
            # Find the first plaintext character that wasn't used as key yet
            auto_key += plaintext[i - len(key)]
        
        p = letter_to_number(plaintext[i])
        k = letter_to_number(auto_key[i])
        c = (p + k) % 26
        
        ciphertext += number_to_letter(c)
    
    return ciphertext

def auto_key_vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    
    # Begin with the provided key
    auto_key = key
    
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
        
        # If we need more key material, use recovered plaintext
        if i >= len(auto_key) and i - len(key) < len(plaintext):
            auto_key += plaintext[i - len(key)]
            
        c = letter_to_number(ciphertext[i])
        k = letter_to_number(auto_key[i])
        p = (c - k + 26) % 26
        
        plaintext += number_to_letter(p)
    
    return plaintext

if __name__ == "__main__":
    plaintext = "VIGENERECIPHER"
    key = "LIGHTSPEEDCHEWIENOW"
    
    print("Auto-Key Vigenere Cipher")
    print("----------------------")
    print(f"\nPlaintext: {plaintext}")
    print(f"Initial Key: {key}")
    
    encrypted = auto_key_vigenere_encrypt(plaintext, key)
    print(f"\nEncrypted: {encrypted}")
    
    decrypted = auto_key_vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")