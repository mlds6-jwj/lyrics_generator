
import os 
import re
import pandas as pd 
import numpy as np


def open_file(path):
  """
  path => str, el path relativo a este documento
  Esta función lee el dataset para su limpieza
  """
  text_file = open(path).read()
  return text_file
def define_artists(data):
  """
  data => archivo de strings
  Esta función define los artistas usados en el minado de canciones
  """
  artists = re.findall("Artist:*.+", data)
  artist_clean = []
  for artist in artists:
    artist_clean.append(re.sub(r'Artist:|[^a-zA-Z0-9-]', "", artist))
  return artist_clean
def lyrics_cleaning(data, special_words=""):
  """
  data = data cruda
  special_words = lista de estribillos dentro de paréntesis, separados por "|", ejemplo: "oh|Oh|yeah"
  Esta función limpia el texto, basándose en el texto de entrada y en estribillos o frases que el cliente desee eliminar
  """
  lyrics = data.split('Artist:') #Separamos la base por la palara Artist, quedando en cada elemento de la lista la letra de una canción completo
  lyrics_prelim = []

  #Limpieza de texto.
  for lyric in lyrics:
    lyrics_prelim.append(re.sub(' +', ' ', #Convierte espacios múltiples en uno solo
                                re.sub(' , ', '', # Elimina las comas solitarias
                                       re.sub(r"|ahah|Ahah|Hey|hey|oh|la-la|sha-ba-da|Shoop-doop-doop|​efil|flaH|yeah|urlcopyembedcopy|\\","", #Elimina estribillos
                                              re.sub(r"endoftext|EmbedShare|URLCopyEmbedCopy|","", #Elimina la etiqueta del final del texto 
                                                     re.sub(r"{sp}".format(sp = special_words), "", # El usuario puede quitar los estribillos que considere
                                                            re.sub(r"[^a-zA-Z\s\.\,\']","", #Reemplaza los saltos de línea entre cada prosa con un espacio en blanco
                                                                   re.sub(r".*,", "", lyric, 1)))))))) #Elimina la etiqueta al principio de cada canción que indica al artista
  return lyrics_prelim[1:]
def data_formatting(artist_list, lyrics_list):
  """
  artist_list => Lista que contiene a todos los cantantes preprocesados con la función define_artists
  lyrics_list => Lista que contiene los lyrics preprocesados con la función lyrics_cleaning
  Outputs: songs_df - Dataframe que corresponde a cada artista con una letra
           artist_corpus - Corpus por artista
           corpus - Corpus total para entrenar la red neuronal
  Esta función crea los outputs para EDA, modelling y training directamente.
  """

  songs_df = pd.DataFrame({'artist':artist_list, 'lyric': lyrics_list}).drop_duplicates()

  artist_corpus = songs_df.groupby(['artist'])['lyric'].apply(' '.join).reset_index()

  corpus = " ".join(lyrics_list)

  return songs_df, artist_corpus, corpus


def data_export(songs_dataframe, path_songs_dataframe, artist_corpus, path_artist_corpus, complete_corpus, path_complete_corpus):
  """
  songs_dataframe=> Dataframe obtenido por el primer argumento de data_formatting
  path_songs_dataframe=> Path relativo para guardar el dataframe a csv
  artist_corpus=> Dataframe obtenido por el segundo argumento de data_formatting
  path_artist_corpus=> Path relativo para guardar el dataframe a csv
  complete_corpus=> texto obtenido por el tercer argumento de data_formatting
  path_complete_corpus=> Path relativo para guardar el string a txt
  Esta función exporta todo lo obtenido en este archivo para hacer el training, modelling y EDA
  """
  songs_dataframe.to_csv(path_songs_dataframe)
  artist_corpus.to_csv(path_artist_corpus)
  with open(path_complete_corpus, "w") as f:
    writer = f.write(complete_corpus)
    

"""
data = open_file(r"lyrics.txt")
artists = define_artists(data)
lyrics_clean = lyrics_cleaning(data)
songs_df, artist_corpus, corpus = data_formatting(artists, lyrics_clean)
data_export(songs_df, 'songs_df.csv', artist_corpus, 'artist_corpus.csv', corpus, 'corpus.txt')
"""

