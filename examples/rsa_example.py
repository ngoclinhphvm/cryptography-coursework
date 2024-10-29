from algorithms.rsa.rsa import generate_keypair, encrypt, decrypt, sign, verify

def main():    
    # Key generation
    public_key, private_key = generate_keypair(1024)
    print(f"Public key (e,n): {public_key}")
    print(f"Private key (d,n): {private_key}")

    # Message
    message = input('Enter message: ')
    encoded_message = int.from_bytes(message.encode('utf-8'), 'big')

    print(f"\nOriginal message: {encoded_message}")
    
    # Encryption
    encrypted = encrypt(encoded_message, public_key)
    print(f"Encrypted: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, private_key)
    print(f"Decrypted: {decrypted}")
    
    # Check if message is successfully recovered
    print(f"Message successfully recovered: {encoded_message == decrypted}")

    # Signing
    signature = sign(encoded_message, private_key)
    print(f"Signature: {signature}")

    # Verification
    verified = verify(encoded_message, signature, public_key)
    print(f"Signature verified: {verified}")

if __name__ == "__main__":
    main()