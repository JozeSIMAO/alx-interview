#!/usr/bin/python3

import sys


def print_stats(status_codes, total_file_size):
    """
    Method to print statistics
    Args:
        status_codes: Dictionary containing counts of status codes
        total_file_size: Total file size
    Returns:
        None
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count != 0:
            print("{}: {}".format(code, count))


total_file_size = 0
counter = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                total_file_size += file_size
                status_codes[status_code] += 1
                counter += 1
                if counter == 10:
                    print_stats(status_codes, total_file_size)
                    counter = 0

except KeyboardInterrupt:
    pass

finally:
    print_stats(status_codes, total_file_size)
