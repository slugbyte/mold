#!/usr/bin/env python
"""The main entry point. Invoke as `mold' or `python -m mold'.
"""
import os 
import sys

from .main import main

if __name__ == '__main__':
    if os.environ['MOLD_DEBUG_MODE']:
        main()
    else:
        try:
            main()
        except:
            print('Sorry, Unexpected error.', file=sys.stderr)
            sys.exit(1)
    sys.exit(0)
