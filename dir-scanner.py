#!/usr/bin/env python3
import argparse
import requests
import time

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="Target URL to scan")    #Flag to specify the target URL for scanning
parser.add_argument("-o", "--output", help="Output file for results")   #Flag to specify the output file for results
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")    #Flag to specify the wordlist file to use for scanning
args = parser.parse_args()
target_url = args.url.rstrip("/")  # Remove trailing slash if present
output_file = args.output  
wordlist_file = args.wordlist

with open(wordlist_file, "r") as f:
    words = f.readlines()
total = len(words)


session = requests.Session()    # Create a session object for making requests
fake = session.get(f"{target_url}/blahblahblahblah", timeout=5)  # Make a request to a non-existent page to get the fake response

for count, word in enumerate(words, start=1):
    
    
    word = word.strip()
    if not word or word.startswith("#"):
            continue
    time.sleep(0.01)  # Add a small delay to avoid overwhelming the server
    percent = (count / total) * 100
    
    try:
        res = session.get(f"{target_url}/{word}", timeout=5)
        
        if (res.text != fake.text 
            or res.status_code != fake.status_code
            or len(res.content) != len(fake.content)):
        


            if res.status_code != 404:
                print(f"{percent:.1f}% - {res.status_code} - {word}")
                if output_file:
                    with open(output_file, "a") as f:
                        f.write(f"{target_url}/{word} - {res.status_code}\n")
        
        
        
    except requests.RequestException as e:
        print(f"{percent:.1f}% - Error - {word}: {e}")

