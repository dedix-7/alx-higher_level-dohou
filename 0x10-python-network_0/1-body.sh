#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. This Bash Script, based on the intranet's example, needs to work with redirections.
curl -sL "$1"
