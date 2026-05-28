import gmpy2
import sys
from functools import reduce

def chinese_remainder_theorem(items):
    """
    Solves the Chinese Remainder Theorem for a system of congruences.
    `items` is a list of tuples (n_i, a_i), where x = a_i (mod n_i).
    """
    N = reduce(lambda x, y: x * y, (item[0] for item in items))
    result = 0
    for n_i, a_i in items:
        p = N // n_i
        result += a_i * gmpy2.invert(p, n_i) * p
    return result % N

def main():
    if len(sys.argv) < 3 or len(sys.argv) % 2 != 1:
        print("Usage: python hastads_broadcast_attack.py <n1> <c1> <n2> <c2> ...")
        sys.exit(1)

    items = []
    for i in range(1, len(sys.argv), 2):
        n = int(sys.argv[i])
        c = int(sys.argv[i+1])
        items.append((n, c))
    
    # Assuming e=3, which is common in these challenges
    e = len(items)
    
    c = chinese_remainder_theorem(items)
    
    m, perfect_root = gmpy2.iroot(c, e)
    
    if perfect_root:
        try:
            message_hex = hex(m)[2:]
            message_bytes = bytes.fromhex(message_hex)
            message_str = message_bytes.decode('utf-8')
            print(f"Attack successful! Message: {message_str}")
        except (ValueError, UnicodeDecodeError):
            print(f"Attack successful! Message (hex): {message_hex}")
    else:
        print("Attack failed. The message is likely padded or the assumptions are incorrect.")


if __name__ == "__main__":
    main()
