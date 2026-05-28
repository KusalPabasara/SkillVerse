import sys

def atbash_cipher_solver(ciphertext):
    """
    Solves an Atbash cipher.
    """
    plaintext = ''
    for char in ciphertext:
        if 'a' <= char <= 'z':
            plaintext += chr(ord('z') - (ord(char) - ord('a')))
        elif 'A' <= char <= 'Z':
            plaintext += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            plaintext += char
    return plaintext

def main():
    if len(sys.argv) != 2:
        print("Usage: python atbash_cipher_solver.py <ciphertext>")
        sys.exit(1)

    ciphertext = sys.argv[1]
    plaintext = atbash_cipher_solver(ciphertext)
    
    print(f"Decrypted text: {plaintext}")

if __name__ == "__main__":
    main()
