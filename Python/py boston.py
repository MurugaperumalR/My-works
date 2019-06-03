# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:30:37 2019

@author: Muruga
"""
####import the requried libraies
import numpy as np
import pandas as pd
import os
###set working directories
os.chdir('F:\\python\\case 4 baston')
#import the file
train=pd.read_csv('train.csv')

#missing values
train['ID'].isna().value_counts()

train.isna().sum()
summary= train.describe()
train.head(10)
train.tail(10)
train['nox'].mean()
train['nox'].sum()
train['nox'].median()

tra_arr=np.array(train)
train.skew()
train['chas'].value_counts()

train['log_crim']= np.log(train['crim'])

train['scale_crim']=(((train['crim'])-np.mean(train['crim'])/np.std(train['crim'])))


def standared_scalar(var):
    mean=np.mean(var)
    std= np.std(var)
    scale_var =(var-mean)/std
    return scale_var

train_scale= standared_scalar(train)


corr_matrix =np.corrcoef(train['crim'],train['tax'])
corr_matrix_pd=train.corr()

#divide the data into x and y
Y= train['medv']
X= train.iloc[:,1:14]

#analysis sklearn modeling process
 from sklearn.linear_model import LinearRegression
 LR = LinearRegression()
 LR.fit(X,Y)
 LR.coef_
LR.intercept_
Preds_LR= LR.predict(X)
from sklearn.metrics import mean_squared_error
mse_lr = mean_squared_error (Y,Preds_LR)
print(mse_lr)
rmse_lr = np.sqrt(mse_lr)
print(rmse_lr)
#########################################################################

from sklearn.ensemble import RandomForestRegressor
RF =RandomForestRegressor(n_estimators=500)
RF.fit(X,Y)
preds_RF = RF.predict(X)
rmse_RF =np.sqrt(mean_squared_error(Y,preds_RF))
print (rmse_RF)
#########################################################################

from sklearn import svm
svm_RF=svm.SVR()
svm_RF.fit(X,Y)
preds_svm= svm_RF.predict(X)
rmse_svm =np.sqrt(mean_squared_error(Y,preds_svm))
print (rmse_svm)
#######################################################################


test=pd.read_csv('test.csv')
#######predict y for test data###############
test_data= test.iloc[:,1:14]
test_data['pred_medv']=RF.predict(test_data)
####### write the output in csv file##########
test_data.to_csv('output.csv')
#######################################################################






























































