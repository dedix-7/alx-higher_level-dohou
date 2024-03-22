#!/bin/bash
# A Bash script that displays the status code of an HTTP response
curl -s -o /dev/null -w "%{http_code}" "$1"
