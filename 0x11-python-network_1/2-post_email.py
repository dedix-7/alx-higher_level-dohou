#!/usr/bin/python3
"""
A Python script that that takes in a  URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
Usage: ./1-hbtn_header.py <URL> <email>
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    my_email = {"email": str(sys.argv[2]}
    data_to_send = urllib.parse.urlencode(my_email).encode("ascii")
    my_request = urllib.request.Request(my_url, data_to_send, method="POST")
    with urllib.request.urlopen(my_request) as my_response:
        # Creating the POST object
        print(my_response.read().decode("utf-8"))
