# Data and Feature Definitions

The model uses text data from **[genius.com](genius.com)** website, which allow us to mine up to top 25 songs lyrics of rock artists. This data is processed to be explored and used as input in our text model.

The database consists of two basic columns: **artists** and **lyrics**. The **artists** column is a list of artists that are available in this website. The **lyrics** column is a list of artist songs lyrics, and are maximum 25 for each artist.

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| lyrics.txt | Lyrics mined from **genius.com** | /lyrics_generator/lyricsgenius/database/ | [data_acquisition_LyricGeniusAPI.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/data_acquisition/data_acquisition_LyricGeniusAPI.py) | [eda_lyrics.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/eda/eda_lyrics.ipynb)|

* **Lyrics summary:** Collection of songs by each artist, containing **25 lyrics** for each one. The ***data_acquisition_LyricGeniusAPI.py*** file provides the method to get the data and the ***eda_lyrics.ipynb*** provides an exploratory data analysis of the dataset.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| songs_df.csv | lyrics.txt | [data_cleaning.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/data_cleaning.py) | [data_cleaning_poo.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/data_cleaning_poo.py) |
| corpus.txt | lyrics.txt | [data_cleaning.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/data_cleaning.py) | [data_cleaning_poo.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/data_cleaning_poo.py) |
* **Processed Data summary:** The lyrics dataset was processed using typical transformations such as lower case, only alphanumeric strings, tokenizing and lemmatizing.

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| artist_corpus.csv | lyrics.txt | [Feature_extraction.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/Feature_extraction.py) | [Feature_extraction.py](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/preprocessing/Feature_extraction.py)|

* **Feature Set summary.** The lyrics dataset was processed using typical transformations such as lower case, only alphanumeric strings, tokenizing and lemmatizing. Then, we perform a feature extraction procedure using Agglomerative Clustering.
