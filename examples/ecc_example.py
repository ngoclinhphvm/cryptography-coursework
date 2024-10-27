from algorithms.ecc.ecc import generate_keypair, encrypt, decrypt, get_generator

def main():
    # Generate key pair
    print("Generating key pair...")
    public_key, private_key = generate_keypair(20)
    
    # Get curve parameters
    curve = public_key[1]
    
    # Find a point on the curve to use as message
    print("Finding message point...")
    generator = get_generator(curve)
    message = generator  # Use generator point as sample message
    
    print("\nOriginal message point:", message)
    
    # Encrypt message
    print("\nEncrypting...")
    ciphertext = encrypt(message, public_key)
    print("Encrypted points:", ciphertext)
    
    # Decrypt message
    print("\nDecrypting...")
    decrypted = decrypt(ciphertext, private_key)
    print("Decrypted point:", decrypted)
    
    # Verify
    print("\nVerification:")
    print("Decryption successful:", message == decrypted)

if __name__ == "__main__":
    main()