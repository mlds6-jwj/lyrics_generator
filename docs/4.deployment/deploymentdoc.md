# Deployment

In order to deploy our model, we decided to use Flask with Python. The deployment mean the client access the model throught a website we create and they put their lyrics to be predicted and the desired length. Then, they get back their prediction of lyrics and two graphs related to the prediction.

This is how the input is introduced:

![Input](https://i.imgur.com/pXBDFLT.png)

The person can write whatever they want to predict and an integer, which is the length of the desired lyrics (usually no more than 1.5k words).

The output generated is in text, formatted as usual:

![Output 1](https://i.imgur.com/vNZuFX3.png)

Besides, they get two graphs, which allow them to understand the basic structure of the generated lyrics:

![Output 2](https://i.imgur.com/5gULGLi.png)

Finally, a screenshot of the Flask app script is provided here:

![Flask implementation](https://i.imgur.com/pe59Ti9.png)