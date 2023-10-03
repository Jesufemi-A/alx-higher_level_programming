#!/usr/bin/python3
""" a python script that accept a  URL, sends request
receive the response and displays it in utf-8 format
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
