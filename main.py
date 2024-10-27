from algorithms.rsa.rsa import generate_keypair, encrypt, decrypt
from utils.utils import encode_message

if __name__ == "__main__":
    # Key generation
    public_key, private_key = generate_keypair(1024)
    print(f"Public key (e,n): {public_key}")
    print(f"Private key (d,n): {private_key}")
    
    # Message
    message = input('Enter message: ')
    encoded_message = encode_message(message)
    print(f"\nOriginal message: {encoded_message}")
    
    # Encryption
    encrypted = encrypt(encoded_message, public_key)
    print(f"Encrypted: {encrypted}")
    
    # Decryption
    decrypted = decrypt(encrypted, private_key)
    print(f"Decrypted: {decrypted}")
    
    # Check if message is successfully recovered
    print(f"Message successfully recovered: {encoded_message == decrypted}")
