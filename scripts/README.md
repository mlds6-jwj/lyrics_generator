# README scripts folder

En esta carpeta, tenemos las siguientes subcarpetas con cada uno de los contenidos especificados:
* data_acquisition: 
    * data_acquisition_LyricGeniusAPU.py: El minado de datos por parte de la API de Genius.
* eda:
    * eda_lyrics.ipynb: Análisis exploratorio preliminar de los datos y los artistas.
* evaluation:
    * model_evaluation_agg_clus.py: Generación de coeficientes de silueta e inercia para el modelo de clústering.
* preprocessing:
    * data_cleaning.py: Limpieza preliminar de los datos, sus outputs son usados en feature extraction para cada uno de los modelos.
    * feature_extraction_LSTM.py: Representación numérica para cada uno de los carácteres en el texto, posteriormente usado como input para el entrenamiento de la red neuronal. 
    * feature_extracion.py: Genera la distribución de emociones para cada uno de los artistas, posteriormente usado como input para el entrenamiento del modelo de clusterización. 
* training:
    * agglomerative_clustering.py: Entrenamiento del modelo de clustering.
    * training_LSTM: Entrenamiento del modelo de LSTM. 
