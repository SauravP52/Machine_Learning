#-----------------KNN.py----------------------------------#
#                                                         #
#      Implementation of KNN Neighbors using Skikit- Learn$
#                                                         #
#---------------------------------------------------------#
"""
Here we are using sklearn and mathplotlib library
These can be downloaded using the command line code:-

$~ pip install scikit-learn mathplotlib numpy

"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

"""
$ Under the KNeighboursClassifier is a class which exist under the sklearn.neighbors module
we are going to use the KNeighbours Classifier algorithm to predict the outcome of our first 
machine learning model 

We will first load the iris dataset into a variable and then split our dataset into training and test dataset using
the train_test_split function which exist inside the model_selection module 

"""
#Argument of n_neighbors has been set to 1 this is the value of K in the Algorithm
#you can set this as whatever pleases you

knn= KNeighborsClassifier(n_neighbors=1)
iris=load_iris()
X_train, X_test ,y_train, y_test = train_test_split(iris['data'],iris['target'],random_state=0)
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))

""""
========================================
$ The code that follows is only a representation of the plot of the different features of the iris dataset
you can omit this part as it has no link to the training model of our Machine Learning Hypothesis
However it is highly recommended that you visualize the dataset by ploting it on the graph



For more help type help(plt)
========================================
"""
fig, ax = plt.subplots(3, 3, figsize=(15, 15))
plt.suptitle("iris_pairplot")
for c in range(1):
    for i in range(3):
        	for j in range(3):
            		ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=60)
            		ax[i, j].set_xticks(())
            		ax[i, j].set_yticks(())
            		if i == 2:
                		ax[i, j].set_xlabel(iris['feature_names'][j])
            		if j == 0:
                		ax[i, j].set_ylabel(iris['feature_names'][i + 1])
            		if j > i:
                		ax[i, j].set_visible(False)
plt.show()

