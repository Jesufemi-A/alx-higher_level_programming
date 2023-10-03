#!/usr/bin/python3
"""This module accepts a URL and a valid email, then sends 
a POST request to received URL, the  email included
as parameter, and display the respons ein utf-8 format
"""
import sys
import requests


if __name__ == "__main__":
    playload = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=playload)
    print(response.text)
