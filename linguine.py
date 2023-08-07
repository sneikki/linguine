#!/usr/bin/env python3

import sys

from util import fail, read_json, write_csv, get_basename


def run():
    args = sys.argv[1:]
    output_path = None
    json_paths = []

    while len(args) > 0:
        arg = args.pop(0)

        if arg in ["-o", "--output"]:
            try:
                output_path = args.pop(0)
            except IndexError:
                fail(
                    f"""Path for the output file must be specified when using "{arg}" flag""")
        else:
            json_paths.append(arg)

    if len(json_paths) != 2:
        fail("path to the JSON files are required")

    source_dict = read_json(json_paths[0])
    target_dict = read_json(json_paths[1])
    value_pairs = []

    for key, value in source_dict.items():
        if key in target_dict:
            value_pairs.append((value, target_dict[key]))

    write_csv(output_path if output_path is not None else "_".join(
        map(get_basename, json_paths)) + "_aligned.csv", value_pairs)


if __name__ == "__main__":
    run()
