# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:43:47 2019

@author: Muruga
"""

####importing thr requried libraries
import numpy as np
import pandas as pd
import os
######setting working directory
os.chdir("F:\\python\\attrition project")
####import the file
data=pd.read_csv("data.csv")
###missing values
data_missing = data.isnull().sum()
####no missing values
summary= data.describe()
data_arr=np.array(data)
#####univarient
data.skew()
###bivarient
corr_matrix_pd=data.corr()

data['DistanceFromHome'].value_counts()

data['DistanceFromHome']= np.log(data['DistanceFromHome'])

data['DistanceFromHome'].value_counts()



#encoding the variable####
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
data['DistanceFromHome']=LE.fit_transform(data['DistanceFromHome'])
data['DistanceFromHome'].value_counts()

data['Education']=LE.fit_transform(data['Education'])
data['Education'].value_counts()


data['EnvironmentSatisfaction']=LE.fit_transform(data['EnvironmentSatisfaction'])
data['EnvironmentSatisfaction'].value_counts()

data['JobInvolvement']=LE.fit_transform(data['JobInvolvement'])
data['JobInvolvement'].value_counts()

data['JobLevel']=LE.fit_transform(data['JobLevel'])
data['JobLevel'].value_counts()

data['JobSatisfaction']=LE.fit_transform(data['JobSatisfaction'])
data['JobSatisfaction'].value_counts()

data['PerformanceRating']=LE.fit_transform(data['PerformanceRating'])
data['PerformanceRating'].value_counts()

data['RelationshipSatisfaction']=LE.fit_transform(data['RelationshipSatisfaction'])
data['RelationshipSatisfaction'].value_counts()

data['StockOptionLevel']=LE.fit_transform(data['StockOptionLevel'])
data['StockOptionLevel'].value_counts()

data['WorkLifeBalance']=LE.fit_transform(data['WorkLifeBalance'])
data['WorkLifeBalance'].value_counts()

data['Attrition']=LE.fit_transform(data['Attrition'])
data['Attrition'].value_counts()

data['Gender']=LE.fit_transform(data['Gender'])
data['Gender'].value_counts()

data['JobRole']=LE.fit_transform(data['JobRole'])
data['JobRole'].value_counts()

data['Over18']=LE.fit_transform(data['Over18'])
data['Over18'].value_counts()

data['OverTime']=LE.fit_transform(data['OverTime'])
data['OverTime'].value_counts()


data['MaritalStatus']=LE.fit_transform(data['MaritalStatus'])
data['MaritalStatus'].value_counts()

data['EducationField']=LE.fit_transform(data['EducationField'])
data['EducationField'].value_counts()

data['BusinessTravel']=LE.fit_transform(data['BusinessTravel'])
data['BusinessTravel'].value_counts()

data['Department']=LE.fit_transform(data['Department'])
data['Department'].value_counts()




#########classification logistics###########
Y=data['Attrition']
X=data.iloc[:,1:31]
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

######svm#############
from sklearn import svm
svm_RF=svm.SVR()
svm_RF.fit(X,Y)
preds_SVM=svm_RF.predict(X)
 
preds_SVM_1= np.abs(np.round(preds_SVM))

cm_SVM=  confusion_matrix(Y,preds_SVM_1)

###############################
#######splitting the data
from sklearn.model_selection import train_test_split

X_train,x_test,Y_train,y_test=train_test_split(X,Y,test_size =0.2, random_state =0)


#############random forest in splited train#########################
from sklearn.ensemble import RandomForestClassifier
RF =RandomForestClassifier(n_estimators=500)
RF.fit(X_train,Y_train)
preds_RF_1 = RF.predict(X_train)
cm_RF_1= confusion_matrix (Y_train,preds_RF_1)

##########random forest in spllited test##########
from sklearn.ensemble import RandomForestClassifier
RF =RandomForestClassifier(n_estimators=500)
RF.fit(x_test,y_test)
preds_RF_2 = RF.predict(x_test)
cm_RF_2= confusion_matrix (y_test,preds_RF_2)

















