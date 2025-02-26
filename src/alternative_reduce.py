#!/usr/bin/env python3
import argparse
import os
import json
import glob
import re
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# Set up the command-line arguments.
parser = argparse.ArgumentParser(
    description="Alternative Reduce: Plot daily tweet counts for specified hashtags")
parser.add_argument('--input_folder', required=True,
                    help="Folder containing mapping output files (e.g. outputs folder)")
parser.add_argument('--hashtags', nargs='+', required=True,
                    help="List of hashtags to plot (e.g. \"#coronavirus\" \"#코로나바이러스\")")
parser.add_argument('--output_path', required=True,
                    help="Path to store the output line plot (PNG file)")
args = parser.parse_args()

# Initialize a structure to hold our data.
# For each hashtag, we will have: day_of_year -> tweet count
hashtag_daily_counts = {hashtag: defaultdict(int) for hashtag in args.hashtags}

# We'll use only one set of mapping output files (e.g. the .lang files) for tweet counts.
# Adjust the pattern if you want to use the .country files too.
file_pattern = os.path.join(args.input_folder, "*.lang")
input_files = glob.glob(file_pattern)

# Regex to extract the date string from file names.
# Assumes file names contain a pattern like: 20-01-01 (two-digit year, month, day)
date_regex = re.compile(r'(\d{2}-\d{2}-\d{2})')

# Process each file.
for file in input_files:
    basename = os.path.basename(file)
    # Try to extract the date string from the filename.
    date_match = date_regex.search(basename)
    if not date_match:
        # Skip if no date pattern is found.
        continue

    date_str = date_match.group(1)   # e.g., "20-01-01"
    # To convert to a datetime object, we assume the year is 20XX.
    try:
        dt = datetime.datetime.strptime("20" + date_str, "%Y-%m-%d")
    except ValueError as e:
        print(f"Skipping {file} due to date conversion error: {e}")
        continue

    day_of_year = dt.timetuple().tm_yday

    # Load the file.
    try:
        with open(file) as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading {file}: {e}")
        continue

    # For each hashtag of interest, update counts.
    # data is expected to be a dictionary with keys for each hashtag.
    for hashtag in args.hashtags:
        # If the hashtag is found in the file, sum up its counter values.
        if hashtag in data:
            count = sum(data[hashtag].values())
        else:
            count = 0
        # Save the count for the day.
        hashtag_daily_counts[hashtag][day_of_year] += count

# Now prepare our plot.
plt.figure(figsize=(12, 8))

# For each hashtag, sort the days and get consistent lists.
for hashtag, day_counts in hashtag_daily_counts.items():
    # Sort days for which we have data; if a day is missing, it is simply omitted.
    days = sorted(day_counts.keys())
    counts = [day_counts[d] for d in days]
    plt.plot(days, counts, marker='o', label=hashtag)

plt.xlabel("Day of the Year")
plt.ylabel("Tweet Counts")
plt.title("Daily Tweet Counts for Selected Hashtags")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure.
plt.savefig(args.output_path)
print(f"Line plot saved as {args.output_path}")

