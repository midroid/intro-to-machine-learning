# Naive Base
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("mislead %d: %d"
    % (iris.data.shape[0], (iris.target != y_pred).sum()))
    
    
# SVM - Support Vector Machine
from sklearn import svm
X = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[2., 2.]]))

#kernel trick - multidimensinoal to make it linear separable

# Decision Trees
from sklearn import tree
X = [[0,0], [1,1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
print(clf.predict([[2. , 2.]]))
print(clf.predict_proba([[2., 2.]]))

#K nearest neighbours

#adaboost

#random forest

from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
clf = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = clf.kneighbors(X)
print(indices)
print(distances)

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 3)
neigh.fit(X, y)
print(neigh.predict([1.1]))
print(neigh.predict_proba([[0.9]]))