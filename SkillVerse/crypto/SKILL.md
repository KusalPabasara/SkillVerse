---
name: ctf-crypto
description: "Provides automated and interactive cryptography attack techniques for CTF challenges. This skill can analyze cryptographic primitives, suggest attacks, and execute them using a variety of tools and scripts."
version: 1.0.0
author: Hermes Agent & KusalPabasara
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Cryptography, CTF, Hacking, Security]
    related_skills: [ctf-pwn, ctf-web, ctf-forensics]
prerequisites:
  commands: [python3, pip, git, hashcat, sagemath]
---

# CTF Cryptography Skill

This skill provides a comprehensive toolkit for solving cryptography CTF challenges. It combines a vast knowledge base with automated attack scripts and interactive problem-solving capabilities.

## When to Use

- When you encounter a cryptography challenge in a CTF.
- When you need to identify a cipher, hash, or encoding.
- When you need to perform an attack on a cryptographic primitive.
- When you're stuck on a crypto challenge and need guidance.

## Core Capabilities

1.  **Cipher Identification:** Automatically identify common ciphers, encodings, and hashes.
2.  **Automated Attacks:** Execute a wide range of automated attacks against various cryptographic primitives.
3.  **Interactive Guidance:** Provide step-by-step guidance for complex attacks, asking for user input when necessary.
4.  **Tool Integration:** Seamlessly integrate with popular crypto tools like RsaCtfTool, hashcat, and SageMath.

## Getting Started

To begin, simply present the challenge description, ciphertext, and any other relevant information to the agent with this skill loaded. The agent will analyze the information and suggest a course of action.

## Sub-Skills

This master skill will invoke a series of sub-skills, each focused on a specific area of cryptography. These sub-skills are not meant to be used directly, but are orchestrated by this master skill.

-   **crypto-analyzer:** Analyzes the challenge to identify the cryptographic primitives in use.
-   **rsa-attacks:** A suite of automated attacks against RSA.
-   **classic-ciphers:** Tools for solving classic ciphers like Caesar, Vigenere, and Atbash.
-   **modern-ciphers:** Attacks against modern symmetric and asymmetric ciphers.
-   **ecc-attacks:** Attacks against elliptic curve cryptography.
-   **prng-attacks:** Techniques for breaking pseudo-random number generators.
-   **hash-attacks:** Attacks against cryptographic hash functions.
-   **lattice-attacks:** Tools and techniques for solving lattice-based crypto challenges.

## Prerequisites

Ensure the following tools are installed and available in your PATH:

```bash
# Python and basic tools
sudo apt-get update
sudo apt-get install -y python3 python3-pip git

# Cryptography libraries
pip install pycryptodome z3-solver sympy gmpy2 hashpumpy fpylll py_ecc

# CTF Tools
sudo apt-get install -y hashcat sagemath
git clone https://github.com/RsaCtfTool/RsaCtfTool.git /opt/RsaCtfTool
```
