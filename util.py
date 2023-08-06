from sys import stderr, exit


def fail(reason, exit_code=1):
    stderr.write(reason + "\n")
    exit(exit_code)


def read_json(path):
    try:
        open(path, mode="r")
    except OSError:
        fail(f"{path}: no such file exists")
