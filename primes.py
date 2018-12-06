#!/usr/bin/python

import sys
import argparse
import numpy as np

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

# Convert the list to a string with spaces
desired_num_primes = int(args.count[0])

if verbose:
    print "Number of primes to calculate: " + str(desired_num_primes)

# Using the Sieve of Eratosthenes, cf
# https://en.wikipediintegers.org/wiki/Sieve_of_Eratosthenes

# Declare a numpy array of bool values to store "prime or not"
# The array index will be used to refer to an integer value.
speculative_largest_prime = desired_num_primes * 15
integers = np.ones(speculative_largest_prime + 1, dtype=bool)

# RFE - this will currently run through the entire array
# regardless of how many primes we've "found". It'd be faster
# to stop when we've found enough.

# Iterate through the entire array
# RFE - try a numpy iterator, rather than a for loop and variable.
# Perhaps it would be more performance. Get objective data.
for this_integer in range(2, integers.size-1):

    # Outer loop marker
    current_int = this_integer
    # The "incrementer" will run through the array and set
    # every nth value as non-prime. n here is the iteration_increment
    iteration_increment = this_integer

    if verbose:
        print "Incrementing through the array, setting" \
              + " elements to not-prime every " \
              + str(iteration_increment)

    if verbose:
        print "Integer is: " + str(this_integer)
        print "Increment is: " + str(this_integer)

    # The previous incrementer run (this_integer-1, this_integer-2...)
    # will have already identified non-primes. Don't need to kick off
    # new incrementers for these values.
    # i.e. only kick off an incrementer if current_int is a prime
    if integers[current_int]:
        # Until we hit the end of our list...
        while current_int <= integers.size-1:
            # Move to next int to kick off an incrementer run
            if verbose:
                print "current_int: " + str(current_int)
            # current_int is a prime, so next one, and all
            # following the same incrementer sequence, are not.

            # Step over "current_int", according to sequence
            current_int = current_int + iteration_increment

            # in case we have incremented outside the end of the array
            if current_int <= integers.size-1:
                # flag as NOT PRIME
                integers[current_int] = False

# RFE: Stopping running the iterator once we've
# identified enough primes?

# RFE: Given that the first iterator step is 2 * current_int, no point
# in finishing the outer loop after the first iterator is off the end of
# the array ?

# Iterate through our primes data structure, and output the values.
primes_seen = 1
if verbose:
    print "Iterating through the structure."

if args.primesonly:
    # Iterate through the whole data structure
    for this_integer in range(2, integers.size-1):
        if integers[this_integer]:
            # Look at the next element of the array.
            #  Maybe numpy has way of making this faster, and only
            #  looking at the next array element already identified as a prime?
            print "Prime " + str(primes_seen) + ": " + str(this_integer)
            if primes_seen == desired_num_primes:
                sys.exit(0)
            primes_seen = primes_seen + 1
        this_integer = this_integer + 1

    # RFE - if we want to calculate more values than our speculative array
    # definition has predefined, we'll need to increase the size of the array.
