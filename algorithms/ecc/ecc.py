import random
from number_theory import modular_arithmetic as ma

def elliptic_func(x, a, b, p):
    return (pow(x, 3, p) + a * x + b) % p

def cipolla(n, p):
    if n == 0:
        return 0, 0
    
    if not ma.is_quadratic_residue(n, p):
        return None, None
        
    a = 0
    while True:
        a = random.randrange(p)
        w = (a * a - n) % p
        if not ma.is_quadratic_residue(w, p):
            break
            
    def multiply(x1, y1, x2, y2, w):
        return ((x1 * x2 + y1 * y2 * w) % p,
                (x1 * y2 + y1 * x2) % p)
    
    def power(x, y, n, w):
        result = (1, 0)
        power = (x, y)
        while n:
            if n & 1:
                result = multiply(result[0], result[1], power[0], power[1], w)
            power = multiply(power[0], power[1], power[0], power[1], w)
            n >>= 1
        return result
    
    r = power(a, 1, (p + 1) // 2, w)[0]
    if (r * r) % p == n:
        return r, p - r
    return None, None

def point_add(P1, P2, curve):
    """Add two points on the curve y^2 = x^3 + ax + b mod p"""
    if P1 is None:
        return P2
    if P2 is None:
        return P1
        
    a, _, p = curve
    x1, y1 = P1
    x2, y2 = P2
    
    if x1 == x2:
        if (y1 + y2) % p == 0:
            return None  # Point at infinity
        # Point doubling
        if y1 == 0:
            return None
        # λ = (3x₁² + a) / (2y₁)
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        # Point addition
        # λ = (y₂ - y₁) / (x₂ - x₁)
        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    
    # x₃ = λ² - x₁ - x₂
    x3 = (lam * lam - x1 - x2) % p
    # y₃ = λ(x₁ - x₃) - y₁
    y3 = (lam * (x1 - x3) - y1) % p
    
    return x3, y3

def scalar_multiply(k, P, curve):
    """Multiply a point by a scalar using double-and-add method"""
    if k == 0 or P is None:
        return None
    
    p = curve[2]
    k = k % p  # Reduce k modulo p
    result = None
    addend = P
    
    while k:
        if k & 1:
            result = point_add(result, addend, curve)
        addend = point_add(addend, addend, curve)
        k >>= 1
    
    return result

def point_neg(P, curve):
    """Return the negative of a point"""
    p = curve[2]
    if P is None:
        return None
    x, y = P
    return x, (-y) % p

def is_on_curve(point, curve):
    """Check if a point lies on the curve"""
    if point is None:
        return True
    a, b, p = curve
    x, y = point
    return (y ** 2) % p == elliptic_func(x, a, b, p)

def generate_keypair(P, curve):
    """Generate private and public key pair"""
    # s = random.randrange(1, curve[2] - 1)
    s = 947
    B = scalar_multiply(s, P, curve)
    
    return (s, curve), (P, B, curve)

def encrypt(M, public_key):
    """
    ECC encryption
    """
    P, B, curve = public_key
    
    if not is_on_curve(M, curve):
        raise ValueError("Message point must lie on the curve")
    
    if not (is_on_curve(P, curve) and is_on_curve(B, curve)):
        raise ValueError(f"Public points must lie on the curve.\nP on curve? {is_on_curve(P, curve)}\nB on curve? {is_on_curve(B, curve)}")
    
    # Generate random k
    # k = random.randint(1, p - 1)
    k = 97742
    
    M1 = scalar_multiply(k, P, curve)
    kB = scalar_multiply(k, B, curve)
    M2 = point_add(M, kB, curve)
    
    return M1, M2

def decrypt(ciphertext, private_key):
    """
    ECC decryption
    """
    M1, M2 = ciphertext
    s, curve = private_key
    
    if not is_on_curve(M1, curve) or not is_on_curve(M2, curve):
        raise ValueError("Ciphertext points must lie on the curve")
    
    # M = M2 -sM1
    neg_sM1 = point_neg(scalar_multiply(s, M1, curve), curve)
    M = point_add(M2, neg_sM1, curve)
    return M


