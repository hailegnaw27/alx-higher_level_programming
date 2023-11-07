#!/usr/bin/python3
"""
Module for log parsing script.
"""

import sys

if __name__ == '__main__':
    count = 0                  # Count of lines processed
    file_size = 0              # Total file size
    status_codes = {}          # Dictionary of status codes and their count

    try:
        for line in sys.stdin:  # Read lines from stdin
            count += 1         # Increment the count of lines
            split_line = line.split()
            if len(split_line) > 6:
                status_code = split_line[-2]
                file_size += int(split_line[-1])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if count % 10 == 0:  # Every 10 lines...
                print("File size: {}".format(file_size))
                for k in sorted(status_codes.keys()):
                    print("{}: {}".format(k, status_codes[k]))

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {}".format(file_size))
        for k in sorted(status_codes.keys()):
            print("{}: {}".format(k, status_codes[k]))
