#!/usr/bin/env python
import sys
import argparse

from PIL import Image
import numpy as np


AVAILABLE_ALGOS = ["predictive", "pairs"]
DEFAULT_OUTPUT_NAME = "output.bin"

op = {
    "input" : None,
    "output": DEFAULT_OUTPUT_NAME,
    "algo"  : None,
}

def parse(op):
    parser = argparse.ArgumentParser(
        description='Encode image files using different algorythms')

    parser.add_argument("-i", "--input",
                        dest='input',
                        required=True,
                        help="source image file",)

    parser.add_argument("-o", "--output",
                        dest='output',
                        help="destination filename",)

    parser.add_argument("-a", "--algo",
                        dest='algo',
                        help="Select encoding algorythms",)

    args = parser.parse_args()

    if not args.algo in AVAILABLE_ALGOS:
        print(
            "Unknown algorythm\n\n"
            "Available algorythms are:")
        for a in AVAILABLE_ALGOS:
            print(" - " + a)
        sys.exit(1)
    else:
        op["algo"] = args.algo

    # import pdb; pdb.set_trace()
    op["input"] = args.input
    if args.output:
        op["output"] = args.output


def run(op):
    try:
        img = Image.open(op['input'])
    except Exception as e:
        print(e)
        sys.exit(1)

    if op['algo'] == 'pairs':
        pass
        # import algo.pairs as pairs

    
if __name__ == "__main__":
    parse(op)
    if op["input"] and op["output"] and op["algo"]:
        run(op)
