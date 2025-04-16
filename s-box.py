s_box = {
    (0, 0, 0): (1, 1),
    (0, 0, 1): (0, 1),
    (0, 1, 0): (0, 0),
    (0, 1, 1): (1, 0),
    (1, 0, 0): (0, 1),
    (1, 0, 1): (0, 0),
    (1, 1, 0): (1, 1),
    (1, 1, 1): (1, 0)
}

def text_to_binary(text):
    """Convert text to binary string using ASCII values."""
    binary = ""
    for char in text:
        ascii_val = ord(char)
        bin_str = format(ascii_val, '08b')
        binary += bin_str
    return binary

def xor_bits(bits1, bits2):
    """Perform XOR on two lists of bits."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox_lookup(input_bits):
    """Look up the S-box output for a 3-bit input."""
    return list(s_box[tuple(input_bits)])

def encrypt_block(plaintext_bits, key_bits):
    """Encrypt a 4-bit plaintext block with a 3-bit key."""
    x1, x2, x3, x4 = plaintext_bits
    k1, k2, k3 = key_bits
    
    input_xor = xor_bits([x3, x4, x3], [k1, k2, k3])
    t1, t2 = sbox_lookup(input_xor)
    
    u1, u2 = xor_bits([x1, x2], [t1, t2]) 
    
    return [x3, x4, u1, u2]

def encrypt_text(plaintext, key):
    """Encrypt plaintext using the S-box algorithm."""
    binary_text = text_to_binary(plaintext)
    key_bits = [int(b) for b in format(int(key, 2), '03b')]
    
    ciphertext = []
    for i in range(0, len(binary_text), 4):
        block = [int(b) for b in binary_text[i:i+4]]
        while len(block) < 4:
            block.append(0)
        encrypted_block = encrypt_block(block, key_bits)
        ciphertext.extend(encrypted_block)
    
    return ''.join(str(b) for b in ciphertext)

def binary_to_ascii_numbers(binary_str):
    """Convert binary string to ASCII decimal numbers."""
    ascii_numbers = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) < 8:
            byte = byte + '0' * (8 - len(byte))
        ascii_val = int(byte, 2)
        ascii_numbers.append(str(ascii_val))
    return ', '.join(ascii_numbers)

def main():
    plaintext = "hope"
    key = "011"
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    ciphertext = encrypt_text(plaintext, key)
    print(f"Ciphertext (binary): {ciphertext}")
    
    ascii_output = binary_to_ascii_numbers(ciphertext)
    print(f"Ciphertext (ASCII): {ascii_output}")

if __name__ == "__main__":
    main()