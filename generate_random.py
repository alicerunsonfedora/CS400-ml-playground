#!/usr/bin/env python3
#
# generate_random.py
# Yellow Converse
#
# Created by Marquis Kurt on 11/10/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

from sys import argv
from csv import DictWriter
from argparse import ArgumentParser
from random import randint

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

ACTIONS = [
    "MOVE_LEFT",
    "MOVE_RIGHT",
    "MOVE_UP",
    "MOVE_DOWN",
    "STOP",
    "NEXT_COSTUME",
    "PREV_COSTUME",
    "PICK_UP",
    "DROP",
    "DEPLOY",
    "RETRACT",
    "ACTIVATE",
    "MOVE_RANDOM",
    "MOVE_EXIT_CLOSER",
    "MOVE_INPUT_CLOSER",
    "MOVE_OBJ_CLOSER"
]

def random_bool() -> bool:
    """Returns a random boolean value."""
    return bool(randint(0, 1))

def arguments() -> ArgumentParser:
    """Returns an argument parser."""
    parser = ArgumentParser(
        "Random State Generator",
        usage="generate_random [-h] [--amount [AMOUNT]]",
        description="Generate random abstract states for Yellow Converse."
    )
    parser.add_argument(
        "--amount",
        nargs='?',
        default=50,
        type=int,
        help="The number of states to make."
    )
    return parser

def make_state() -> dict:
    """Returns a randomly-generated state dictionary with a corresponding action."""
    state = { }
    for attribute in ATTRIBUTES:
        state[attribute] = random_bool()
    state["action"] = ACTIONS[randint(0, len(ACTIONS) - 1)]
    return state

if __name__ == "__main__":
    OPTS = arguments().parse_args()

    states = []
    for _ in range(OPTS.amount):
        states.append(make_state())

    with open("random.csv", "w+") as data:
        csv_header = ATTRIBUTES + ["action"]
        csv_author = DictWriter(data, csv_header)
        csv_author.writeheader()
        csv_author.writerows(states)
