import random
from number_theory import prime_generation as pg, modular_arithmetic as ma

def generate_keypair(number_of_bits=1024):
    """
    Generate RSA public and private key pair.
    
    Returns:
        ((e, n), (d, n)): Public and private key pairs
    """
    p = pg.generate_prime_number(number_of_bits // 2)
    q = pg.generate_prime_number(number_of_bits // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    while ma.gcd(e, phi) != 1:
        e = random.randint(1, phi)
    
    d = ma.multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    """
    Encrypt a message using the public key.
    
    Args:
        message (int): Message to encrypt
        public_key ((int, int)): Public key
    
    Returns:
        int: Encrypted message
    """
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    """
    Decrypt a message using the private key.
    
    Args:
        ciphertext (int): Encrypted message
        private_key ((int, int)): Private key
    
    Returns:
        int: Decrypted message
    """
    d, n = private_key
    return pow(ciphertext, d, n)
