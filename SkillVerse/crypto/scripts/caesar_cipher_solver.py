import sys
from collections import Counter

def caesar_cipher_solver(ciphertext):
    """
    Solves a Caesar cipher by trying all possible shifts.
    Returns a dictionary of possible decryptions and a best guess.
    """
    # English letter frequency, from most to least common
    english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    
    results = {}
    for shift in range(26):
        plaintext = ''
        for char in ciphertext:
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                plaintext += shifted_char
            elif 'A' <= char <= 'Z':
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                plaintext += shifted_char
            else:
                plaintext += char
        results[shift] = plaintext

    # Find the best guess by comparing letter frequencies
    best_guess_shift = -1
    highest_score = -1
    for shift, plaintext in results.items():
        # Get the frequency of letters in the plaintext
        plaintext_freq = Counter(c.upper() for c in plaintext if 'a' <= c.lower() <= 'z').most_common()
        
        # Give a score based on the frequency of the most common letters
        score = 0
        for i, (char, count) in enumerate(plaintext_freq):
            if char in english_freq:
                # Higher score for more common letters in the correct position
                score += english_freq.index(char)
        
        if score > highest_score:
            highest_score = score
            best_guess_shift = shift

    return {
        "all_possibilities": results,
        "best_guess": results[best_guess_shift],
        "best_guess_shift": best_guess_shift
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher_solver.py <ciphertext>")
        sys.exit(1)

    ciphertext = sys.argv[1]
    solution = caesar_cipher_solver(ciphertext)
    
    print("All possibilities:")
    for shift, plaintext in solution["all_possibilities"].items():
        print(f"Shift {shift}: {plaintext}")
    
    print("\\nBest guess (shift " + str(solution['best_guess_shift']) + "): " + solution['best_guess'])

if __name__ == "__main__":
    main()
