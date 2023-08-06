from sys import stderr, exit


def fail(reason, exit_code=1):
    stderr.write(reason + "\n")
    exit(exit_code)
