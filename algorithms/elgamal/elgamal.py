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
    
    return ((p, alpha, beta), (p, alpha, a))

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
    p, _, a = private_key
    y1, y2 = ciphertext
    inverse = ma.multiplicative_inverse(pow(y1, a, p), p)
    return (y2 * inverse) % p

def sign(message, private_key):
    """
    Sign a message using the private key.
    
    Args:
        message (int): Message to sign
        private_key ((int, int)): Private key
        
    Returns:
        (int, int): Signature
    """
    p, alpha, a = private_key

    k = random.randint(1, p - 2)
    while ma.gcd(k, p - 1) != 1:
        k = random.randint(1, p - 2)
    
    gamma = pow(alpha, k, p)
    inverse_k = ma.multiplicative_inverse(k, p - 1)
    # A hash function should be used instead of the message
    nabla = (message - a * gamma) * inverse_k % (p - 1)
    return gamma, nabla

def verify(message, signature, public_key):
    """
    Verify a signature using the public key.
    
    Args:
        message (int): Message to verify
        signature ((int, int)): Signature
        public_key ((int, int, int)): Public key
        
    Returns:
        bool: True if the signature is valid, False otherwise
    """
    p, alpha, beta = public_key
    gamma, nabla = signature
    return (pow(beta, gamma, p) * pow(gamma, nabla, p)) % p == pow(alpha, message, p)
