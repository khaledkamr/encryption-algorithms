def gcd(m, key):
    while key:
        m, key = key, m % key
    return m

def mod_inverse(m, mod):
    if gcd(m, mod) != 1:
        return None  # Modular inverse doesn't exist
    
    for x in range(1, mod):
        if (m * x) % mod == 1:
            return x
    return None

def affine_encrypt(plaintext, m, key):
    if gcd(m, 26) != 1:
        return "Error: 'm' must be coprime with 26"
    
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine ASCII offset based on case
            ascii_offset = 65 if char.isupper() else 97
            # Convert to 0-25 range
            x = ord(char) - ascii_offset
            # Apply affine transformation and convert back to ASCII
            encrypted = (m * x + key) % 26 + ascii_offset
            ciphertext += chr(encrypted)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, m, key):
    m_inverse = mod_inverse(m, 26)
    if m_inverse is None:
        return "Error: 'm' must be coprime with 26"
    
    print(f"m_inverse: {m_inverse}")
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine ASCII offset based on case
            ascii_offset = 65 if char.isupper() else 97
            # Convert to 0-25 range
            y = ord(char) - ascii_offset
            # Apply inverse affine transformation and convert back to ASCII
            decrypted = (m_inverse * (y - key)) % 26 + ascii_offset
            plaintext += chr(decrypted)
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    message = "war lost"
    key = 10
    m = 7  # Must be coprime with 26 (gcd(m,26)=1)
    
    encrypted = affine_encrypt(message, m, key)
    print(f"Original message: {message}")
    print(f"Key: (m={m}, key={key})")
    print(f"Encrypted: {encrypted}")
    
    decrypted = affine_decrypt(encrypted, m, key)
    print(f"Decrypted: {decrypted}")
   