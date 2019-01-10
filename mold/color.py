import sys 
# import mold.env as env 
# check if pogram is being piped dont print colors or MOLD_COLOR is set

# FIX OR MIGRATE COLOR_MODE
_is_colormode = sys.stdout.isatty() #or env.MOLD_COLOR 

red = '\033[31m' if _is_colormode else ''
green = '\033[32m' if _is_colormode else ''
yellow = '\033[33m' if _is_colormode else ''
blue = '\033[94m' if _is_colormode else ''
magenta  = '\033[35m' if _is_colormode else ''
cyan = '\033[36m' if _is_colormode else ''
lightgrey = '\033[37m' if _is_colormode else ''
grey = '\033[38m' if _is_colormode else ''
reset = '\033[39m' if _is_colormode else ''
