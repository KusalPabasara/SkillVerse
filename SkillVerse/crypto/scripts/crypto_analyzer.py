import sys
import json
from Crypto.PublicKey import RSA

def analyze_rsa(public_key_pem):
    """
    Analyzes an RSA public key and suggests possible attacks.
    """
    key = RSA.import_key(public_key_pem)
    n = key.n
    e = key.e

    suggestions = []

    # Check for small e
    if e in [3, 5, 17]:
        suggestions.append({
            "attack": "small_e",
            "description": f"The public exponent e={e} is small. If the message is not padded, the 'small_e' attack may work."
        })

    # Suggestions for other attacks would be added here
    # For now, we'll just focus on small e

    return {
        "n": str(n),
        "e": str(e),
        "suggestions": suggestions
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python crypto_analyzer.py <public_key_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        public_key_pem = f.read()

    analysis = analyze_rsa(public_key_pem)
    print(json.dumps(analysis, indent=4))

if __name__ == "__main__":
    main()
