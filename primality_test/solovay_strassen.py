import random
from utils.utils import jacobi_symbol

def is_composite(n):
    """
    A yes-biased algorithm to check if a number is composite.
    """
    a = random.randint(1, n - 1)
    x = jacobi_symbol(a, n)
    if x == 0:
        return True
    y = pow(a, (n - 1) / 2, n)

    return (x % n) == (y % n)
