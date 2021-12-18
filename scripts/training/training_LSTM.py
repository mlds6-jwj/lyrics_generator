
try:
    %tensorflow_version 2.x
    %load_ext tensorboard
except Exception:
    pass
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os, random

from scripts.preprocessing.feature_extraction_LSTM import vectorized_text

tf.random.set_seed(123)
np.random.seed(123)

def load_corpus(path):
  """
  path: Path relativo a este script
  Esta función carga el corpus para su procesamiento y lectura en la red neuronal
  """
  with open(path) as f:
    corpus = f.readlines()
    corpus = ' '.join(corpus)
  return corpus


def split_input_target(chunk):
  input_text = chunk[:-1]
  target_text = chunk[1:]
  return input_text, target_text

def dataset_preparation(text_as_int, len_corpus, seq_length=100, buffer_size = 10000, batch_size = 64):
  examples_per_epoch = len_corpus // (seq_length + 1) 
  char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
  sequences = char_dataset.batch(seq_length+1, drop_remainder=True)
  dataset = sequences.map(split_input_target).shuffle(buffer_size).batch(batch_size, drop_remainder=True)
  return examples_per_epoch, dataset

def train_test_split(dataset):
  test_dataset = dataset.take(int(len(list(dataset))*0.2))
  train_dataset = dataset.skip(int(len(list(dataset))*0.2))
  return (test_dataset, train_dataset)

def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

def model_definition(vocab, embedding_dim = 256, rnn_units = 1024, buffer_size = 10000, batch_size = 64, recurrent_initializer = 'glorot_uniform', dense_dim = 128, activation = "relu", dropout = 0.2):
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

def compile_model(model, optimizer, loss, metrics):
  model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

def fit_model(model, train_dataset, test_dataset, epochs, examples_per_epoch, validation_steps, batch_size=64, saving_path = 'lstm.h5'):
  checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=saving_path,
    save_weights_only=True, save_best_only = True)
  model.fit(train_dataset.repeat(), validation_data = test_dataset.repeat(), epochs=epochs, callbacks=[checkpoint_callback], 
                 steps_per_epoch=examples_per_epoch//batch_size, validation_steps = validation_steps)
  


"""
corpus = load_corpus('corpus.txt')

text_as_int, idx2char = vectorized_text(corpus)

examples_per_epoch, dataset =  dataset_preparation(text_as_int = text_as_int, len_corpus = len(corpus))

test_dataset, train_dataset = train_test_split(dataset)

model = model_definition(vocab = idx2char)

compile_model(model, optimizer = "adam", loss = loss, metrics = 'accuracy')

fit_model(model, train_dataset, test_dataset, 1, examples_per_epoch, validation_steps = 48)
"""



