import sys

from util import fail


def run():
    args = sys.argv[1:]

    if len(args) != 2:
        fail("Two JSON files are required")


if __name__ == "__main__":
    run()
