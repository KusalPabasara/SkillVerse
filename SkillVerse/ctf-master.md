---
name: ctf-master
description: "The master skill for orchestrating CTF challenge solving. It analyzes challenges and delegates to the appropriate sub-skills."
version: 1.0.0
author: Hermes Agent & KusalPabasara
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [CTF, Hacking, Security, Orchestration]
    related_skills: [ctf-crypto, ctf-pwn, ctf-web, ctf-forensics, ctf-reverse, ctf-osint, ctf-misc]
---

# CTF Master Skill

This skill is the primary entry point for solving CTF challenges with the Hermes Agent. It acts as an orchestrator, analyzing the challenge and delegating the task to the appropriate specialized sub-skill.

## When to Use

- When you are starting a new CTF challenge.
- When you are not sure which category a challenge falls into.

## Core Capabilities

1.  **Challenge Analysis:** The skill takes the challenge description, files, and any other information as input and performs an initial analysis to determine the challenge category.
2.  **Skill Delegation:** Based on the analysis, the skill delegates the task to the appropriate sub-skill (e.g., `ctf-crypto`, `ctf-pwn`, `ctf-web`).
3.  **Context Management:** The skill manages the context of the challenge, passing relevant information between skills as needed.
4.  **User Interaction:** The skill can interact with the user to ask for clarification or provide updates on the progress of the challenge.

## Getting Started

To use this skill, simply present the CTF challenge to the agent with this skill loaded. For example:

> "I have a new CTF challenge. The description is '...' and I have a file named '...'. Can you solve it?"

The `ctf-master` skill will then take over, analyze the challenge, and begin the solving process.
