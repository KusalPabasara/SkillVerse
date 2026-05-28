import gmpy2
import sys

def integer_nth_root(n, r):
    """
    Calculates the integer nth root of a number.
    Returns a tuple (root, perfect_root_boolean).
    """
    return gmpy2.iroot(n, r)

def main():
    if len(sys.argv) != 4:
        print("Usage: python small_e_attack.py <c> <e> <n>")
        sys.exit(1)

    c = int(sys.argv[1])
    e = int(sys.argv[2])
    n = int(sys.argv[3])

    m, perfect_root = integer_nth_root(c, e)

    if perfect_root:
        try:
            # The message might be in hex or ascii, so we try to decode both
            message_hex = hex(m)[2:]
            message_bytes = bytes.fromhex(message_hex)
            message_str = message_bytes.decode('utf-8')
            print(f"Attack successful! Message: {message_str}")
        except (ValueError, UnicodeDecodeError):
            print(f"Attack successful! Message (hex): {message_hex}")
    else:
        print("Attack failed. The message is likely padded or the attack is not applicable.")

if __name__ == "__main__":
    main()
