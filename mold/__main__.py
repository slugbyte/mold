#!/usr/bin/env python
"""
The main entry point. Invoke as `mold' or `python -m mold'.
"""

import os 
import sys

import mold.cli as cli 
from mold.context import MoldContext


def main():
    ctx = MoldContext(sys.argv, os.environ)
    if ctx.MOLD_DEBUG:
        sys.exit(cli.handle_context(ctx))
    else:
        try:
            sys.exit(cli.handle_context(ctx))
        except:
            sys.exit(1)
    sys.exit(2)


if __name__ == '__main__':
    main()
