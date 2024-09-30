import random

def find_k(n):
    """
    Finds k such that n - 1 = 2^k * m, where m is odd
    """
    n1 = n + 1
    k = 0
    while n1 % 2 == 0:
        k += 1
        n1 /= 2
    return k

def is_composite(n):
    k = find_k(n)
    m = (n + 1) / pow(2, k)
    a = random.randint(1, n - 1)
    b = pow(a, m, n)
    if b % n == 1:
        return False
    for i in range(k):
        # Checking if b is congruent to -1 modulo n
        if b % n == n - 1:
            return False
        else:
            b = pow(b, 2, n)
    return True