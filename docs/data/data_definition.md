# Data and Feature Definitions

The model uses text data from a website, which allow us to mine up to top 25 songs lyrics of rock artists. This data is processed to be explored and used as input in our text model.

The database consists of two basic columns: "artists" and "lyrics". The "artists" column is a list of artists that are available in this website. The "lyrics" column is a list of artist songs lyrics, and are maximum 25 for each artist.

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Lyrics | Lyrics mined from Genius.com | lyrics_generator/scripts/data_acquisition | [data_acquisition_POO.ipynb](https://github.com/mlds6-jwj/lyrics_generator/blob/Dev/scripts/data_acquisition/data_acquisition_POO.ipynb) | [eda_lyrics.ipynb](https://github.com/mlds6-jwj/lyrics_generator/scripts/eda/eda_lyrics.ipynb)|

* Lyrics summary: <Collection of songs by each artist, containing 25 lyrics for each one. The data_acquisition.py file provides the method to get the data and the eda_lyrics provides an exploratory data analysis of the dataset.>

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset | [Dataset](link/to/dataset1/report) | [data_cleaning_poo.ipynb](https://github.com/mlds6-jwj/lyrics_generator/scripts/preprocessing/data_acquisition_POO.ipynb) | [data_cleaning_poo.ipynb](https://github.com/mlds6-jwj/lyrics_generator/scripts/preprocessing/data_acquisition_POO.ipynb) |
* Processed Data summary: <The lyrics dataset was processed using typical transformations such as lower case, only alphanumeric strings, tokenizing and lemmatizing.>

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set | [Dataset](link/to/dataset1/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
