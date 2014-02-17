"""
Example Call:

python script1.py first_name last_name print_times
"""
import sys

try:
    FIRST_NAME = sys.argv[1]
except IndexError:
    message = "Please provide a valid string for 'first_name'"
    sys.exit(message)

try:
    LAST_NAME = sys.argv[2]
except IndexError:
    message = "Please provide a valid string for 'last_name'"
    sys.exit(message)

try:
    PRINT_TIMES = int(sys.argv[3])
except IndexError:
    message = "Please provide a valid int for the number of times to print"
    sys.exit(message)
except ValueError:
    message = "Please provide a valid integer value instead of '%s'" % sys.argv[3]
    sys.exit(message)


def call_user(first, last, times):
    print "Calling %s %s...\n" % (first, last) * times


if __name__ == "__main__":

    call_user(FIRST_NAME, LAST_NAME, PRINT_TIMES)

