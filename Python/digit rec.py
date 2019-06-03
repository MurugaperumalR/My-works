####import the requried libraies
import numpy as np
import pandas as pd
import os
###set working directories
os.chdir('F:\\python\\digit recognizer')
#import the file
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

######in pixles there will not be a missing values######

train.isnull().sum()
####set X AND Y ##################
Y =train['label']
X= train.iloc[:,1:]

#######spliting the data##########
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2,random_state=42)###will make constant split of 20%##

from sklearn.neural_network import MLPClassifier
MLP=MLPClassifier(hidden_layer_sizes=(50,50,50),solver='adam',verbose=True,max_iter=300)
MLP.fit(X_train,Y_train)

Y_preds_train_MLP=MLP.predict(X_train)
Y_preds_test_MLP=MLP.predict(X_test)

from sklearn.metrics import confusion_matrix
co_MLP_train=confusion_matrix(Y_train,Y_preds_train_MLP)
co_MLP_test=confusion_matrix(Y_test,Y_preds_test_MLP)

#########test###############
preds_test=MLP.predict(test)
preds_test=pd.DataFrame(preds_test)
preds_test.to_csv('output.csv')
