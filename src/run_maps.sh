#!/bin/bash

for input_file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    echo "Starting map.py on $input_file"
    nohup python src/map.py --input_path="$input_file" &

done

echo "All map.py jobs have started"
    
