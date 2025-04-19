def s_box_lookup(input_bits):
    s_box = {
        "000": "00", 
        "001": "01", 
        "010": "00", 
        "011": "10", 
        "100": "01", 
        "101": "00", 
        "110": "11", 
        "111": "10", 
    }
    return s_box[input_bits]

def xor_bits(bits1, bits2):
    result = ""
    for i in range(len(bits1)):
        result += "1" if bits1[i] != bits2[i] else "0"
    return result

def encrypt_block(block, key):
    x1, x2, x3, x4 = block[0], block[1], block[2], block[3]
    k1, k2, k3 = key[0], key[1], key[2]
    
    # Calculate t1 t2 = S(x3 x4 x3 ⊕ k1 k2 k3)
    s_box_input = xor_bits(x3 + x4 + x3, k1 + k2 + k3)
    t1_t2 = s_box_lookup(s_box_input)
    
    # Calculate u1 u2 = x1 x2 ⊕ t1 t2
    u1_u2 = xor_bits(x1 + x2, t1_t2)
    
    # Final output: E(x1 x2 x3 x4, k1 k2 k3) = x3 x4 u1 u2
    encrypted_block = x3 + x4 + u1_u2
    
    return encrypted_block

def encrypt_word(word, key):
    encrypted_ascii = []
    
    for char in word:
        binary = format(ord(char), '08b')  # Convert character to 8-bit binary
        
        # Process first 4 bits
        first_block = binary[:4]
        encrypted_first = encrypt_block(first_block, key)
        
        # Process second 4 bits
        second_block = binary[4:]
        encrypted_second = encrypt_block(second_block, key)
        
        # Combine the two encrypted blocks
        encrypted_byte = encrypted_first + encrypted_second
        encrypted_ascii.append(int(encrypted_byte, 2))
    
    return encrypted_ascii

def main():
    # The example from the slides: encrypt "hope" with key "011"
    plaintext = "hope"
    key = "011"
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    encrypted_ascii = encrypt_word(plaintext, key)
    print(f"Encrypted ASCII values: {encrypted_ascii}")
    

if __name__ == "__main__":
    main()