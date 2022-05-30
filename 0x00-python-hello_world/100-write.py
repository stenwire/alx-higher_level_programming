#!/usr/bin/python3
import sys
from sys import stderr

str = 'and that piece of art is useful - Dora Korpar, 2015-10-19'

sys.stderr.write(str + '\n')
sys.stderr.flush()
exit(1)
