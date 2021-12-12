# Data Dictionary

En este proyecto se utiliza un dataset que contiene esencialmente dos columnas, artista y lyrics. Para ello, tenemos 4 archivos principales que se usan a lo largo de todo el proyecto.

# Lyrics.txt

Es el dataset crudo que es minado de Genius.com por parte del script de minado. Para ser usado, se utiliza el script de preprocesado que nos retorna 3 outputs principales, descritos a continuación

### artist_corpus.csv

El dataset es un corpus completo con todas las canciones de cada uno de los artistas, donde cada registro es un artista único con el corpus completo de todo su repertorio musical. 

| columna | tipo | descripción |
| --- | --- | --- |
| artist | STR | Nombre del artista |
| lyrics  | STR | Todas las canciones del artista unidas en un solo corpus |

## songs_df.csv

El dataset es similar, salvo que cada registro es una canción única del artista y permite el análisis preliminar del script de EDA. 

| columna | tipo | descripción |
| --- | --- | --- |
| artist | STR | Nombre del artista |
| lyrics  | STR | Todas las canciones del artista, separadas en registros únicos por canción |

## corpus.txt

Es un archivo de texto sin estructura de dataset que contiene todas las canciones de todos los artistas, usado para el entrenamiento y ajuste del modelo de redes neuronales LSTM para la generación de lyrics.