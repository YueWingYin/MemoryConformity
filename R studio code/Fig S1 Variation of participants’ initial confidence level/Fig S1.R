library(reshape)
library(dplyr)
library(plotly)
library(ggplot2)
library(ggpubr)
library(rstatix)
library(plyr)

data <- Memory_conformity_Raw_data_
data$mean<-data$mean

target<- subset(data,data$StudyTest == 'Target')
lure <- subset(data,data$StudyTest == 'Foil')

targetmeansdt1<-ddply(target,~VideoName,summarise,mean=mean(R0),sd=sd(R0))
luremeansdt1<-ddply(lure,~VideoName,summarise,mean=mean(R0),sd=sd(R0))

targetmeansdt1 <- targetmeansdt1[order(-targetmeansdt1$mean),]
luremeansdt1 <- luremeansdt1[order(luremeansdt1$mean),]

targetmeansdt1$ID <- seq.int(nrow(targetmeansdt1))
luremeansdt1$ID <- seq.int(nrow(luremeansdt1))

targetmeansdt1$min <-targetmeansdt1$mean-targetmeansdt1$sd
targetmeansdt1$max <-targetmeansdt1$mean+targetmeansdt1$sd

luremeansdt1$min <-luremeansdt1$mean-luremeansdt1$sd
luremeansdt1$max <-luremeansdt1$mean+luremeansdt1$sd

#plotting
targetplot<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_point(aes(x=targetmeansdt1$ID, y=targetmeansdt1$mean), colour="#007fff", size=1)+ geom_errorbar(data=targetmeansdt1,aes(x=targetmeansdt1$ID, y=targetmeansdt1$mean, ymin=targetmeansdt1$min, ymax=targetmeansdt1$max), width = 0.1, colour="#007fff")+
  ylim(-110, 110)+ labs(y = "Mean of participant’s initial response (R0)", x = "Video #")+
  theme_minimal()

lureplot<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_point(aes(x=luremeansdt1$ID, y=luremeansdt1$mean), colour="#FF0000", size=1)+ geom_errorbar(data=luremeansdt1,aes(x=luremeansdt1$ID, y=luremeansdt1$mean, ymin=luremeansdt1$min, ymax=luremeansdt1$max), width = 0.1, colour="#FF0000")+
  ylim(-110, 110)+ labs(y = "Mean of participant’s initial response (R0)", x = "Video #")+
  theme_minimal()