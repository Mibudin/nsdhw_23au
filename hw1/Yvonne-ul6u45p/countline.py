#!/usr/bin/env python3

import sys
import os.path

if(os.environ['PYTHON_BIN'] == "python0"):
    sys.stdout.write("[ERROR] exec: python0: not found\n")
    exit(1)     # exit with an error code

elif(os.environ['PYTHON_BIN'] == "python2") or (os.environ['PYTHON_BIN'] == "python3"):
    if len(sys.argv) < 2:
        sys.stdout.write('missing file name\n')
    elif len(sys.argv) > 2:
        sys.stdout.write('only one argument is allowed\n')
    else:
        fname = sys.argv[1]
        if os.path.exists(fname):
            with open(fname) as fobj:
                lines = fobj.readlines()
            sys.stdout.write('{} lines in {}\n'.format(len(lines), fname))
        else:
            sys.stdout.write('{} not found\n'.format(fname)
