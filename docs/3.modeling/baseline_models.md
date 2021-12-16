# Baseline Model Report

## Analytic Approach
* Para el modelo de clusterización, no tenemos un target como tal. Para el ***modelo de generación de lyrics***, lo ideal es tener un valor de **loss** bajo y un **accuracy** alto para validación.
* Para el modelo de clusterización, será un dataset donde se contienen los valores normalizados de los sentimientos asociados a los artistas por medio del mapeo de emolex. Para el ***modelo de generación de lyrics***, el dataset es un corpus de texto con una representación vectorizada.
* Para el modelo de clusterización, se hizo uso de **Agglomerative Clustering**, donde se encontró el mejor cluster por medio de **inercia** y por medio del **coeficiente de silueta**. Además, para el **modelo de generación de lyrics**, se entrenó un **LSTM multicapa**. 

## Model Description

* Clusterización por Agglomerative Clustering

	* ![alt text](https://i.imgur.com/zhFzYcS.jpeg)
	* Para la medida de propagación usaremos una **distancia euclídeana**, un criterio de **conexiones de tipo Ward** que minimza la varianza de los clústeres juntados
	* El hiperparámetro para este modelo es el **número de clústers** a usar. 

* LSTM para generación de Lyrics

	* ![alt text](https://i.imgur.com/wDScpQi.jpeg)
	  ![alt text](https://i.imgur.com/gExYgkn.png)
	* El **optimizador** usado fue el **Adam**, mientras que para la **métrica** se utilizó **accuracy**. 
	* Embedding, número de unidades de RNN, dropout, activación de la capa densa posterior a la capa LSTM.

## Resultados (Model Performance Agglomerative Clustering)
* **Coeficiente de silueta** maximizado en **n = 3**, pero por practicidad y dada la cantidad de artistas, escogemos **n = 5 con valor de 0.245**. La **inercia** cambio de variación en **n = 3**, al igual que en **n = 5**. 
* ![alt text](https://i.imgur.com/ISXVesp.png)
  ![alt text](https://i.imgur.com/6oWnks3.png)

## Resultados (Model Performance LSTM)
* **Accuracy en training** de **81.88%**, **Loss en training** de **0.5970**. **Accuracy en validación** de **85.32%**, **Loss en validación** de **0.4988**.


## Entendimiento del modelo (Agglomerative Clustering)

* El modelo agrupa directamente *artistas que comparten sentimientos similares en sus letras*. A pesar de que existen algunos outliers con valores extremos, esto no afecta la clasificación general del modelo en cuanto a lo que se puede presentar al cliente.

## Entendimiento del modelo (LSTM)

* El ***modelo genera lyrics*** automáticamente basándose en las palabras qué se le den inicialmente, y dado un factor de temperatura, permitirá tener párrafos más cortos o más largos según lo deseado por el usuario. 

## Conclusion y discusión Agglomerative Clustering

* ***El modelo es viable*** para implementación posterior.
* **Profanity score** para medir qué tan relacionado está un sentimiento negativo o positivo con un conteo mayor o menor de palabras consideradas ofensivas en las letras de las canciones y permitir un mejor ajuste de cada uno de los subgrupos o clústers generados.
* El ritmo de la música, sí es posible codificar la velocidad, el tono y la fuerza de las canciones para ***ajustar mejor las preferencias de los usuarios***.

## Conclusion y discusión LSTM

* ***El modelo es viable*** para implementación posterior.
* ***El modelo no parece estar sufriendo de overfitting*** dado que en el dataset de validación encontrábamos mejores estadísticos indicadores qué no daban evidencia de este fenómeno para este conjunto de datos y esta configuración de pesos y estructura del modelo.
* Rimas de las canciones, una capa que se encargue de identificar sinónimos y usarlos pragmáticamente.
* Género, medición de popularidad y medición a nivel de canción para identificar lo más popular y trendy.
