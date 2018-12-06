#!/usr/bin/python

import sys
import argparse
# import numpy as np

parser = argparse.ArgumentParser(
    description='An application to calculate and output a \
    multiplication table of made of prime numbers.'
)
parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="include verbose output."
)

parser.add_argument(
    "-p", "--primesonly",
    action="store_true",
    help="output just a list of prime numbers."
)

parser.add_argument(
    "count",
    nargs=1,
    help="the (integer) number of prime numbers you wish to calculate."
)

# Display the full help message if the user hasn't supplied any arguments.
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

verbose = args.verbose
