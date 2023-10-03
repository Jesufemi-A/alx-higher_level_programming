#!/usr/bin/python3
""" a python script accept letter then sends
request to http://0.0.0.0:5000/search_user with parameter letter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    playload = {"q": q}
    resp = requests.post(url, data=playload)
    try:
        r = resp.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print("Not a valid JSON")
