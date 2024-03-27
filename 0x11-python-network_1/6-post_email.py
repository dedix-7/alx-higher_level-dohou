#!/usr/bin/python3
"""
A Python script that that takes in a  URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
Usage: ./6-post_email.py <URL> <email>
"""
import requests
import sys


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    my_email = {"email": str(sys.argv[2])}
    with requests.post(my_url, my_email) as my_request:
        print(my_request.text)
