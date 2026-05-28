import gmpy2
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def main():
    if len(sys.argv) != 6:
        print("Usage: python common_modulus_attack.py <c1> <c2> <e1> <e2> <n>")
        sys.exit(1)

    c1 = int(sys.argv[1])
    c2 = int(sys.argv[2])
    e1 = int(sys.argv[3])
    e2 = int(sys.argv[4])
    n = int(sys.argv[5])

    # Since e1 and e2 are coprime, we can find coefficients s1 and s2 such that
    # e1*s1 + e2*s2 = 1
    # Then m = c1^s1 * c2^s2 mod n
    s1 = modinv(e1, e2)
    s2 = (1 - e1 * s1) // e2

    # We need to handle negative exponents
    if s1 < 0:
        c1 = modinv(c1, n)
        s1 = -s1
    if s2 < 0:
        c2 = modinv(c2, n)
        s2 = -s2

    m1 = pow(c1, s1, n)
    m2 = pow(c2, s2, n)
    m = (m1 * m2) % n

    try:
        message_hex = hex(m)[2:]
        message_bytes = bytes.fromhex(message_hex)
        message_str = message_bytes.decode('utf-8')
        print(f"Attack successful! Message: {message_str}")
    except (ValueError, UnicodeDecodeError):
        print(f"Attack successful! Message (hex): {message_hex}")

if __name__ == "__main__":
    main()
