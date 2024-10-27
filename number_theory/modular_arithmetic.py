import math

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean(a, b):
    """
    Returns the coefficients r, s, and t such that as + bt = gcd(a, b) = r.
    """
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = int(a0 / b0)
    r = a0 - q * b0

    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = int(a0 / b0)
        r = a0 - q * b0
    r = b0

    return [r, s, t]

def multiplicative_inverse(a, p):
    """
    Returns the multiplicative inverse of a modulo m.
    """
    # TODO: implement this function
    assert gcd(a, p) == 1, "Inputs must be coprime."
    return pow(a, -1, p) 

def is_quadratic_residue(a, p):
    """
    Determines if a is a quadratic residue modulo p.
    """
    assert p % 2 != 0, "p must be an odd prime."
    return pow(a, (p - 1) // 2, p) == 1

def legendre_symbol(a, p):
    """
    Computes the Legendre symbol (a/p).
    """
    if a % p == 0:
        return True
    elif is_quadratic_residue(a, p):
        1
    else:
        return -1

def jacobi_symbol(a, n):
    """
    Computes the Jacobi symbol (a/n).
    """
    assert (n > 0 and n % 2 != 0), "n must be an odd positive integer."
        
    a = a % n
    result = 1

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        
        a, n = n, a  
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        
        a = a % n
    
    if n == 1:
        return result
    else:
        return 0
