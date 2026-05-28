# SkillVerse: Your AI Companion for Capture The Flag Challenges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/KusalPabasara/SkillVerse.svg)](https://github.com/KusalPabasara/SkillVerse/commits/master)

SkillVerse is an open-source toolkit designed to supercharge Large Language Models (LLMs) like Gemini with the specialized knowledge and automated tools needed to excel at Capture The Flag (CTF) competitions. This project, powered by the Hermes Agent, aims to be the ultimate AI-powered assistant for CTF enthusiasts, security researchers, and students.

## The Problem

While modern LLMs are incredibly powerful, they often lack the specific, deep-domain knowledge and the ability to run specialized tools required for complex CTF challenges. Solving these challenges requires not just reasoning but also the practical application of a wide array of security tools and techniques.

## The Solution

SkillVerse bridges this gap by providing a structured, agent-driven framework of "skills." Each skill is a combination of a knowledge base, automated scripts, and integrations with standard CTF tools. This allows an AI agent to not only understand a CTF challenge but also to take active steps to solve it.

## Features

-   **Modular Skill System:** Organized by CTF category (Crypto, Pwn, Web, etc.) for a clean and extensible architecture.
-   **Automated Tooling:** Scripts for automating common attacks and analysis tasks, from RSA factorization to solving classic ciphers.
-   **Orchestration Engine:** A master skill (`ctf-master`) that analyzes challenges and delegates them to the appropriate specialized skill.
-   **Rich Knowledge Base:** Incorporates and builds upon the excellent `ljagiello/ctf-skills` repository, providing a vast library of reference material for the agent.

## Project Structure

-   `/SkillVerse`: The main directory containing all the skills.
-   `/<category>`: Each CTF category (e.g., `crypto`, `pwn`) has its own directory.
-   `SKILL.md`: The definition file for each skill.
-   `/scripts`: Contains the executable Python scripts that automate tasks.
-   `/references`: Contains the detailed knowledge base in Markdown files.

## Getting Started

### Prerequisites

-   [Hermes Agent](https://github.com/NousResearch/Hermes-Function-Calling) installed and configured.

### Installation

You can install the SkillVerse skills using the provided installation script:

```bash
./install.sh
```

This script will clone the repository and create symbolic links to the skills in your Hermes Agent skills directory (`~/.hermes/skills`).

## Usage

Once the skills are installed, you can start using them with your Hermes Agent. The `ctf-master` skill is the main entry point.

**Example:**

> **You:** I have a new CTF challenge. The description is "I found this weird file, can you decrypt it? It's called `message.txt`." I also have a public key file `key.pem`.
>
> **Hermes Agent (with SkillVerse):** *(The `ctf-master` skill is activated. It analyzes the description and the `.pem` file, determines it's a crypto challenge, and delegates to the `ctf-crypto` skill. The `crypto-analyzer` then inspects the key and suggests an attack...)*

## Roadmap

-   [ ] **Pwn:** Add skills for binary exploitation, including buffer overflows, ROP chains, and heap exploitation.
-   [ ] **Web:** Add skills for web application security, including XSS, SQLi, and LFI/RFI.
-   [ ] **Forensics:** Add skills for file format analysis, steganography, and network traffic analysis.
-   [ ] **Full Integration:** Enable seamless, multi-step problem solving where the agent can chain skills together (e.g., a forensics skill extracts a file, which is then passed to a crypto skill).
-   [ ] **NPM/PyPI Package:** Create a more formal package for easier distribution.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## Acknowledgements

This project was inspired by and builds upon the excellent work of the [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills) repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
