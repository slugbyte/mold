#!/usr/bin/env python
"""
The main entry point. Invoke as `mold' or `python -m mold'.
"""

import os 
import sys

from mold.context import MoldContext
from .main import main

if __name__ == '__main__':
    ctx = MoldContext(sys.argv, os.environ)
    if ctx.MOLD_DEBUG:
        sys.exit(main(ctx))
    else:
        try:
            sys.exit(main(ctx))
        except:
            sys.exit(1)
    sys.exit(2)
