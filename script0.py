
FIRST_NAME = "JOE"
LAST_NAME = "SMITH"

PRINT_TIMES = 8


def call_user(first, last, times):
    print "Calling %s %s...\n" % (first, last) * times


if __name__ == "__main__":

    call_user(FIRST_NAME, LAST_NAME, PRINT_TIMES)
