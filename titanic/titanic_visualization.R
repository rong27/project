# setwd("C:/Users/rong/Desktop/R/titanic")
# setwd("C:/Users/joy.lin/Desktop/titanicdataset-traincsv")

TitanicTrain <- read.csv("train.csv")
View(TitanicTrain)

any(is.na(TitanicTrain))
sum(is.na(TitanicTrain))
complete.cases(TitanicTrain)

install.packages("ggplot2")
install.packages("mice")

library(ggplot2)
library(RColorBrewer)
library(scales)
library(mice)


#missing value of Age 
summary(TitanicTrain$Age)
Age_miss <- subset(TitanicTrain, select = c(Age,Fare))
Age_miss
age_no_missing_value <- mice(Age_miss, m = 3, maxit = 50, method = 'cart', seed = 100 )
View(complete(age_no_missing_value,1))
View(complete(age_no_missing_value,2))
View(complete(age_no_missing_value,3))

age_fare_mice_2 <- (complete(age_no_missing_value,2))

#單變數 ( Survived )

table(TitanicTrain$Survived)
class(TitanicTrain$Survived)
survived_factor <- as.factor(TitanicTrain$Survived)
survived_factor
class(survived_factor)


ggplot(TitanicTrain, aes(survived_factor))+
  geom_bar(fill='deepskyblue4')+
  labs(title = '倖存長條圖', x = '倖存', y = '人數', hjust=0.5)+
  theme(plot.title = element_text(colour = 'black', face = 'bold', size = 16, hjust = 0.5),
        axis.title.x = element_text(colour = 'darkslateblue', face = 'bold', size = 14, hjust = 0.5),
        axis.title.y = element_text(colour = 'darkslateblue', face = 'bold', size = 14, hjust =0.5))

#單變數 ( Pclass )

table(TitanicTrain$Pclass)
class(TitanicTrain$Pclass)
Pclass_factor <- as.factor(TitanicTrain$Pclass)
Pclass_factor
class(Pclass_factor)

ggplot(TitanicTrain, aes(Pclass_factor))+
  geom_bar(fill='firebrick2')+
  labs(title = '船票等級長條圖', x = '船票等級', y = '人數', hjust=0.5)+
  theme(plot.title = element_text(colour = 'hotpink4', face = 'bold', size = 16, hjust = 0.5),
        axis.title.x = element_text(colour = 'navy', face = 'bold', size = 14, hjust = 0.5),
        axis.title.y = element_text(colour = 'navy', face = 'bold', size = 14, hjust =0.5))

#雙變數 ( Survived and Sex )
table(TitanicTrain$Survived, TitanicTrain$Sex)

Sex_table_survived <- xtabs(Survived==1~Sex,TitanicTrain)
Sex_table_survived_prop <- prop.table(Sex_table_survived)
Sex_table_survived_prop.df <- data.frame(Sex_table_survived_prop)

Sex_table_death <- xtabs(Survived==0~Sex,TitanicTrain)
Sex_table_death_prop <- prop.table(Sex_table_death)
Sex_table_death_prop.df <- data.frame(Sex_table_death_prop)

ggplot(Sex_table_survived_prop.df, aes(x='',y=Freq, fill = Sex)) +
  geom_bar(stat = 'identity', width = 1) +
  coord_polar('y', start=0) + 
  labs(title='性別於倖存之圓餅圖',fill = NULL) +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(),
    plot.title=element_text(colour = 'red',size = 14, face = 'bold',hjust = 0.5)
  ) +
  geom_text(aes(label = percent(Freq)),size=5,position = position_stack(vjust = 0.5))

ggplot(Sex_table_death_prop.df, aes(x='',y=Freq, fill = Sex)) +
  geom_bar(stat = 'identity', width = 1) +
  coord_polar('y', start=0) + 
  labs(title='性別於罹難之圓餅圖',fill = NULL) +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(),
    plot.title=element_text(colour = 'red',size = 14, face = 'bold',hjust = 0.5)
  ) +
  geom_text(aes(label = percent(Freq)),size=5,position = position_stack(vjust = 0.5))




#雙變數 ( Survived and Embarked )
table(TitanicTrain$Survived, TitanicTrain$Embarked)


Embarked_table_survived <- xtabs(Survived==1~Embarked,TitanicTrain)
Embarked_table_survived_prop <- prop.table(Embarked_table_survived)
Embarked_table_survived_prop.df <- data.frame(Embarked_table_survived_prop)


ggplot(Embarked_table_survived_prop.df, aes(x='',y=Freq, fill = Embarked)) +
  geom_bar(stat = 'identity', width = 1) +
  coord_polar('y', start=0) + 
  labs(title='不同登船港口對存活之圓餅圖',fill = '登船口') +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(),
    plot.title=element_text(colour = 'red',size = 14, face = 'bold',hjust = 0.5)
  ) +
  geom_text(aes(label = percent(Freq)),size=5,position = position_stack(vjust = 0.5))


Embarked_table_death <- xtabs(Survived==0~Embarked,TitanicTrain)
Embarked_table_death_prop <- prop.table(Embarked_table_death)
Embarked_table_death_prop.df <- data.frame(Embarked_table_death_prop)


ggplot(Embarked_table_death_prop.df, aes(x='',y=Freq, fill = Embarked)) +
  geom_bar(stat = 'identity', width = 1) +
  coord_polar('y', start=0) + 
  labs(title='不同登船港口對罹難之圓餅圖',fill = '登船口') +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(),
    plot.title=element_text(colour = 'red',size = 14, face = 'bold',hjust = 0.5)
  ) +
  geom_text(aes(label = percent(Freq)),size=5,position = position_stack(vjust = 0.5))

#趨勢圖
ggplot(TitanicTrain, aes(age_fare_mice_2$Age)) +
  geom_freqpoly(colour = 'red', size = 1) +
  labs(title = '年齡對於是否倖存之趨勢圖', x = '年齡', y = '人數', fill = '存活' ) +
  theme(plot.title = element_text(colour = 'blue', face = 'bold',size = 14, hjust = 0.5),
        axis.title.x = element_text(colour = 'darkblue', face = 'bold', size = 14, hjust = 0.5),
        axis.title.y = element_text(colour = 'darkblue', face = 'bold', size = 14, hjust =0.5)) +
  scale_y_continuous(labels = comma) + 
  facet_wrap(~ Survived) +
  theme(legend.position = 'none')


# boxplot
ggplot(TitanicTrain,aes(x=factor(Survived), y=Fare)) +
  geom_boxplot(fill = c('darkgoldenrod2', 'brown2'), colour = 'black') + 
  labs(title = '票價與是否存活之盒形圖',  x = '是否存活', y = '票價') + 
  theme(plot.title = element_text(colour = 'darkblue', size = 14, face = 'bold', hjust = 0.5),
        axis.title.x = element_text(colour = 'brown2', face = 'bold', size = 14, hjust = 0.5),
        axis.title.y = element_text(colour = 'darkslateblue', face = 'bold', size = 14, hjust =0.5)) +
  coord_flip()




