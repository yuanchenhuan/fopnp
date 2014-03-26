#!/usr/bin/env python3
#
# Check listings for sanity

import os

start1 = """#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# {}
"""

start2 = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Foundations of Python Network Programming, Third Edition
# {}
"""

base = 'https://github.com/brandon-rhodes/fopnp/blob/m/py3/'

def main():
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath == '.':
            continue
        if dirpath.startswith('./'):
            dirpath = dirpath[2:]
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            path = os.path.join(dirpath, filename)
            content = open(path).read()
            url = base + path
            if not (content.startswith(start1.format(url)) or
                    content.startswith(start2.format(url))):
                print(path)

if __name__ == '__main__':
    main()