import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#import the data. Iris flower data set
iris_dataset = load_iris() #this is an object
#the above object is a Bunch object, similar to dictionary,
#has keys and values

########## let's look at the data #################

print("Keys of iris dataset: \n{}".format(iris_dataset.keys()))

'''Gives:
dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
'''

print(iris_dataset['DESCR'][:193] + "\n...")
#gives data set characteristics

#value of the key target_names is an array of strings,
#containing the species of the flower we want to predict:
print("Target names: {}".format(iris_dataset['target_names']))
'''
Target names: ['setosa' 'versicolor' 'virginica']
'''

#value of feature_name is a list of string, with descpription of each feature
print("Feature names: {}".format(iris_dataset['feature_names']))
'''
Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
'''

#data itself is contained in the target and data fields
#contains the numeric measurements of the above, in a NumPy array
print("Type of data: {}".format(type(iris_dataset['data'])))

print("Shape of data: {}".format(iris_dataset['data'].shape))
'''
Shape of data: (150, 4)
'''
#this means there are 150 rows (measurements for 150 different flowers) (samples)
#and 4 columns: each of the measured features

print("First 5 rows of data:\n{}".format(iris_dataset['data'][:5]))

#the target array contains the species of each of the flowers that were measured
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))
#from this we can see that it is a 1D array with one entry per flower

print("Target:\n{}".format(iris_dataset['target']))
#from this we can see that they are encoded as 0, 1 or 2:
#0 means setosa, 1 means versicolor, 2 means virginica
#(given by the iris[target_names] array)

#############Training and Testing data########################
#we will show the model we make 'new' data (i.e. data that it hasn't seen before)
#by splitting our model into training and testing data
#scikit-learn contains a function that shuffles and splits for you:

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

#data denoted by uppercase X with labels as y (from mathematics, a matrix and a vector)
#using random_state=0 makes the shuffle deterministic, so we always get the same output
#X_train contains 75% of the rows of the dataset, and X_test contains the remaining 25%

print("X_train shape: {}".format(X_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_train shape: {}".format(y_train.shape))
print("y_test shape: {}".format(y_test.shape))

#################visualize the data: pair plot ############
#as we have 4 features, this is reasonable here:
#to create the plot we first convert the numpy array into a pandas dataframe
#as pandas has a function to create pair plots (scatter_matrix)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o',
                            hist_kwds={'bins':20}, s=60, alpha=0.8)
plt.show()
