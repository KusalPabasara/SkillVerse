import sys
from sympy import *

def continued_fractions(n, d):
    """
    Returns the continued fraction representation of n/d.
    """
    cf = []
    while d:
        q = n // d
        cf.append(q)
        n, d = d, n % d
    return cf

def convergents(cf):
    """
    Returns the convergents of a continued fraction.
    """
    convs = []
    n0, d0 = 0, 1
    n1, d1 = 1, 0
    for q in cf:
        n = q * n1 + n0
        d = q * d1 + d0
        convs.append((n, d))
        n0, d0 = n1, d1
        n1, d1 = n, d
    return convs

def wiener_attack(e, n):
    """
    Performs Wiener's attack on an RSA public key.
    Returns the private exponent d if found, otherwise None.
    """
    cf = continued_fractions(e, n)
    convs = convergents(cf)

    for k, d in convs:
        if k == 0:
            continue

        # Check if (e*d - 1) is a multiple of k
        if (e * d - 1) % k != 0:
            continue

        phi = (e * d - 1) // k
        # Check if x^2 - (n - phi + 1)x + n = 0 has integer roots
        # The roots are p and q
        b = n - phi + 1
        delta = b * b - 4 * n
        if delta >= 0:
            x1 = (b + isqrt(delta)) / 2
            x2 = (b - isqrt(delta)) / 2
            if x1 * x2 == n:
                return d
    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python wieners_attack.py <e> <n>")
        sys.exit(1)

    e = int(sys.argv[1])
    n = int(sys.argv[2])

    d = wiener_attack(e, n)

    if d:
        print(f"Attack successful! Private exponent d: {d}")
    else:
        print("Attack failed. The private exponent is likely not small enough.")

if __name__ == "__main__":
    main()
