def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine ASCII offset based on case (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            
            shifted = ((ord(char) - ascii_offset + shift) % 26) + ascii_offset
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    
    # Decryption is just encryption with the negative shift
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    message = "the word privacy does not appear in the united states constitution"
    key = 3
    
    encrypted = caesar_encrypt(message, key)
    decrypted = caesar_decrypt(encrypted, key)

    print(f"Caesar Cipher Example")
    print(f"=====================")

    print(f"\nOriginal message: {message}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    
    print(f"Decrypted: {decrypted}")
    