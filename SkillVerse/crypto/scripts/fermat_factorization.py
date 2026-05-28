import gmpy2
import sys

def fermat_factorization(n, max_iter=1000000):
    """
    Performs Fermat's factorization on n.
    Returns the factors (p, q) if found, otherwise None.
    """
    a = gmpy2.isqrt(n)
    b2 = a * a - n
    i = 0
    while not gmpy2.is_square(b2):
        a += 1
        b2 = a * a - n
        i += 1
        if i > max_iter:
            return None, None
    b = gmpy2.isqrt(b2)
    p = a + b
    q = a - b
    return p, q

def main():
    if len(sys.argv) != 2:
        print("Usage: python fermat_factorization.py <n>")
        sys.exit(1)

    n = int(sys.argv[1])

    p, q = fermat_factorization(n)

    if p and q:
        print(f"Attack successful! Factors: p={p}, q={q}")
    else:
        print("Attack failed. The prime factors are likely not close enough.")

if __name__ == "__main__":
    main()
