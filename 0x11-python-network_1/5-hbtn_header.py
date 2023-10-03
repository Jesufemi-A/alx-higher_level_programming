#!/usr/bin/python3
""" a python script that accept a URL, sends request
through the URL receive the response and displays
the response via requests package
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
