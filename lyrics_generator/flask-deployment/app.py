import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os, random
import re

tf.random.set_seed(123)
np.random.seed(123)


def load_corpus(path):
  """
  path: Path relativo a este script
  Esta función carga el corpus para su procesamiento y lectura en la red neuronal
  """
  with open(path, encoding="utf8") as f:
    corpus = f.readlines()
    corpus = ' '.join(corpus)
  return corpus


def model_definition(vocab, embedding_dim = 256, rnn_units = 1024, buffer_size = 10000, batch_size = 64, recurrent_initializer = 'glorot_uniform', dense_dim = 128, activation = "relu", dropout = 0.2):
  """
  Definición del modelo LSTM que incluye una capa de embedding, la capa LSTM, 2 capas densas y un Dropout
  """
  model = tf.keras.Sequential([tf.keras.layers.Embedding(len(vocab), embedding_dim,
                                                            batch_input_shape=[batch_size, None]),
                                  tf.keras.layers.LSTM(rnn_units,
                                                       return_sequences=True, #este argumento hace que el modelo sea many-to-many
                                                       stateful=True,
                                                       recurrent_initializer = recurrent_initializer),
                                  tf.keras.layers.Dense(dense_dim,
                                                        activation="relu"),
                                  tf.keras.layers.Dropout(dropout),
                                  tf.keras.layers.Dense(len(vocab))])
  return model

def generate_text(model, start_string, vocab, text_len=500, temperature=0.5):

    """
    Función que genera texto de manera automática a partir de predecir el siguiente caracter mas probable
    recibe como input el modelo, un texto plano, un vocabulario y una temperatura para ajustar el resultado.
    """


    # vectorizamos el string inicial
    char2idx = {u:i for i, u in enumerate(vocab)}
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # Lista para guardar los resultados
    text_generated = []

    # Reiniciamos los estados del modelo
    model.reset_states()
    # iteramos para obtener el número de carácteres deseado
    for i in range(text_len):
        # obtenemos las predicciones
        predictions = model(input_eval)
        # removemos el eje de los batch
        predictions = tf.squeeze(predictions, 0)

        # utilizamos la distribución categorica para obtener el siguiente caracter
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
        # predicted_id es el caracter predicho (este será la entrada en la siguiente iteración)
        input_eval = tf.expand_dims([predicted_id], 0)
        # agregamos el string correspondiente al id predicho
        text_generated.append(idx2char[predicted_id])
    return (start_string + ''.join(text_generated))

def define_predictor():
    idx2char = load_corpus('idx2char.txt').split("|")
    model_lstm = model_definition(vocab = idx2char, batch_size= 1)
    model_lstm.load_weights("lstm.h5")
    return model_lstm, idx2char

model_lstm, idx2char = define_predictor()


# Diccionario donde se guardarán los léxicos.
vocab = {}
base_path = "emolex"
# Iteramos para cada una de las emociones de EmoLex.
for lexicon in os.listdir(base_path):
    # Se abre cada .txt, se extraen todas las palabras y se eliminan saltos de línea.
    with open(
            os.path.join(base_path, lexicon)
            ) as f:
        vocab[
                lexicon.split(".")[0]
                ] = f.read().split("\n")




def emotion_count(text, vocab):
    # Separamos las palabras por espacios.
    words = text.split(" ")
    # Creamos un diccionario donde se guardarán los conteos por cada emoción.
    counts = {i: 0 for i in list(vocab.keys())}
    # Creamos un diccionario donde se guardarán las palabras coincidentes con cada léxico.
    words_per_emo = {i: [] for i in list(vocab.keys())}
    # Iteramos para cada una de las palabras dentro del texto.
    for word in words:
        # Iteramos para cada una de las emociones del léxico.
        for emo in vocab:
            # Evaluamos si la palabra está dentro del léxico de cada emoción
            if word in vocab[emo]:
                # Si la palabra está en el léxico de determinada emoción, sumamos 1 al conteo acumulado.
                counts[emo] += 1
                # También agregamos la palabra coincidente.
                words_per_emo[emo].append(word)
    return counts, words_per_emo


def plot_distribution(counts):
  fig,ax = plt.subplots(1, 1, figsize=(15, 10))
  rect = ax.bar(counts.keys(), counts.values())
  ax.set_xlabel("Emotion")
  ax.set_ylabel("Number of words")
  ax.set_title("Emotions distribution (acording to Emolex)")

  def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%d' % int(height),
                ha='center', va='bottom')
  autolabel(rect)
  plt.close(fig)
  plt.show()
  return fig

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
import re
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('english')

from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()

def freq_words(text_input, stopwords=stopwords, tokenizer=tokenizer):
  text_input = re.sub(r'[^\w]', ' ', text_input)
  text_input = text_input.strip()
    
  tokens = tokenizer.tokenize(text_input)
  final = [''.join(ele) for ele in tokens]
  final = [word for word in final if len(word) > 3]

  freq_dist = nltk.FreqDist(final)
  most_common = pd.DataFrame(freq_dist.most_common()[:20], columns = ["Word", "Conteo"])
  y = most_common["Conteo"]
  x = most_common["Word"]
  return x,y


def plot_words(x,y):
  fig,ax = plt.subplots(1, 1, figsize=(15, 10))
  rect = ax.bar(x, y, color = "red")
  ax.set_xlabel("Word in lyrics")
  ax.set_ylabel("Number of words")
  ax.set_title("Word count in predicted lyrics")

  def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%d' % int(height),
                ha='center', va='bottom')
  autolabel(rect)
  plt.close(fig)
  plt.show()
  return fig


# import Flask 
from flask import Flask, request, render_template

# create an instance of Flask
app = Flask(__name__)

# create a route
@app.route('/')
def home():
    return render_template('index.html')


import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure

# generate prediction
@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.form.to_dict()

    input_start_string = to_predict_list['review_text']
    input_text_length = int(to_predict_list['length'])

    prediction = generate_text(model = model_lstm, start_string = input_start_string, vocab = idx2char, text_len = input_text_length, temperature = 0.65)

    counts, _ = emotion_count(prediction, vocab)
    fig = plot_distribution(counts)
    fig.savefig("static/images/count.png")

    x,y = freq_words(prediction, stopwords=stopwords)
    fig_count = plot_words(x,y)
    fig_count.savefig("static/images/count2.png")

    return render_template('predict.html', 
                          prediction = prediction)

# run the app
if __name__=="__main__":
    app.run(debug=True, host='localhost', port=5000)