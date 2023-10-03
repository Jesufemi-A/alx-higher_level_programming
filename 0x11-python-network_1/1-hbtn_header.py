#!/usr/bin/python3
"""The module accepet URL,
then sends  request to the URL and then display
the value of the request
"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as resp:
        header = dict(resp.headers)
        print(header.get("X-Request-Id"))
