#!/usr/bin/python3
"""a python script accept a url, sends request and recieve
response from the url and displays it using requests
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
