import sys
import json
from Crypto.PublicKey import RSA

def analyze_challenge(challenge_text, artifacts):
    """
    Analyzes a CTF challenge to suggest the next steps.
    `artifacts` is a dictionary that can contain 'public_key_file', 'ciphertext_file', etc.
    """
    analysis = {"suggestions": []}

    # Analyze public key if provided
    if artifacts.get('public_key_file'):
        try:
            with open(artifacts['public_key_file'], 'r') as f:
                public_key_pem = f.read()
            key = RSA.import_key(public_key_pem)
            n = key.n
            e = key.e
            analysis['rsa_params'] = {'n': str(n), 'e': str(e)}

            if e in [3, 5, 17]:
                analysis['suggestions'].append({
                    "attack": "rsa_small_e",
                    "description": f"The public exponent e={e} is small. If the message is not padded, the 'small_e' attack may work."
                })
        except Exception as e:
            analysis['errors'] = [f"Failed to parse RSA key: {str(e)}"]

    # Analyze ciphertext if provided
    if artifacts.get('ciphertext_file'):
        try:
            with open(artifacts['ciphertext_file'], 'r') as f:
                ciphertext = f.read().strip()
            analysis['ciphertext_preview'] = ciphertext[:100]

            # Check for Caesar cipher characteristics
            if all(c.isalpha() or c.isspace() for c in ciphertext):
                 analysis['suggestions'].append({
                    "attack": "caesar_cipher",
                    "description": "Ciphertext contains only letters and spaces, suggesting a simple substitution cipher like Caesar."
                })
        except Exception as e:
            analysis['errors'] = [f"Failed to read or analyze ciphertext: {str(e)}"]


    return analysis

def main():
    # This script is intended to be called by other skills,
    # but we can provide a simple command-line interface for testing.
    if len(sys.argv) < 2:
        print("Usage: python crypto_analyzer.py <challenge_description> --public_key <file> --ciphertext <file>")
        sys.exit(1)

    description = sys.argv[1]
    artifacts = {}
    if '--public_key' in sys.argv:
        artifacts['public_key_file'] = sys.argv[sys.argv.index('--public_key') + 1]
    if '--ciphertext' in sys.argv:
        artifacts['ciphertext_file'] = sys.argv[sys.argv.index('--ciphertext') + 1]

    result = analyze_challenge(description, artifacts)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
