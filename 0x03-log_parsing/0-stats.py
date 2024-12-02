#!/usr/bin/python3
"""
Script to process log lines from stdin and compute metrics.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys


def print_stats(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    Main function to process lines and compute statistics.
    """
    total_size = 0
    line_count = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            try:
                # Parse the line
                parts = line.split()
                if len(parts) < 7:
                    continue

                # Extract status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update metrics
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                # Skip invalid lines
                continue

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(total_size, status_counts)
        raise

    # Final stats
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
