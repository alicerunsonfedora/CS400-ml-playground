#!/usr/bin/env python3
#
# stitch_csv.py
# Teal Converse
#
# Created by Marquis Kurt on 11/10/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import os
from sys import argv
from csv import DictWriter, DictReader
from argparse import ArgumentParser

ATTRIBUTES = [
    "canEscape",
    "nearExit",
    "nearInput",
    "inputActive",
    "inputRelevant",
    "requiresObject",
    "requiresCostume",
    "wearingCostume",
    "hasObject",
    "nearObject",
    "allInputsActive"
]

def arguments() -> ArgumentParser:
    """Returns an argument parser."""
    parser = ArgumentParser(
        "Random State Generator",
        usage="generate_random [-h] [--amount [AMOUNT]]",
        description="Stitch CSV files for Teal Converse states."
    )
    parser.add_argument(
        "--path",
        type=str,
        help="The directory to the CSV files to stitch together."
    )
    return parser

def add_to_dictionary(filepath: str, entries: list):
    """Read the CSV file and dump the contents into a list of entries."""
    with open(filepath, 'r', encoding="utf-8") as file:
        csv_reader = DictReader(file, ATTRIBUTES + ["action"])
        next(csv_reader) # skip headers
        for row in csv_reader:
            entries.append(row)

def write_to_file(entries: list, to_path: str):
    """Write the list of entries to a CSV file."""
    with open(to_path, 'w+') as writer:
        csv_writer = DictWriter(writer, ATTRIBUTES + ["action"])
        csv_writer.writeheader()
        csv_writer.writerows(entries)


if __name__ == "__main__":
    OPTS = arguments().parse_args(argv[1:])
    entries = []

    if not os.path.isdir(OPTS.path):
        print("ERR: specified argument does not point to path. Aborting.")
        exit()

    for file in os.listdir(OPTS.path):
        if file.endswith(".csv"):
            add_to_dictionary(os.path.join(OPTS.path, file), entries)

    write_to_file(entries, os.path.join(OPTS.path, "stitched.csv"))
