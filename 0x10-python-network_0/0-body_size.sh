#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# I tested my script in my Ubuntu 20.04 Python Network Sandbox
curl -s "$1" | wc -c
