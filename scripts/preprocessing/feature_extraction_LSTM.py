
#Librerias
import pandas as pd
import numpy as np


#Cargar archivo, en .py se puede traer el método de data_cleaning
""""
with open('corpus.txt') as f:
  corpus = f.readlines()

#Corpus se carga como lista, se pasa a un string.
corpus = " ".join(corpus)
"""
def vectorized_text(corpus):
  """
  Se recibe un texto y lo devuelve en una representación númerica.
  """
  
  #Voabulario, caracteres unicos que aparecen en el corpus
  vocab = np.array(sorted(np.unique(list(set(corpus)))))
  #Asignar un valor numerico a cada caracter
  char2idx = {u:i for i, u in enumerate(vocab)}

  text_as_int = np.array([char2idx[c] for c in corpus])

  return text_as_int, vocab

def export_vect_text(text_as_int, path):
  """
  Opcional por si se desea exportar la vectorización 
  """
  text_as_int.tofile(path," ")
  
"""  
corpus_int, vocab_idx = vectorized_text(corpus)
export_vect_text(corpus_int, "vect_corpus.txt")
"""

