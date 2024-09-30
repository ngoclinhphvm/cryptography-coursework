import math

def square_and_multiply_always(base, exp, mod):
    """
    Returns the residue of base^exp modulo mod. 

    Parameters
    ----------
    base : int
        The base number.
    exp : int
        The exponent.
    mod : int
        The modulus.

    Returns
    -------
    int
        The result of (base^exp) % mod.
    """
    R0=1
    R1 = base
    c = '{0:b}'.format(exp)
    i=len(c)-1
    t=0
    c=c[::-1]
    while(i>=0):
        if(t==0):
            Rt=R0
        elif(t==1):
            Rt=R1
        else:
            print("t != 0 or 1")
        R0=(R0*Rt)%mod
        d=int(c[i])
        t=(t^d)
        i=i-1+t
    return R0

def dumb_is_prime(n):
    if 1 < n and n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def dumb_prime_factors(n):
    """
    Returns the prime factors of a positive integer n.
    """
    factors = []
    divisor = 2
    while n != 1:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor  
        divisor += 1
    return factors

def multiplicative_group(n):
    """
    Returns a group of integers that are smaller than and coprime to n, including 1.
    This group is known as the multiplicative group modulo n or the group of units modulo n.
    """
    group = []
    for num in range(1, n):
        if math.gcd(num, n) == 1:
            group.append(num)
    return group

def is_primitive_element(a, p):
    """
    Returns if a is a primitive element modulo p
    """
    if math.gcd(a, p) != 1:
        return False
    p1 = p - 1
    prime_factors = dumb_prime_factors(p1)
    for q in prime_factors:
        if pow(a, p1 // q, p) == 1:
            return False
    return True

def extended_euclidean(a, b):
    """
    Returns the coefficients r, s, and t such that as + bt = gcd(a, b) = r.

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    dict
        A dictionary containing the coefficients 'r', 's', and 't'.
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

    return {'r' : r, 's' : s, 't' : t}

def multiplicative_inverse(a, b):
    """
    Returns the multiplicative inverse of b modulo a.

    Parameters
    ----------
    a : int
        The modulus.
    b : int
        The number to find an inverse.

    Returns
    -------
    int
        The multiplicative inverse of b modulo a.

    Raises
    ------
    AssertionError
        If a and b are not coprime, i.e., b does not have a multiplicative inverse modulo a.
    """
    assert math.gcd(a, b) == 1, "Inputs must be coprime."

    a0 = a
    b0 = b
    t0 = 0
    t = 1
    q = int(a0 / b0)
    r = a0 - q * b0

    while r > 0:
        temp = (t0 - q * t) % a
        t0 = t
        t = temp
        a0 = b0
        b0 = r
        q = int(a0 / b0)
        r = a0 - q * b0
    
    return t