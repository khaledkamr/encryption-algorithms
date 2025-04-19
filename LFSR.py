class LFSR:
    def __init__(self, seed, feedback_taps):
        self.state = seed
        self.feedback_taps = feedback_taps
        self.length = len(seed)
    
    def shift(self):
        # Calculate feedback bit (XOR of all tapped bits)
        feedback = '0' if self.state[self.feedback_taps[0]] == self.state[self.feedback_taps[1]] else '1'
        
        # Output bit is the rightmost bit
        output = self.state[-1]
        
        # Shift register and insert new feedback bit
        self.state = feedback + self.state[:-1]
        
        return output
    
def stream_cipher_encrypt(plaintext, seed, feedback_taps, transitions):
    plaintext_binary = bin(plaintext)[2:]
    
    # Initialize LFSR
    lfsr = LFSR(seed, feedback_taps)
    
    states = [seed]
    outputs = []
    
    print("\nLFSR Transitions:")
    print("T\tState\t\tOutput")
    print("------------------------------")
    print(f"0\t{seed}\t\t-")
    
    for i in range(transitions):
        output = lfsr.shift()
        outputs.append(output)
        states.append(lfsr.state)
        print(f"{i+1}\t{lfsr.state}\t\t{output}")
    
    # Generate keystream
    keystream = ''.join(outputs)
    
    # XOR plaintext with keystream
    ciphertext_binary = ""
    for i in range(len(plaintext_binary)):
        ciphertext_binary += '1' if plaintext_binary[i] != keystream[i] else '0'
    
    ciphertext = int(ciphertext_binary, 2)
    
    print(f"\nPlaintext:  {plaintext_binary}")
    print(f"Keystream:  {keystream}")
    print(f"Ciphertext: {ciphertext_binary} ({ciphertext})")
    
    return ciphertext

def main():
    # Example from lecture slides
    print("LFSR STREAM CIPHER EXAMPLE")
    print("==========================")
    
    seed = "1110"
    
    # For b4 = b2 ⊕ b0, we need taps at positions [1, 3]
    # Note: we're using 0-indexed positions, so b0 is at index 3, b2 at index 1
    feedback_taps = [1, 3]
    
    plaintext = 183
    transitions = 8
    
    print(f"\nEncrypting {plaintext} with LFSR (seed={seed}, b4=b2⊕b0) after {transitions} transitions")
    
    ciphertext = stream_cipher_encrypt(plaintext, seed, feedback_taps, transitions)
    
    print("\n--- VERIFICATION ---")
    print(f"Original: {plaintext}")
    print(f"Encrypted: {ciphertext}")

if __name__ == "__main__":
    main()