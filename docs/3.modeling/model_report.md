# Final Model Report
_Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project_

# Modelo de Clustering

## Analytic Approach 
* Target definition: Deseamos ver cómo se clasifican los artistas usados como insumo para todo el pipeline de ejecución, para que el usuario pueda determinar sí las distribuciones de emociones son acordes con sus necesidades.
* Inputs description: Un dataset qué contiene las distribuciones emocionales de cada uno de los artistas.
* Model type: Agglomerative Clustering.

## Solution Description
* Architecture: Se hizo uso de los datos obtenidos de genius, a partir de la api de desarrolladores.
* Output: Una clasificación por clústeres de los artistas, junto con un gráfico tridimensional para analizar las distancias entre los artistas.

## Data
* Source: Genius.com
* Data Schema: Dataset estructurado con emociones y artistas.
* Sampling: Ninguno, se usa todo el dataset.
* Selection: Se usa completo el dataset.
* Stats: 54 artistas base.

## Features
* Features: Emociones encontradas por medio del diccionario emolex.
* Importance ranking: Todas las emociones tienen las mismas importancias para la clasificación.

## Algorithm
* Description: ![alt text](https://i.imgur.com/zhFzYcS.jpeg)
* Learners: Agglomerative Clustering
* Hyper-parameters: Número de clústeres, lo demás se mantiene constante y por defecto.

## Results
* Inercia de 825, coeficiciente de silueta de 0.23
* ![alt text](https://i.imgur.com/ISXVesp.png)
  ![alt text](https://i.imgur.com/6oWnks3.png)

# Modelo de LSTM para generación de lyrics.

## Analytic Approach 
* Target definition: La idea principal es generar lyrics que tengan sentido para el consumidor final, coherentes y estéticamente apropiados con base en un texto inicial generado. 
* Inputs description: Un corpus previamente limpio y arreglado, pero con signos de puntuación, saltos de línea y gramática correcta.
* Model type: Red multicapa LSTM. 

## Solution Description
* Architecture: Se hizo uso de los datos obtenidos de genius, a partir de la api de desarrolladores.
* Output: Un texto del largo qué el consumidor final especifique, escrito en un archivo de texto crudo en formato .txt.

## Data
* Source: Genius.com
* Data Schema: Texto crudo. Sin estructura.
* Sampling: 20% de todo el dataset.
* Selection: 20% de todo el dataset.
* Stats: Más de 2.5 millones de carácteres, 54x25 canciones en total.

## Features
* Features: Ninguna, se usa el texto crudo.
* Importance ranking: Las capas encontradas por medio de los hiperparámetros fueron suficientes, adicionalmente, el dropout resultó siendo determinante para alcanzar los resultados del modelo actual. 

## Algorithm
* Description: ![alt text](https://i.imgur.com/wDScpQi.jpeg)
* Learners: LSTM, red neuronal multicapa. ![alt text](https://i.imgur.com/gExYgkn.png)
* Hyper-parameters: Son los parámetros por defecto para el entrenamiento del modelo inicial

    * Embedding Dimension = 256
    * RNN Units = 1024
    * Buffer Size = 10000
    * Batch Size = 64
    * Recurrent Initializer = 'glorot_uniform'
    * Activation = 'relu' 
    * Dropout = 0.2

## Results
* **Accuracy en training** de **81.88%**, **Loss en training** de **0.5970**. **Accuracy en validación** de **85.32%**, **Loss en validación** de **0.4988**.
