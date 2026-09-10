# directory-scanner

`directory-fuzzer` is a short and simple Python directory enumeration tool that I created for use in my own cybersecurity projects and labs. I may continue updating and improving it in the future.

The script goes through each entry in the wordlist provided with the `-w` option and sends requests to the target URL provided with `-u`. It then checks the responses to identify potentially existing directories or pages.

## Usage

To view the available options:

```bash
python3 /path/to/dir-scanner.py -h
```

Example:

```bash
python3 dir-scanner.py -u http://127.0.0.1:3000 -w /path/to/wordlist.txt
```

You can also save discovered results to a file using:

```bash
python3 dir-scanner.py -u http://127.0.0.1:3000 -w /path/to/wordlist.txt -o results.txt
```

## Legal Notice

This tool is intended for educational purposes, personal labs, CTF environments, and systems you are explicitly authorised to test.

**Do not use this tool against websites or systems without explicit permission from the owner.**
