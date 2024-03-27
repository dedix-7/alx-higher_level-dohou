#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status using
# the requests module
import requests
my_url = "https://alx-intranet.hbtn.io/status"
with requests.get(my_url) as my_response:
    if my_response.status_code == 200:
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}".format(
                type(my_response.text),
                my_response.text))
# In Python, \t represents the escape sequence for a horizontal tab character.
# When used within a string, \t inserts a tab character, which typically moves
# the cursor to the next tab stop.
