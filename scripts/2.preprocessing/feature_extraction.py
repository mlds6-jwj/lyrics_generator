
#libreria para medir el profanity.

from better_profanity import profanity
import os

import numpy as np
import pandas as pd
from nltk.tokenize import WordPunctTokenizer



def load_emolex(path = "emolex"):
  """
  Método para cargar el emolex, indica la emoción de una palabra (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust)
  y 2 sentimientos (positive. negative)
  """

 #Realizar unzip al archivo emolex
  !unzip emolex.zip
  vocab = {}
  base_path = path


  #Cargar los emolex en un diccionario
  for lexicon in os.listdir(base_path):
    with open(os.path.join(base_path, lexicon)) as f:
      vocab[lexicon.split(".")[0]] = f.read().split("\n")


  #regresar el vocab con los emolex
  return vocab



def count_profanity_sentences(doc):
  """
  Método para identificar la cantidad de groserias dentro de un texto
  """
  doc_prof = [profanity.censor(word) for word in str(doc).split(" ")]
  doc_prof = [word for word in doc_prof if "*" in word]

  return len(doc_prof)


def get_profanity_ratio(df, col):
    """ 
    df -> dataFrame
    col -> Columna con las lyrics
    """

    df["Prof_Count"] = df[col].apply(count_profanity_sentences)
    df["Words"]      = df[col].str.split(" ").apply(len)
    df["Profanity Ratio"] = (df["Prof_Count"] / df["Words"]) * 100
    df.drop(columns = ["Prof_Count", "Words"], inplace = True)
    return df


# Función auxiliar para estimar la distribución de emociones en un texto
def emotion_count(text, vocab):
  """
  Función para estimar la distribuciones de emociones del emolex
  """
  words = WordPunctTokenizer().tokenize(text) #separamos palabras
  counts = {i: 0 for i in list(vocab.keys())}
  for word in words:
      for emo in vocab:
          if word in vocab[emo]:
              counts[emo] += 1
  return counts


def emolex_df(artist, corpus, vocab):
  """
  Dataframe con el % de emociones que se tiene para cada artista, cada columna es un sentimiento

  artist -> listado de artistas
  corpus -> lyrics por artistas
  vocab -> vocabulario con el emolex de palabras y su sentimiento asociado
  """

  #Lista vacia para agregar el conteo de emolexs
  artist_sentiment =[]

  for i in np.unique(artist):
    artist_sentiment.append(emotion_count(" ".join(np.array(corpus)[artist==i]), vocab))

  #Se crea un DataFrame con los valores y se dejan en terminos porcentuales sobre el total de apariciones por artista (normalización)
  artist_sentiment = pd.DataFrame(artist_sentiment)
  artist_sentiment.set_index(np.unique(artist), inplace=True)

  #Dejar en terminos porcentuales el conteo de sentimientos.
  artist_sentiment['Total'] = artist_sentiment.sum(axis=1)

  #iterar en cada columna para obtener el % sobre el total
  for column in artist_sentiment.columns:
    artist_sentiment[f"{column}"] =  (artist_sentiment[f"{column}"] / artist_sentiment['Total'] * 100 )
    
  artist_sentiment.drop(['Total'],axis=1, inplace= True)

  return artist_sentiment

"""
vocab = load_emolex()


artist_songs_df = pd.read_csv("artist_corpus.csv")


artist_songs_df = artist_songs_df[['artist','lyric']]


get_profanity_ratio(artist_songs_df, "lyric")


df_artist_emolex = emolex_df(artist_songs_df['artist'], artist_songs_df['lyric'], vocab)


df_artist_emolex.to_csv("df_features_emolex.csv")
"""

