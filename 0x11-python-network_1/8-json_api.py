#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
Otherwise:
    - Display Not a valid JSON if the JSON is invalid
    - Display No result if the JSON is empty
    - You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    my_url = "http://0.0.0.0:5000/search_user"
    my_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    my_payload = {"q": my_letter}
    my_request = requests.post(my_url, my_payload)
    try:
        my_response = my_request.json()
        if my_response == {}:
            print("No result")
        else:
            print(
                "[{}] {}".format(
                    my_response.get("id"),
                    my_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
