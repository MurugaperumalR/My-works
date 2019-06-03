data<-read.csv("H:\\data science\\data science\\final project attrition\\data.csv",header=T,sep=",",na.strings=c(""))

____________________________________________________#DATA PREP________________________________________________

str(data)
summary(data)
skewness(data$DistanceFromHome)
skewness(data$Age)
skewness(data$DailyRate)
data_int<-subset(data,select=-c(Attrition,BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,Over18,OverTime))
cor_mat<-cor(data_int)
write.csv(cor_mat,"cor_mat.csv")

data$Education<-as.factor(data$Education)
data$EnvironmentSatisfaction<-as.factor(data$EnvironmentSatisfaction)
data$JobInvolvement<-as.factor(data$JobInvolvement)
data$JobLevel<-as.factor(data$JobLevel)
data$JobSatisfaction<-as.factor(data$JobSatisfaction)
data$PerformanceRating<-as.factor(data$PerformanceRating)
data$RelationshipSatisfaction<-as.factor(data$RelationshipSatisfaction)
data$StockOptionLevel<-as.factor(data$StockOptionLevel)
data$WorkLifeBalance<-as.factor(data$WorkLifeBalance)

str(data)

names(data)

model<-glm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,family = "binomial",data=data)
model
summary(model)
data$preds_glm<-predict(model,data,type="response")
table(data$Attrition,data$preds_glm)
data$outcome<-ifelse(data$preds_glm>=0.5,1,0)
table(data$Attrition,data$outcome)
#logging the variables
data$DistanceFromHome<-log(data$DistanceFromHome)
data$DistanceFromHome<- ifelse(data$DistanceFromHome==-Inf,0,data$DistanceFromHome)

model<-glm(Attrition~Age+DailyRate+Department+DistanceFromHome+Education+EducationField+EnvironmentSatisfaction+Gender+HourlyRate+JobInvolvement+JobLevel+JobRole+JobSatisfaction+MaritalStatus+MonthlyIncome+MonthlyRate+NumCompaniesWorked+PercentSalaryHike+RelationshipSatisfaction+TotalWorkingYears+WorkLifeBalance+YearsAtCompany+YearsInCurrentRole+YearsSinceLastPromotion+YearsWithCurrManager,family = "binomial",data=data)

summary(model)
data$preds_glm<-predict(model,data,type="response")
table(data$Attrition,data$preds_glm)
data$outcome<-ifelse(data$preds_glm>=0.5,1,0)
table(data$Attrition,data$outcome)
