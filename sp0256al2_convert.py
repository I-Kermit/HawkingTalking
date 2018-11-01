#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_in", help="Input file", type=str )
parser.add_argument("file_out", help="Output file", type=str)
parser.parse_args()

args = parser.parse_args()

print("args = " + args)
