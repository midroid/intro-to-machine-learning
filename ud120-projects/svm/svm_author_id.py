#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
clf = svm.SVC(kernel="rbf", C=10000.0)
t0 = time()
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
#pred10 = clf.predict(features_test[10])
#pred26 = clf.predict(features_test[26])
#pred50 = clf.predict(features_test[50])
print("svm training time: ", round(time()-t0, 3))
print(accuracy_score(labels_test, pred))
#print(pred)
#print(pred10, pred26, pred50)
def occurences(tokens,words):
    count = 0
    for result in words:
        if (result == tokens):
            count += 1
    return count
print(occurences(1, pred))
#########################################################


