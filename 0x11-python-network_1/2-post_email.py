#!/usr/bin/python3
"""This module accepts a URL and a valid email, then sends 
a POST request to received URL, the  email included
as parameter, and display the respons ein utf-8 format
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
