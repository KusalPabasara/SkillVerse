import sys
import json
import os

def analyze_challenge(description, files):
    """
    Analyzes a CTF challenge to determine its category.
    """
    description = description.lower()
    
    # Simple keyword-based category detection
    if 'crypto' in description or 'cipher' in description or 'rsa' in description or 'aes' in description:
        return 'ctf-crypto'
    if 'pwn' in description or 'exploit' in description or 'buffer overflow' in description:
        return 'ctf-pwn'
    if 'web' in description or 'xss' in description or 'sqli' in description:
        return 'ctf-web'
    if 'forensics' in description or 'steganography' in description or 'pcap' in description:
        return 'ctf-forensics'
    if 'reverse' in description or 'disassemble' in description or 'ghidra' in description:
        return 'ctf-reverse'
    if 'osint' in description or 'recon' in description or 'geolocate' in description:
        return 'ctf-osint'

    # File extension-based category detection
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in ['.pcap', '.pcapng', '.dd', '.vmem', '.raw', '.img']:
            return 'ctf-forensics'
        if ext in ['.elf', '.exe', '.so', '.dll', '.apk']:
            return 'ctf-pwn' # Could also be reverse, but pwn is a good starting point
        if ext in ['.py', '.php', '.js', '.html', '.css', '.jar', '.war']:
            return 'ctf-web'
        if ext in ['.pem', '.der', '.key', '.crt', '.cer']:
            return 'ctf-crypto'

    return 'ctf-misc'

def main():
    if len(sys.argv) < 2:
        print("Usage: python ctf_master.py <description> [file1, file2, ...]")
        sys.exit(1)

    description = sys.argv[1]
    files = sys.argv[2:]

    category = analyze_challenge(description, files)
    
    # In a real scenario, the agent would now delegate to the skill
    # For now, we'll just print the detected category
    print(json.dumps({"detected_category": category}, indent=4))

if __name__ == "__main__":
    main()
