import sys
import os
import math
from utils import multiplicative_inverse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def binary_search(arr, target, low, high):
    """
    Performs binary search for Shanks algorithm.

    Parameters:
    arr (list): The list to search through.
    target (int): The value to search for.
    low (int): The lower index of the search range.
    high (int): The upper index of the search range.

    Returns:
    int: The index of the x if found, otherwise -1.
    """
    while low <= high:
        mid = low + (high - low)//2
        if target == arr[mid][1]:
            return mid
        elif target > arr[mid][1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def log(alpha, beta, n, p):
    """
    Calculates the discrete logarithm base alpha of beta modulo n.

    Parameters:
    alpha (int): The base of the logarithm.
    beta (int): The value whose logarithm is to be found.
    n (int): The modulus.
    p (int): A prime number.

    Returns:
    int: The discrete logarithm.
    """
    m = int(math.sqrt(n)) if math.sqrt(n) == int(math.sqrt(n)) else int(math.sqrt(n)) + 1

    pairs = []
    for j in range(m):
        ans = pow(alpha, m * j, p)
        pairs.append([j, ans])
    l1 = sorted(pairs, key=lambda x : x[1])

    pairs = []
    for i in range(m):
        inverse = multiplicative_inverse(p, pow(alpha, i, p))
        ans = (beta * inverse) % p
        pairs.append([i, ans])
    l2 = sorted(pairs, key=lambda x : x[1])

    for index_j in range(m):
        index_i = binary_search(l2, l1[index_j][1], 0, m - 1)
        if index_i != -1:
            j = l1[index_j][0]
            i = l2[index_i][0]
            a = (m * j + i) % n
            return a

