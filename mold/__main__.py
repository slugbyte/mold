#!/usr/bin/env python
"""The main entry point. Invoke as `mold' or `python -m mold'.
"""
import os 
import sys
import mold.env as env

from .main import main

if __name__ == '__main__':
    if env.MOLD_DEBUG_MODE:
        main()
    else:
        try:
            main()
        except:
            sys.exit(1)
    sys.exit(0)
