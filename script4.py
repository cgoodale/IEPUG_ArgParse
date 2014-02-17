"""
A simple script that will print a name repeatedly depending
on how many times you specify at the commandline
"""
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('times', type=int)


def call_user(first, last, times):
    print "Calling %s %s...\n" % (first, last) * times


if __name__ == "__main__":

    args = parser.parse_args()
    call_user(args.first_name, args.last_name, args.times)

