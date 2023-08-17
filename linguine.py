#!/usr/bin/env python3

import sys

from util import fail, read_json, write_csv, get_basename

from collections.abc import MutableMapping

def _flatten_dict_gen(d, parent_key, sep):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v


def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.'):
    return dict(_flatten_dict_gen(d, parent_key, sep))


def run():
    args = sys.argv[1:]
    output_path = None
    encoding = "utf8"
    json_paths = []

    while len(args) > 0:
        arg = args.pop(0)

        if arg in ["-o", "--output"]:
            try:
                output_path = args.pop(0)
            except IndexError:
                fail(
                    f"""Path for the output file must be specified when using "{arg}" flag""")
        elif arg in ["-e", "--encoding"]:
            try:
                encoding = args.pop(0)
            except IndexError:
                fail(f"""Encoding must be specified when using "{arg}" flag""")
        else:
            json_paths.append(arg)

    if len(json_paths) != 2:
        fail("path to the JSON files are required")

    source_dict = flatten_dict(read_json(json_paths[0], encoding))
    target_dict = flatten_dict(read_json(json_paths[1], encoding))
    value_pairs = []

    for key, value in source_dict.items():
        if key in target_dict:
            value_pairs.append((value, target_dict[key]))

    write_csv(output_path if output_path is not None else "_".join(
        map(get_basename, json_paths)) + "_aligned.csv", value_pairs)


if __name__ == "__main__":
    run()
