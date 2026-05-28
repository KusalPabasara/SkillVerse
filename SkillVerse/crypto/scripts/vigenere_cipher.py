import sys
from collections import Counter

def vigenere_cipher(text, key, decrypt=False):
    """
    Encrypts or decrypts a text using the Vigenere cipher.
    """
    key_len = len(key)
    key_ints = [ord(k.upper()) - ord('A') for k in key]
    output = ''
    key_index = 0
    for char in text:
        if 'a' <= char <= 'z':
            shift = key_ints[key_index % key_len]
            if decrypt:
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            output += shifted_char
            key_index += 1
        elif 'A' <= char <= 'Z':
            shift = key_ints[key_index % key_len]
            if decrypt:
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            output += shifted_char
            key_index += 1
        else:
            output += char
    return output

def main():
    if len(sys.argv) < 4:
        print("Usage: python vigenere_cipher.py <encrypt/decrypt> <key> <text>")
        sys.exit(1)

    action = sys.argv[1]
    key = sys.argv[2]
    text = sys.argv[3]

    if action.lower() == 'encrypt':
        result = vigenere_cipher(text, key)
        print(f"Encrypted text: {result}")
    elif action.lower() == 'decrypt':
        result = vigenere_cipher(text, key, decrypt=True)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
