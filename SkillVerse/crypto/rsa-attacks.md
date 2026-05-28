---
name: rsa-attacks
description: "A suite of automated attacks against the RSA cryptosystem."
version: 1.0.0
author: Hermes Agent & KusalPabasara
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Cryptography, CTF, Hacking, Security, RSA]
    related_skills: [ctf-crypto, crypto-analyzer]
---

# RSA Attacks Skill

This skill provides a collection of automated attacks against the RSA cryptosystem. It is designed to be invoked by the `ctf-crypto` master skill.

## When to Use

This skill is not meant to be used directly by the user. It is invoked by the `ctf-crypto` master skill when an RSA challenge is identified.

## Attacks

This skill will eventually contain a variety of attacks, including:

-   **Small e (Cube Root) Attack:** For when `e` is small (e.g., 3) and the message is not padded.
-   **Common Modulus Attack:** When two different public keys share the same modulus `n`.
-   **Wiener's Attack:** For when the private exponent `d` is small.
-   **Fermat's Factorization Attack:** For when the prime factors `p` and `q` are close to each other.
-   **Pollard's p-1 Attack:** For when `p-1` is a smooth number.
-   **Hastad's Broadcast Attack:** For when the same message is encrypted with different public keys and a small `e`.

## Scripts

The attacks are implemented as Python scripts in the `scripts` directory. The main skill will orchestrate the execution of these scripts based on the parameters of the challenge.
