# Twitter Coronavirus Analysis

This project processes a large Twitter dataset to capture tweet counts related to COVID-19 hashtags across different languages and countries. Using MapReduce techniques, multiple stages of data aggregation were performed:

1. **Mapping (`map.py`):**  
   This script reads input zipfiles containing Twitter data, extracts tweet metadata, and tallies counts for selected hashtags by language and country.

2. **Reducing (`reduce.py`):**  
   The reduce phase merges individual mapping outputs into two consolidated JSON files (`combined.lang` and `combined.country`), aggregating tweet counts per hashtag for languages and countries.

3. **Visualization (`visualize.py`):**  
   Visualization scripts were used to generate bar graphs for the top 10 key counts (e.g., `#coronavirus` and `#코로나바이러스`), producing the following images:
   - `combined_lang_#coronavirus.png`
   - `combined_country_#coronavirus.png`
   - `combined_lang_#코로나바이러스.png`
   - `combined_country_#코로나바이러스.png`
   
4. **Alternative Reduce (`alternative_reduce.py`):**  
   This script constructs a line plot that shows daily tweet counts over the year for specified hashtags, aggregating mapping outputs on a per-day basis.

These visualizations provide insights into the geographic and linguistic trends in COVID-19 related tweets, which can be valuable in understanding public health communications on social media. 

