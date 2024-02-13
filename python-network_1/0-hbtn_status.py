#!/usr/bin/env python3
""" request a url https://intranet.hbtn.io"""

import requests



if __name__== "__main__":
    url = "https://intranet.hbtn.io/status"
    
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
