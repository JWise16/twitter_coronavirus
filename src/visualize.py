#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, help="Path to the JSON file output by reduce.py")
parser.add_argument('--key', required=True, help="Key to visualize (e.g., a hashtag or field)")
parser.add_argument('--percent', action='store_true', help="If specified, normalize counts by total")
args = parser.parse_args()

# imports
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# open the input file
with open(args.input_path) as f:
    counts = json.load(f)

# Check if key exists
if args.key not in counts:
    print(f"Key '{args.key}' not found in the file.")
    exit(1)

# normalize the counts by total values if requested
if args.percent:
    # Ensure the normalization denominator exists ('_all') in each case.
    for k in counts[args.key]:
        try:
            counts[args.key][k] /= counts['_all'][k]
        except KeyError:
            print(f"Warning: Key '{k}' not found in '_all'. Skipping normalization for this value.")

# Sort the items in descending order to pick the top 10 (highest counts)
sorted_items = sorted(counts[args.key].items(), key=lambda item: item[1], reverse=True)
top10_items = sorted_items[:10]

# Now sort these top 10 items in ascending order (low to high)
top10_sorted = sorted(top10_items, key=lambda item: item[1])

# Print the results to stdout
for k, v in top10_sorted:
    print(k, ":", v)

# Prepare data for bar plot
keys = [k for k, v in top10_sorted]
values = [v for k, v in top10_sorted]

# Create the bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(keys, values, color='skyblue')
plt.xlabel("Keys")
plt.ylabel("Values")
plt.title(f"Top 10 Keys for '{args.key}' (sorted low to high)")
plt.xticks(rotation=45, ha='right')

# Optional: add the value labels on top of each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.2f}',
             ha='center', va='bottom')

plt.tight_layout()

# Define an output filename based on input file and key (adjust if necessary)
basename = os.path.basename(args.input_path)        # e.g., "combined.lang"
parts = basename.split('.')                          # e.g., ["combined", "lang"]
output_filename = f"{parts[0]}_{parts[1]}_{args.key}.png"

plt.savefig(output_filename)
print(f"Bar graph saved as {output_filename}")

