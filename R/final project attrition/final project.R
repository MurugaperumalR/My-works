#final project on attrition rate
#importing the file
Attrition<- read.csv("H:\\data science\\data science\\final project attrition\\Attrition.csv",header=T,sep=",",na.strings=c(""))
str(Attrition)
summary(Attrition)
#library import
library(Hmisc)
library(e1071)
library(propagate)
#audit data
skewness(Attrition$DistanceFromHome)
skewness(Attrition$DailyRate)
skewness(Attrition$HourlyRate)
skewness(Attrition$MonthlyIncome)
skewness(Attrition$MonthlyRate)
subset_Attrition <- subset(Attrition,select = -c(Attrition ,BusinessTravel,Department,
                                                 EducationField,Gender,JobRole,MaritalStatus,Over18,OverTime))
#bivarient
correlation_matrix<-rcorr(subset_Attrition)
write.csv(correlation_matrix,'cormat.csv')
