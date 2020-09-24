library(plotly)
library(ggplot2)
library(dplyr)
library(akima)
library(reshape2)

data <- Memory_conformity_Raw_data_

#y axis

R1R0<-(data$R1-data$R0)

#x axis
C1divR0<-(data$C1/data$R0)
C1R0 <- data$C1-data$R0

#excluded 0
#data group - trial 1 --- exclude C1=R0

CIvalid <- subset(data,(data$C1 != data$R0))
CIvalid$CI1<-(CIvalid$R1-CIvalid$R0)/(CIvalid$C1-CIvalid$R0)

#exclude C1=0 & calculate SSE
CIvalidSSE1 <- subset(CIvalid,(CIvalid$C1 !=0))
CIvalidSSE1$SSE1 <- CIvalidSSE1$R1/CIvalidSSE1$C1
CIvalidSSE1pos<- subset(CIvalidSSE1,CIvalidSSE1$R0>0 & CIvalidSSE1$C1>0)
CIvalidSSE1neg<- subset(CIvalidSSE1,CIvalidSSE1$R0>0 & CIvalidSSE1$C1<0)
SSE1posmean<- tapply(CIvalidSSE1pos$SSE1, cut(CIvalidSSE1pos$R0, seq(0, 100, by=5)), mean)
SSE1possd<- tapply(CIvalidSSE1pos$SSE1, cut(CIvalidSSE1pos$R0, seq(0, 100, by=5)), sd)
SSE1negmean<- tapply(CIvalidSSE1neg$SSE1, cut(CIvalidSSE1neg$R0, seq(0, 100, by=5)), mean)
SSE1negsd<- tapply(CIvalidSSE1neg$SSE1, cut(CIvalidSSE1neg$R0, seq(0, 100, by=5)), sd)

#data group - trial 2
CIvalid2 <- subset(data,(data$C2 != data$R1))
CIvalid2$CI2<-(CIvalid2$R2-CIvalid2$R1)/(CIvalid2$C2-CIvalid2$R1)

CIvalidSSE2 <- subset(CIvalid2,(CIvalid2$C2 !=0))
CIvalidSSE2$SSE2 <- CIvalidSSE2$R2/CIvalidSSE2$C2
CIvalidSSE2pos<- subset(CIvalidSSE2,CIvalidSSE2$R1>0 & CIvalidSSE2$C2>0)
CIvalidSSE2neg<- subset(CIvalidSSE2,CIvalidSSE2$R1>0 & CIvalidSSE2$C2<0)

#data group - trial 3
CIvalid3 <- subset(data,(data$C3 != data$R2))
CIvalid3$CI3<-(CIvalid3$R3-CIvalid3$R2)/(CIvalid3$C3-CIvalid3$R2)

CIvalidSSE3 <- subset(CIvalid2,(CIvalid2$C3 !=0))
CIvalidSSE3$SSE3 <- CIvalidSSE3$R3/CIvalidSSE3$C3
CIvalidSSE3pos<- subset(CIvalidSSE3,CIvalidSSE3$R2>0 & CIvalidSSE3$C3>0)
CIvalidSSE3neg<- subset(CIvalidSSE3,CIvalidSSE3$R2>0 & CIvalidSSE3$C3<0)

palette <- colorRampPalette(c("mediumblue", "mediumblue","mediumblue", "gold4","gold","orange","orangered"))

#heatmap - trial 1
heatmap1 <- plot_ly(x=CIvalid$R0, y=CIvalid$C1, z=CIvalid$CI1, type = "heatmap", xgap=0, ygap=0, colors=palette(50), zauto = FALSE, zmin = -1.5, zmax = 1.5)  %>%
  layout(xaxis = list(range=(c(-101,101))), yaxis = list(range = (c(-101,101)))) 
  #add_segments(x = -100, xend = 100, y = -100, yend = 100, line = list(color = 'red', dash = 'dot'))

#heatmap --- flip side all - trial 2
heatmap2 <- plot_ly(x=CIvalid2$R1, y=CIvalid2$C2, z=CIvalid2$CI2, type = "heatmap", xgap=0, ygap=0,  colors=palette(50), zauto = FALSE, zmin = -1.5, zmax = 1.5)  %>%
  layout(xaxis = list(range=(c(-101,101))), yaxis = list(range = (c(-101,101)))) 
  #add_segments(x = -100, xend = 100, y = -100, yend = 100, line = list(color = 'red', dash = 'dot'))

#heatmap --- flip side all - trial 3
heatmap3 <- plot_ly(x=CIvalid3$R2, y=CIvalid3$C3, z=CIvalid3$CI3, type = "heatmap", xgap=0, ygap=0,  colors=palette(50), zauto = FALSE, zmin = -1.5, zmax = 1.5)  %>%
  layout(xaxis = list(range=(c(-101,101))), yaxis = list(range = (c(-101,101)))) 
  #add_segments(x = -100, xend = 100, y = -100, yend = 100, line = list(color = 'red', dash = 'dot'))

