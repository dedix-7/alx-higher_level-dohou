#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions,
and print: Error code: followed by the HTTP status code
You must use the packages requests and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
import sys
import requests


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    with requests.get(my_url) as my_response:
        if my_response.status_code == 200:
            print(my_response.text)
        else:
            print("Error code: {}".format(e.status_code))
