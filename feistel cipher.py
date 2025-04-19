def xor_binary_strings(a, b):
    """XOR two binary strings of the same length"""
    result = ""
    for i in range(len(a)):
        result += "1" if a[i] != b[i] else "0"
    return result

def feistel_cipher_encrypt(plaintext, keys):
    binary = bin(plaintext)[2:]

    key_length = len(keys[0])
    required_length = 2 * key_length
    if len(binary) < required_length:
        binary = binary.zfill(required_length)
    
    # Split binary into left and right halves
    mid = len(binary) // 2
    L, R = binary[:mid], binary[mid:]
    
    # Three rounds of Feistel network
    for i, key in enumerate(keys):
        # Calculate F(R, K) = R XOR K
        f_result = xor_binary_strings(R, key)
        
        # New L = R
        # New R = L XOR F(R, K)
        new_L = R
        new_R = xor_binary_strings(L, f_result)
        
        L, R = new_L, new_R
    
    # Final ciphertext is the concatenation of L and R
    ciphertext_binary = L + R
    ciphertext = int(ciphertext_binary, 2)
    
    return ciphertext

def feistel_cipher_decrypt(ciphertext, keys):
    binary = bin(ciphertext)[2:]
    
    key_length = len(keys[0])
    required_length = 2 * key_length
    if len(binary) < required_length:
        binary = binary.zfill(required_length)
    
    
    # Split binary into left and right halves
    mid = len(binary) // 2
    L = binary[:mid]
    R = binary[mid:]
    
    # Three rounds of Feistel network (in reverse order)
    for i, key in enumerate(reversed(keys)):
        # Calculate F(L, K) = L XOR K
        f_result = xor_binary_strings(L, key)
        
        # New R = L
        # New L = R XOR F(L, K)
        new_R = L
        new_L = xor_binary_strings(R, f_result)
        
        L, R = new_L, new_R
    
    # Final plaintext is the concatenation of L and R
    plaintext_binary = L + R
    plaintext = int(plaintext_binary, 2)
    
    return plaintext

def main():
    plaintext = 425
    keys = ["00100", "10101", "10001"]
    
    print("FEISTEL CIPHER EXAMPLE")
    print("======================")
    
    print("\n--- ENCRYPTION ---")
    plaintext_binary = bin(plaintext)[2:]
    print(f"Plaintext: {plaintext} (binary: {plaintext_binary})")
    
    ciphertext = feistel_cipher_encrypt(plaintext, keys)
    ciphertext_binary = bin(ciphertext)[2:]
    print(f"Ciphertext: {ciphertext} (binary: {ciphertext_binary})")
    
    print("\n--- DECRYPTION ---")
    print(f"Ciphertext: {ciphertext} (binary: {ciphertext_binary})")
    
    decrypted = feistel_cipher_decrypt(ciphertext, keys)
    decrypted_binary = bin(decrypted)[2:]
    print(f"Plaintext: {decrypted} (binary: {decrypted_binary})")
    
    # Verify
    print("\n--- VERIFICATION ---")
    print(f"Decryption successful: {plaintext == decrypted}")

if __name__ == "__main__":
    main()