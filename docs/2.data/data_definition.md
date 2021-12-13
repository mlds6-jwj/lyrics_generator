# Data and Feature Definitions

The model uses text data from a website (**genius.com**), which allow us to mine up to top 25 songs lyrics of rock artists. This data is processed to be explored and used as input in our text model.

The database consists of two basic columns: **artists** and **lyrics**. The **artists** column is a list of artists that are available in this website. The **lyrics** column is a list of artist songs lyrics, and are maximum 25 for each artist.

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Lyrics | Lyrics mined from **genius.com** | lyrics_generator/scripts/data_acquisition | [data_acquisition_POO.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/scripts/data_acquisition/data_acquisition_POO.ipynb) | [eda_lyrics.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/main/scripts/eda/eda_lyrics.ipynb)|

* **Lyrics summary:** Collection of songs by each artist, containing **25 lyrics** for each one. The ***data_acquisition.py*** file provides the method to get the data and the ***eda_lyrics.py*** provides an exploratory data analysis of the dataset.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset | [Dataset](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/lyricsgenius/database/lyrics.txt) | [data_cleaning_poo.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/scripts/preprocessing/data_cleaning_poo.ipynb) | [data_cleaning_poo.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/scripts/preprocessing/data_cleaning_poo.ipynb) |
* **Processed Data summary:** The lyrics dataset was processed using typical transformations such as lower case, only alphanumeric strings, tokenizing and lemmatizing.

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set | [Dataset](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/lyricsgenius/database/data_preprocessed/artist_corpus.csv) | [Dataset_preprocessed](link/to/R/script/file/in/Code) | [Feature_extraction.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/scripts/preprocessing/Feature_extraction.ipynb)|

* **Feature Set summary.** The lyrics dataset was processed using typical transformations such as lower case, only alphanumeric strings, tokenizing and lemmatizing. Then, we perform a feature extraction procedure using Agglomerative Clustering.
