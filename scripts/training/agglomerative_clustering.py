
import os

import numpy as np
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px 

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from plotly import offline


def open_file(path):
  """
  path : str, el path relativo a este documento
  Esta función lee el dataset para su modelación
  """
  dataset = pd.read_csv(path, index_col=0)
  return dataset

def model_generation(numero_clusters, dataset, normalizar):
  """
  numero_clusters: entero, número de clusters deseados o indicados por model_evaluation a criterio del investigador
  dataset: dataset de pandas, contiene las features definidas, debe tener sólo números
  nombre_columna: str, nombre que se desea poner a la columna que contiene la clasificación del clúster
  Esta función genera el modelo y lo ajusta con respecto al número de clústers deseados, dado un dataset con las features o características deseadas. Así mismo,
  devuelve una tabla de frecuencias de los clusters, y ésta puede normalizarse
  """
  model = AgglomerativeClustering(n_clusters=numero_clusters)
  ypred = model.fit_predict(dataset)
  freq = pd.Series(ypred).value_counts(normalize = normalizar)
  
  return model, ypred, freq

def graph_model(dataset, ypred):
  """
  dataset: dataset de pandas, contiene las features definidas, debe tener sólo números
  ypred: clúster predicho por el modelo
  Esta función genera el gráfico del modelo, éste es tridimensional y generado por plotly. 
  """
  transform_data = pd.DataFrame(TSNE(3, random_state = 2021).fit_transform(dataset), columns=['x','y','z'], index=dataset.index)
  transform_data['Predicted'] = ypred

  fig = px.scatter_3d(transform_data, x='x', y='y', z='z',
                      color='Predicted', hover_name = transform_data.index)
  fig.update_layout(autosize=False,
      width=750,
      height=750)
  fig.show()  

  return transform_data, fig

def export_model(transform_data, path_transform_data, original_data, path_original_data, ypred, fig, path_fig):
  """
  transform_data: Dataframe obtenido por el primer argumento de graph_model
  path_transform_data: Path relativo para guardar el dataframe a csv
  original_data: Dataframe original
  path_original_data: Path relativo para guardar el dataframe a csv
  ypred: Clústeres asignados
  fig: Imagen de plotly para guardar en html
  path_complete_corpus: Path relativo para guardar la imagen
  Esta función exporta todo lo obtenido en este archivo hecho por modelling
  """
  transform_data.to_csv(path_transform_data)
  original_data['Predicted'] = ypred
  original_data.to_csv(path_original_data)
  offline.plot(fig, filename=path_fig)
  
  
  
"""
dataset = open_file('df_features_emolex.csv')

model, ypred, freq = model_generation(5, dataset, True)

transform_data, fig = graph_model(dataset, ypred)

export_model(transform_data, "transformed_data.csv", dataset, "dataset_predicted.csv", ypred, fig, path_fig="fig.html")
"""

