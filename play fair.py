def create_playfair_matrix(key):
    # Combine I and J in the same cell
    # Remove duplicate letters from the key
    key = key.upper().replace("J", "I")
    key_chars = []
    for char in key:
        if char.isalpha() and char not in key_chars:
            key_chars.append(char)
    
    # Add remaining alphabet characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
    
    # Create 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i+5])
    
    return matrix

def find_position(matrix, char):
    char = char.upper()
    if char == 'J':
        char = 'I'
    
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)
    return None

def playfair_encrypt(plaintext, key):
    print("\nEncryption step by step:")
    matrix = create_playfair_matrix(key)
    
    # Prepare plaintext: remove non-alphabetic chars, convert to uppercase
    plaintext = ''.join(char for char in plaintext.upper() if char.isalpha())
    plaintext = plaintext.replace("J", "I")
    
    # Split plaintext into digraphs (pairs of letters)
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i + 1 >= len(plaintext):
            # Add X if the last character is alone
            digraphs.append(plaintext[i] + 'X')
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            # If the two letters are the same, add X between them
            digraphs.append(plaintext[i] + 'X')
            i += 1
        else:
            # Regular case: take the two letters as a digraph
            digraphs.append(plaintext[i:i+2])
            i += 2
    
    print(f"Digraphs: {' '.join(digraphs)}")

    # Encrypt each digraph
    ciphertext = ""
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            print(f"Digraph {digraph} -> {ciphertext[-2:]} (same row)")
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            print(f"Digraph {digraph} -> {ciphertext[-2:]} (same column)")
        else:  # Rectangle case
            ciphertext += matrix[row2][col1] + matrix[row1][col2]
            print(f"Digraph {digraph} -> {ciphertext[-2:]} (rectangle)")
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    print("\nDecryption step by step:")
    matrix = create_playfair_matrix(key)
    
    # Prepare ciphertext
    ciphertext = ''.join(char for char in ciphertext.upper() if char.isalpha())
    
    # Split ciphertext into digraphs
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

    print(f"Digraphs: {' '.join(digraphs)}")
    
    # Decrypt each digraph
    plaintext = ""
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            print(f"Digraph {digraph} -> {plaintext[-2:]} (same row)")
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            print(f"Digraph {digraph} -> {plaintext[-2:]} (same column)")
        else:  # Rectangle case
            plaintext += matrix[row2][col1] + matrix[row1][col2]
            print(f"Digraph {digraph} -> {plaintext[-2:]} (rectangle)")
    
    return plaintext

def print_matrix(matrix):
    print("Playfair Matrix:")
    for row in matrix:
        print("  ".join(row))

if __name__ == "__main__":
    key = "THE PLAYFAIR CIPHER"
    plaintext = "AMBASSADOR SHOT"
    
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    
    matrix = create_playfair_matrix(key)
    print_matrix(matrix)
    
    encrypted = playfair_encrypt(plaintext, key)
    print(f"\nEncrypted: {encrypted}")
    
    decrypted = playfair_decrypt(encrypted, key)
    print(f"\nDecrypted: {decrypted}")
