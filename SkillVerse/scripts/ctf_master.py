import sys
import json

def analyze_challenge(description, files):
    """
    Analyzes a CTF challenge to determine its category.
    """
    description = description.lower()
    
    # Simple keyword-based category detection
    if 'crypto' in description or 'cipher' in description or 'rsa' in description or 'aes' in description:
        return 'ctf-crypto'
    elif 'pwn' in description or 'exploit' in description or 'buffer overflow' in description:
        return 'ctf-pwn'
    elif 'web' in description or 'xss' in description or 'sqli' in description:
        return 'ctf-web'
    elif 'forensics' in description or 'steganography' in description or 'pcap' in description:
        return 'ctf-forensics'
    elif 'reverse' in description or 'disassemble' in description or 'ghidra' in description:
        return 'ctf-reverse'
    elif 'osint' in description or 'recon' in description or 'geolocate' in description:
        return 'ctf-osint'
    else:
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
