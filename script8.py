"""
A simple script that will print a name repeatedly depending
on how many times you specify at the commandline
"""
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('first_name', help="Someone's first name")
parser.add_argument('-m', '--middle', help="Give someone a middle name")
parser.add_argument('last_name', help="Someone's last name")
parser.add_argument('times', type=int, help="The number of times to print the given name",
                    choices=range(6))


def call_user(first, last, times, middle=None):
    if middle:
        print "Calling %s %s %s...\n" % (first, middle, last) * times
    else:
        print "Calling %s %s...\n" % (first, last) * times


if __name__ == "__main__":

    args = parser.parse_args()
    if args.middle:
        call_user(args.first_name, args.last_name, args.times, args.middle)
    else:
        call_user(args.first_name, args.last_name, args.times)

