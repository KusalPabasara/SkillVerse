import gmpy2
import sys
from math import gcd

def pollards_p_minus_1(n, B=100000):
    """
    Performs Pollard's p-1 factorization on n.
    Returns a factor of n if found, otherwise None.
    """
    a = 2
    for i in range(2, B + 1):
        a = pow(a, i, n)
        d = gcd(a - 1, n)
        if 1 < d < n:
            return d
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python pollards_p_minus_1.py <n> [B]")
        sys.exit(1)

    n = int(sys.argv[1])
    B = int(sys.argv[2]) if len(sys.argv) > 2 else 100000


    factor = pollards_p_minus_1(n, B)

    if factor:
        print(f"Attack successful! Factor: {factor}")
        print(f"Other factor: {n // factor}")
    else:
        print(f"Attack failed. p-1 is likely not {B}-smooth.")

if __name__ == "__main__":
    main()
