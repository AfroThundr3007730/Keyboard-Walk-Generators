#!/usr/bin/env python3

# pyright: reportMissingParameterType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownParameterType=false
# pyright: reportUnknownVariableType=false
# pylint: disable=missing-function-docstring

"""
Combine strings into arbitrary length strings

usage: combinator.py [-h] [-l [L]] [file_name]

positional arguments:
    file_name               File with strings of same length

optional arguments:
    -h, --help              show this help message and exit
    -l [L], -length [L]     Length of final strings

The MIT License (MIT)

Copyright (c) 2014 Rich Kelley, RK5DEVMAIL[A T]gmail[D O T]com, @RGKelley5
"""

import argparse
from math import ceil


def combine(file_name, string_len, input_len, trim_len, output):
    if string_len > 0:
        with open(file_name, "r", encoding="utf8") as _f:
            for _, chunk in enumerate(_f):
                combine(
                    file_name,
                    string_len - input_len,
                    input_len,
                    trim_len,
                    output + chunk.rstrip(),
                )
    else:
        output = output.rstrip()
        print(output[: len(output) - trim_len])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Combinator: Combine strings into arbitrary length strings"
    )
    parser.add_argument(
        "file_name",
        nargs="?",
        help="File with strings of same length",
        type=str,
    )
    parser.add_argument(
        "-l",
        "-length",
        nargs="?",
        help="Length of final strings",
        type=int,
        default=1,
    )
    args = parser.parse_args()
    with open(args.file_name, "r", encoding="utf8") as _f:
        first_line = _f.readline()
        first_line = first_line.rstrip()
    # Script assumes all lines are the same length
    input_length = len(first_line)
    num_of_copies = int(ceil(float(args.length) / float(input_length)))
    trim_length = -1 * (args.length - (input_length * num_of_copies))
    combine(args.file_name, args.length, input_length, trim_length, "")
