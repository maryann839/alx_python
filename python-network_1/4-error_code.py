#!/usr/bin/env python3
import requests
import sys

if __name__== "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.text)
    if response.status_code>= 400:
        print('Error code: {response.stautus_code}')