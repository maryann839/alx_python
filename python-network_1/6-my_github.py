#!/usr/bin/env python3
import requests
import sys

if __name__== "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    url = 'https://api.hithub.com/user'
    auth = (username, personal_access_token)
    response = requests.get(url, auth=auth)
    try:
        user_data = response.json()
        print('Github user ID:', user_data.get('id'))
    except ValueError:
        print('Error: Invalid JSON response from Github API')
