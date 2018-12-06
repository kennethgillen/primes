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

# integers is now a full data structure of Booleans representing
# prime/not prime, indexed by the value of the integer.

# Iterate through our primes data structure and store and optionally
# print the values which are primes.
#   RFE we could append only primes during the iterations above
#   then sort the values, rather than iterating twice? # TODO gather metrics

# Storing an array of just the primes for later use.
primes_only = np.ones(desired_num_primes, dtype=np.int64)
primes_seen = 1

if verbose:
    print "Iterating our array, to find only the primes."

# Iterate through the data structure till we reach desired number of primes
for this_integer in range(2, integers.size-1):
    #   Note: Maybe numpy has way of making this faster, and only
    #   looking at the next array element already identified as a prime?

    # If this integer is a prime:
    if integers[this_integer]:
        # Down-side here is we're using double the memory we really need.
        if args.verbose:
            print "Seen the prime: " + str(this_integer)
            print "Primes seen: " + str(primes_seen)
        primes_only[primes_seen - 1] = this_integer
        if args.primesonly:
            print "Prime " + str(primes_seen) + ": " + str(this_integer)
        if primes_seen == desired_num_primes:
            # Exit the loop, we're done.
            break
        primes_seen = primes_seen + 1
    this_integer = this_integer + 1

    # RFE - if we want to calculate more values than our speculative array
    # definition has predefined, we'll need to increase the size of the array.


if not args.primesonly:
    # We want to output the product of the array of primes.
    for row in range(primes_only.size+1):
        rowtext = ""
        for column in range(primes_only.size+1):
            if column == 0 and row == 0:
                rowtext += "|   |"
            else:
                if column == 0:
                    rowtext += "| {} |".format(primes_only[row-1])
                elif row == 0:
                    rowtext += " {} |".format(primes_only[column-1])
                else:
                    rowtext += " {} |".format(
                        primes_only[row-1] * primes_only[column-1]
                    )
        print rowtext
