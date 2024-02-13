#!/usr/bin/env python3
""" request a url https://intranet.hbtn.io"""

import urllib.request


if __name__== "__main__":
    url = "https://intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")