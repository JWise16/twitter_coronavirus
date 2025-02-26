#!/usr/bin/env python3
import argparse
import os
import json
from collections import Counter, defaultdict

def combine_files(input_paths, suffix):
    """
    Processes input files that end with the given suffix and
    aggregates their counts.
    """
    aggregate = defaultdict(Counter)
    for path in input_paths:
        if not path.endswith(suffix):
            continue
        with open(path) as f:
            tmp = json.load(f)
            for key, subcounts in tmp.items():
                # merge subcounts using Counter arithmetic
                aggregate[key] += Counter(subcounts)
    return aggregate

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True,
                    help="List of input file paths (both .lang and .country files)")
parser.add_argument('--lang_output_path', required=True,
                    help="Output file path for the combined .lang data")
parser.add_argument('--country_output_path', required=True,
                    help="Output file path for the combined .country data")
args = parser.parse_args()

# Combine files based on the file extension
lang_total = combine_files(args.input_paths, '.lang')
country_total = combine_files(args.input_paths, '.country')

# Write out the aggregated results into two separate files
with open(args.lang_output_path, 'w') as f:
    json.dump(lang_total, f)

with open(args.country_output_path, 'w') as f:
    json.dump(country_total, f)

