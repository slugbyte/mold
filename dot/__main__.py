#!/usr/bin/env python
"""The main entry point. Invoke as `dot' or `python -m dot'.
"""
import sys

if __name__ == '__main__':
    try:
        from .main import main
        main()
    except:
        print('Sorry, Unexpected error.', file=sys.stderr)
        return sys.exit(1)
    sys.exit(0)
