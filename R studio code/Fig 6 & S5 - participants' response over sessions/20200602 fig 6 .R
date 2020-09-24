library(seriation)
library(plotly)
library(ggplot2)
library(heatmaply)
library(dplyr)

data <- Memory_conformity_Raw_data_

#flip side  -- trial 1,2,3 (base on R0)
pos1 <- subset(data,(data$R0>=0))
neg1 <- subset(data,(data$R0<0))
neg_flip1 <- neg1
neg_flip1$R0 <- -neg_flip1$R0
neg_flip1$C1 <- -neg_flip1$C1
neg_flip1$R1 <- -neg_flip1$R1
neg_flip1$C2 <- -neg_flip1$C2
neg_flip1$R2 <- -neg_flip1$R2
neg_flip1$C3 <- -neg_flip1$C3
neg_flip1$R3 <- -neg_flip1$R3
data <- rbind(pos1,neg_flip1)

count<-count(data, data$R0, data$C1)


#grouping
data$group <- case_when (data$R3>=0 & data$R0==data$R1 & data$R1==data$R2 & data$R2==data$R3~"1",
                         data$R3>=0 & data$R3>data$R0 ~"2",
                         data$R3>=0 & data$R3<data$R0~"3",
                         data$R3>=0 & data$R0==data$R3 & data$R0!=data$R1 |data$R0>=0 & data$R3>=0 & data$R0==data$R3 & data$R0!=data$R2~"4",
                        data$R3<0 ~"6",
)

data$group2 <- case_when (data$C1> data$C2 & data$C2>data$C3 ~"1",
                         data$C1< data$C2 & data$C2<data$C3 ~"2",
                         data$C1> data$C2 & data$C2<data$C3 ~"3",
                         data$C1< data$C2 & data$C2>data$C3 ~"4",
                         data$C1== data$C2 & data$C2>data$C3 ~"5",
                         data$C1== data$C2 & data$C2<data$C3 ~"6",
                         data$C1> data$C2 & data$C2==data$C3 ~"7",
                         data$C1< data$C2 & data$C2==data$C3 ~"8",
                         data$C1== data$C2 & data$C2==data$C3 ~"9",
)


#ordering data and delete irrelevent columns
data <- data[order(data$group, -data$R3-data$R2-data$R1-data$R0),]
heatdata<-data
heatdata$Group <- NULL
heatdata$Participant <- NULL
heatdata$Video <- NULL
heatdata$VideoName <- NULL
heatdata$StudyTest <- NULL
heatdata$Order <- NULL
heatdata$C1 <- NULL
heatdata$C2 <- NULL
heatdata$C3 <- NULL

heatdata2<-data
heatdata2$Group <- NULL
heatdata2$Participant <- NULL
heatdata2$Video <- NULL
heatdata2$VideoName <- NULL
heatdata2$StudyTest <- NULL
heatdata2$Order <- NULL
heatdata2$R0 <- NULL
heatdata2$R1 <- NULL
heatdata2$R2 <- NULL
heatdata2$R3 <- NULL


#plotting 
heatcolor <- c("purple4","purple","white", "olivedrab1","mediumseagreen")
R<-heatmaply(heatdata, Colv = FALSE, Rowv=FALSE, show_dendrogram = c(FALSE, FALSE), colors = heatcolor, seriate = "none", row_order=TRUE)%>%
  layout(yaxis = list(showline = FALSE, showticklabels = FALSE))

C<-heatmaply(heatdata2, Colv = FALSE, Rowv=FALSE, show_dendrogram = c(FALSE, FALSE), colors = heatcolor, seriate = "none", row_order=TRUE)%>%
  layout(yaxis = list(showline = FALSE, showticklabels = FALSE))
