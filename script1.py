"""
Example Call:

python script1.py first_name last_name print_times
"""
import sys

FIRST_NAME = sys.argv[1]
LAST_NAME = sys.argv[2]

PRINT_TIMES = sys.argv[3]



def call_user(first, last, times):
    print "Calling %s %s...\n" % (first, last) * times


if __name__ == "__main__":

    call_user(FIRST_NAME, LAST_NAME, PRINT_TIMES)

