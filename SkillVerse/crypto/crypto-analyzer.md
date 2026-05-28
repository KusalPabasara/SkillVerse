---
name: crypto-analyzer
description: "Analyzes cryptography CTF challenges to identify the primitives in use and suggest a course of action."
version: 1.0.0
author: Hermes Agent & KusalPabasara
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Cryptography, CTF, Hacking, Security, Analysis]
    related_skills: [ctf-crypto]
---

# Crypto Analyzer Skill

This skill is the entry point for the `ctf-crypto` master skill. It analyzes the provided information and determines the best course of action.

## When to Use

This skill is not meant to be used directly by the user. It is invoked by the `ctf-crypto` master skill.

## Core Logic

1.  **Input Parsing:** The skill takes the challenge description, ciphertext, and any other artifacts as input.
2.  **Keyword Analysis:** It searches for keywords in the challenge description that might indicate the type of crypto being used (e.g., "RSA," "AES," "ECC," "LFSR").
3.  **Artifact Analysis:** It analyzes any provided artifacts:
    *   **Public Keys:** It will attempt to parse public keys (e.g., PEM, DER, JWK) and extract parameters like `n` and `e` for RSA.
    *   **Ciphertext:** It will perform frequency analysis on the ciphertext to help identify classic ciphers. It will also check for common encodings like Base64, Hex, and ASCII.
4.  **Tool Integration:** It uses tools like `hashid` to identify hashes.
5.  **Output:** The skill outputs a structured analysis, including:
    *   The suspected cryptographic primitive(s).
    *   The recommended sub-skill to use next.
    *   Any extracted parameters or relevant information.

## Example Invocation (by `ctf-crypto` master skill)

```python
from hermes_tools import terminal

def analyze_challenge(description, ciphertext, artifacts):
    # Keyword analysis
    if "RSA" in description:
        return {"primitive": "RSA", "recommendation": "rsa-attacks"}

    # Artifact analysis
    if ciphertext:
        # Check for hex encoding
        try:
            bytes.fromhex(ciphertext)
            return {"primitive": "Unknown", "encoding": "hex", "recommendation": "classic-ciphers"}
        except ValueError:
            pass

        # Check for base64 encoding
        try:
            import base64
            base64.b64decode(ciphertext)
            return {"primitive": "Unknown", "encoding": "base64", "recommendation": "classic-ciphers"}
        except:
            pass

    # ... and so on
```
