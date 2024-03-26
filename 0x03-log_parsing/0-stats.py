#!/usr/bin/python3
""" Solution
"""

import time
import sys

output = sys.stdin


def log_parsing():
    """implementation
    """
    big_list = []
    total_items = 0
    status_count = {}

    try:
        for line in output:
            data = line.strip().split()
            status_code = int(data[-2])
            file_size = int(data[-1])
            if isinstance(status_code, int) and isinstance(file_size, int):
                my_dict = {'status_code': status_code, 'file_size': file_size}
                big_list.append(my_dict)
                if len(big_list) == 10:
                    for items in big_list:
                        total_items += items.get('file_size')
                        code = items.get('status_code')
                        status_count[code] = status_count.get(code, 0) + 1
                    print(f'File size: {total_items}')
                    for key_code, val_count in sorted(status_count.items()):
                        print(f'{key_code}: {val_count}')
                    big_list.clear()
    except KeyboardInterrupt:
        print(f"File size: {total_items}")
        for code, count in sorted(status_count.items()):
            if count > 0:
                print(f"{code}: {count}")
        sys.exit(0)


if __name__ == '__main__':
    log_parsing()
