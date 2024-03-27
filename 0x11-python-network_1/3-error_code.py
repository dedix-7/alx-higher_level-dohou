#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions,
and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
import sys
import urllib.request
import urllib.error
import urllib.parse


if __name__ == "__main__":
    my_url = str(sys.argv[1])
    with urllib.request.urlopen(my_url) as my_response:
        try:
            read_response = my_response.read()
            print(read_response)
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
