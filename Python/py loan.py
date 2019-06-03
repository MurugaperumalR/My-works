# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:14:33 2019

@author: Muruga
"""

####import the requried libraies
import numpy as np
import pandas as pd
import os
###set working directories
os.chdir('F:\\python\\case 3 loan')
#import the file
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
#missing values
train_missing = train.isnull().sum()
test_missing = test.isnull().sum()
######impute missing valuesin train
train['Gender'].value_counts()
new_gender = np.where(train['Gender'].isnull(),'Male',train['Gender'])
train['Gender']=new_gender
train['Gender'].isnull().sum()

train['Married'].value_counts()
new_married = np.where(train['Married'].isnull(),'Yes',train['Married'])
train['Married']=new_gender
train['Married'].isnull().sum()

#replace and impute
train['Dependents'].value_counts()
train['Dependents']=train['Dependents'].replace('3+',3)
train['Dependents']=train['Dependents'].replace('0',0)
new_dependents = np.where(train['Dependents'].isnull(),0,train['Dependents'])
train['Dependents']=new_dependents
train['Dependents'].isnull().sum()
train['Dependents']=pd.to_numeric(train['Dependents'])
train['Dependents'].dtypes


train['Self_Employed'].value_counts()
new_selfemployed = np.where(train['Self_Employed'].isnull(),'No',train['Self_Employed'])
train['Self_Employed']=new_selfemployed
train['Self_Employed'].isnull().sum()

train['LoanAmount'].value_counts()
train['LoanAmount'] =np.where(train['LoanAmount'].isnull(),np.nanmedian(train['LoanAmount']),train['LoanAmount'])
train['LoanAmount'].isnull().sum()

train['Loan_Amount_Term'].value_counts()
train['Loan_Amount_Term']=np.where(train['Loan_Amount_Term'].isnull(),'360',train['Loan_Amount_Term'])
train['Loan_Amount_Term'].isnull().sum()

train['Credit_History'].value_counts()
train['Credit_History']=np.where(train['Credit_History'].isnull(),'1.0',train['Credit_History'])
train['Credit_History'].isnull().sum()
checking_missing= train.isnull().sum()
train.to_csv('check.csv')

#encoding the variable####
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
train['Gender']=LE.fit_transform(train['Gender'])
train['Gender'].value_counts()

train['Married']=LE.fit_transform(train['Married'])
train['Married'].value_counts()

train['Married']=LE.fit_transform(train['Married'])
train['Married'].value_counts()

train['Education']=LE.fit_transform(train['Education'])
train['Education'].value_counts()

train['Self_Employed']=LE.fit_transform(train['Self_Employed'])
train['Self_Employed'].value_counts()

train['Property_Area']=LE.fit_transform(train['Property_Area'])
train['Property_Area'].value_counts()

train['Loan_Status']=LE.fit_transform(train['Loan_Status'])
train['Loan_Status'].value_counts()

#########classification logistics###########
Y=train['Loan_Status']
X=train.iloc[:,1:11]
from sklearn.linear_model import LogisticRegression
Log_Reg=LogisticRegression()
Log_Reg.fit(X,Y)
Preds_Log_Reg =Log_Reg.predict(X)
from sklearn.metrics import confusion_matrix
cm_log_reg= confusion_matrix (Y,Preds_Log_Reg)

#############random forest#########################
from sklearn.ensemble import RandomForestClassifier
RF =RandomForestClassifier(n_estimators=500)
RF.fit(X,Y)
preds_RF = RF.predict(X)
cm_RF= confusion_matrix (Y,preds_RF)
#############nb##########################
from sklearn.naive_bayes import GaussianNB
NB=GaussianNB()
NB.fit(X,Y)
preds_NB=NB.predict(X)
cm_NB=  confusion_matrix(Y,preds_NB)
#################################################################

##########test dataset#############################################
#missing values
test_missing = test.isnull().sum()

test['Gender'].value_counts()
new_gender = np.where(test['Gender'].isnull(),'Male',test['Gender'])
test['Gender']=new_gender
test['Gender'].isnull().sum()

test['Married'].value_counts()
new_married = np.where(test['Married'].isnull(),'Yes',test['Married'])
test['Married']=new_gender
test['Married'].isnull().sum()

#replace and impute
test['Dependents'].value_counts()
test['Dependents']=test['Dependents'].replace('3+',3)
test['Dependents']=test['Dependents'].replace('0',0)
new_dependents = np.where(test['Dependents'].isnull(),0,test['Dependents'])
test['Dependents']=new_dependents
test['Dependents'].isnull().sum()
test['Dependents']=pd.to_numeric(test['Dependents'])
test['Dependents'].dtypes

test['Self_Employed'].value_counts()
new_selfemployed = np.where(test['Self_Employed'].isnull(),'No',test['Self_Employed'])
test['Self_Employed']=new_selfemployed
test['Self_Employed'].isnull().sum()

test['LoanAmount'].value_counts()
test['LoanAmount'] =np.where(test['LoanAmount'].isnull(),np.nanmedian(test['LoanAmount']),test['LoanAmount'])
test['LoanAmount'].isnull().sum()

test['Loan_Amount_Term'].value_counts()
test['Loan_Amount_Term']=np.where(test['Loan_Amount_Term'].isnull(),'360',test['Loan_Amount_Term'])
test['Loan_Amount_Term'].isnull().sum()

test['Credit_History'].value_counts()
test['Credit_History']=np.where(test['Credit_History'].isnull(),'1.0',test['Credit_History'])
test['Credit_History'].isnull().sum()
checking_missing= test.isnull().sum()
test.to_csv('check.csv')

#encoding the variable####
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
test['Gender']=LE.fit_transform(test['Gender'])
test['Gender'].value_counts()

test['Married']=LE.fit_transform(test['Married'])
test['Married'].value_counts()

test['Married']=LE.fit_transform(test['Married'])
test['Married'].value_counts()

test['Education']=LE.fit_transform(test['Education'])
test['Education'].value_counts()

test['Self_Employed']=LE.fit_transform(test['Self_Employed'])
test['Self_Employed'].value_counts()

test['Property_Area']=LE.fit_transform(test['Property_Area'])
test['Property_Area'].value_counts()

    
test_data= test.iloc[:,1:11]
test_data['pred_medv']=RF.predict(test_data)










































































