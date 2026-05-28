---
name: classic-ciphers
description: "A collection of solvers for classic ciphers."
version: 1.0.0
author: Hermes Agent & KusalPabasara
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Cryptography, CTF, Hacking, Security, Classic Ciphers]
    related_skills: [ctf-crypto, crypto-analyzer]
---

# Classic Ciphers Skill

This skill provides a collection of solvers for classic ciphers. It is designed to be invoked by the `ctf-crypto` master skill.

## When to Use

This skill is not meant to be used directly by the user. It is invoked by the `ctf-crypto` master skill when a classic cipher is identified.

## Ciphers

This skill will eventually contain solvers for a variety of classic ciphers, including:

-   **Caesar Cipher:** A simple substitution cipher where each letter is shifted by a certain number of places.
-   **Atbash Cipher:** A substitution cipher where the alphabet is reversed.
-   **Vigenere Cipher:** A polyalphabetic substitution cipher.
-   **ROT13 Cipher:** A special case of the Caesar cipher where the shift is 13.

## Scripts

The solvers are implemented as Python scripts in the `scripts` directory. The main skill will orchestrate the execution of these scripts based on the parameters of the challenge.
