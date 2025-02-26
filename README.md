# Twitter Coronavirus Analysis

This project processes a large Twitter dataset to capture tweet counts related to COVID-19 hashtags across different languages and countries. The following images summarize the results:

### Bar Graphs
- **Language Data for #coronavirus:**  
<img src='combined_lang_coronavirus.png' width=100% />


- **Country Data for #coronavirus:**  
<img src='combined_country_coronavirus.png' width=100% />

- **Language Data for #코로나바이러스:**  
<img src='combined_lang_코로나바이러스.png' width=100% />

- **Country Data for #코로나바이러스:**  
<img src='combined_country_코로나바이러스.png' width=100% />

### Alternative Reduce Plot

The alternative reduce script generated a line plot that shows the daily tweet counts for selected hashtags over the course of a year. This plot can be found below:

<img src='alt_reduce.png' width=100%     />

## How to Run the Project

### Prerequisites

- Python 3 installed
- A virtual environment set up with the required libraries (e.g., matplotlib)
- The dataset zip files (e.g., located in `/data/Twitter dataset/`)
- Git for version control

### Step 1: Mapping Stage

To process the input Twitter dataset files, run the `map.py` script. This script extracts tweet counts for selected hashtags and outputs JSON files into the `outputs/` folder.

For example, to process all zip files:

```bash
cd your-project-directory
bash src/run_maps.sh
```

### Step 2: Reducing Stage
After the mapping phase is complete, combine the output files using the reduce.py script. This will generate two combined files: one for language counts and another for country counts.

Example command:
```bash
python3 src/reduce.py --input_paths outputs/* --lang_output_path combined.lang --country_output_path combined.country
```

### Step 3: Visualization with Bar Graphs
Generate bar graphs for specific hashtags by running the `visualize.py` script. For example, to create bar graphs for `#coronavirus` and `#코로나바이러스` for both language and country data:
```bash
python3 src/visualize.py --input_path combined.lang --key "#coronavirus"
python3 src/visualize.py --input_path combined.country --key "#coronavirus"
python3 src/visualize.py --input_path combined.lang --key "#코로나바이러스"
python3 src/visualize.py --input_path combined.country --key "#코로나바이러스"
```
These commands will produce images such as `combined_lang_coronavirus.png`, etc. (If you've renamed them to replace special characters, adjust the image names accordingly.)

### Step 4: Alternative Reduction and Line Plot
To generate a line plot showing daily tweet counts for selected hashtags, run `alternative_reduce.py`:
```bash
python3 src/alternative_reduce.py --input_folder outputs --hashtags "#coronavirus" "#코로나바이러스" --output_path alt_reduce.png

```
This command will scan through the mapping outputs, aggregate the data per day, and produce a line plot saved as `alt_reduce.png`.

```markdown

