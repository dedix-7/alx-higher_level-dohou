#!/usr/bin/python3
"""
A Python script that that takes in a URL, sends a request to that URL,
# and displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import sys
my_url = str(sys.argv[1])
with urllib.request.urlopen(my_url) as my_response:
    if "X-Request-Id" in my_response.headers:
        x_request_id_body = my_response.headers.get("X-Request-Id")
        print(x_request_id_body)
