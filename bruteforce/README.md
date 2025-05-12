# Cyber Sentinel Secure Brute Force Tool
## Overview

This Python script performs a brute force attack against a web login form by systematically testing combinations of usernames and passwords from provided wordlists.

## Features:

    Multi-threaded credential testing

    Customizable target URL

    Supports HTML form-based authentication

    Credential loading from text files

    Response parsing with BeautifulSoup

    Session management with requests.Session

## Prerequisites:

    Python 3.x

Required Python packages:

```bash
pip install requests beautifulsoup4
```

## Usage

Prepare your credential files:

    user.txt - Contains list of usernames (one per line)

    wordlist.txt - Contains list of passwords (one per line)

Modify the target URL in the main() function
```bash
def main():
    target = 'http://127.0.0.1:8080' <CHANGE THIS>

    print(f'[+] Starting Brute Force attack on {target}')
    print(f'[+] Loaded credentials: ', len(load_credentials()))

    user, passwd = brute(target)

    if user and passwd:
        print('[+] Brute force challange has been passed')
    else:
        print('Credential not found!')

if __name__ == '__main__':
    main()
```

Run the script:
```bash
python brute.py
```

## File Structure

```
brute.py                - Main brute force script
user.txt                - Username wordlist
wordlist.txt            - Password wordlist
```

## Configuration

Edit these variables in the code:

    target in main() function - Set your target login URL

    File paths in load_credentials() - Update if your wordlists are in different locations

## Legal Disclaimer

This tool is for educational and authorized penetration testing purposes only. Unauthorized use against systems you don't own or have explicit permission to test is illegal. The developers assume no liability and are not responsible for any misuse or damage caused by this program.
