#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status using
# the urllib package
import urllib.request
my_url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(my_url) as my_response:
    read_response = my_response.read()
    if my_response.status == 200:
        # print(my_response.read())
        # print(type(my_response.read()))
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}".format(
                type(read_response.decode('utf-8')),
                read_response.decode('utf-8')))
# In Python, \t represents the escape sequence for a horizontal tab character.
# When used within a string, \t inserts a tab character, which typically moves
# the cursor to the next tab stop.
