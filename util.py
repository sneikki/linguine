import os
from sys import stderr, exit
import json, csv


def fail(reason, exit_code=1):
    stderr.writelines([
        f"Error -- {reason}\n",
        "\nUsage: linguine <json-file> <json-file> [-o|--output <output-file>]\n"
    ])
    exit(exit_code)


def get_basename(path):
    return os.path.splitext(os.path.basename(path))[0]


def read_json(path):
    try:
        return json.load(open(path, mode="r"))
    except OSError:
        fail(f"{path}: no such file exists")
    except json.decoder.JSONDecodeError:
        fail(f"{path}: invalid format")


def write_csv(path, data):
    file_obj = open(path, "w")
    csv.writer(file_obj,
               delimiter="\t"
               ).writerows(data)