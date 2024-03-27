#!/usr/bin/python3
"""
A Python script that that takes in a URL, sends a request to that URL,
and displays the value of the X-Request-Id variable found in the header
of the response.
Usage: ./1-hbtn_header.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    with requests.get(my_url) as my_response:
        if 'X-Request-Id' in my_response.headers:
            print(my_response.headers['X-Request-Id'])
