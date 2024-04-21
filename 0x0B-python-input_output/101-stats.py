#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys
import signal


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats(total_size=None, status_codes=None):
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))


signal.signal(signal.SIGINT, signal_handler)
