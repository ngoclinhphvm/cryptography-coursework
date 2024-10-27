import random
from number_theory import prime_generation as pg, modular_arithmetic as ma

def generate_keypair(number_of_bits=64):
    """
    Generate ElGamal public and private key pair.
    
    Returns:
        ((p, alpha, beta), (p, a)): Public and private key pairs
    """
    p = pg.generate_prime_number(number_of_bits)
    alpha = ma.smallest_primitive_element(p)
    a = random.randint(1, p - 2)
    beta = pow(alpha, a, p)
    
    return ((p, alpha, beta), (p, a))

def encrypt(message, public_key):
    """
    Encrypt a message using the public key.
    
    Args:
        message (int): Message to encrypt
        public_key ((int, int, int)): Public key
        
    Returns:
        ((int, int)): Encrypted message
    """
    p, alpha, beta = public_key
    k = random.randint(1, p - 2)
    while ma.gcd(k, p - 1) != 1:
        k = random.randint(1, p - 2)

    y1 = pow(alpha, k, p)
    y2 = (message * pow(beta, k, p)) % p
    
    return (y1, y2)

def decrypt(ciphertext, private_key):
    """
    Decrypt a message using the private key.
    
    Args:
        ciphertext ((int, int)): Encrypted message
        private_key ((int, int)): Private key
        
    Returns:
        int: Decrypted message
    """
    p, a = private_key
    y1, y2 = ciphertext
    inverse = ma.multiplicative_inverse(pow(y1, a, p), p)
    return (y2 * inverse) % p

