#!/usr/bin/env python3
import requests
import sys

if __name__== "__main__":
    url = sys.argv[1]

    response =requests.get(url)
    if response.status_code == 200:
        x_request_id =response.headers.get('x-Request-id')
        if x_request_id:
            print(x_request_id)
        else:
            print('x_request_id header not foundin the response')
    else:
        print(f'Failed to retrieve data. Status Code: {response.status_code}')