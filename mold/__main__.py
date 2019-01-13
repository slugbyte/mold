#!/usr/bin/env python
"""
The main entry point. Invoke as `mold' or `python -m mold'.
"""

# import os 
import sys

# from mold.context import MoldContext
# from .main import main
from mold.help import help_example

if __name__ == '__main__':
    help_example()
    sys.exit(0)
    # ctx = MoldContext(sys.argv, os.environ)
    # if ctx.MOLD_DEBUG:
        # sys.exit(main(ctx))
    # else:
        # try:
            # sys.exit(main(ctx))
        # except:
            # sys.exit(1)
    # sys.exit(2)
