library(plotly)
library(dplyr)
library(ggplot2)
library(ggpubr)
library(zoo)

### Please import data from excel file "Memory conformity Raw data", sheet "Data"

data <- Memory_conformity_Raw_data_

#flip side -- trial 1,2,3 (base on R0) 
#trial 1
pos1 <- subset(data,(data$R0>=0)) 
neg1 <- subset(data,(data$R0<0))
neg_flip1 <- neg1
neg_flip1$R0 <- -neg_flip1$R0
neg_flip1$C1 <- -neg_flip1$C1
neg_flip1$R1 <- -neg_flip1$R1
flip1 <- rbind(pos1,neg_flip1)

#trial 2
pos2 <- subset(data,(data$R1>=0))
neg2 <- subset(data,(data$R1<0))
neg_flip2 <- neg2
neg_flip2$R0 <- -neg_flip2$R0
neg_flip2$C1 <- -neg_flip2$C1
neg_flip2$R1 <- -neg_flip2$R1
neg_flip2$C2 <- -neg_flip2$C2
neg_flip2$R2 <- -neg_flip2$R2
flip2 <- rbind(pos2,neg_flip2)

#trial 3
pos3 <- subset(data,(data$R2>=0))
neg3 <- subset(data,(data$R2<0))
neg_flip3 <- neg3
neg_flip3$R0 <- -neg_flip3$R0
neg_flip3$C1 <- -neg_flip3$C1
neg_flip3$R1 <- -neg_flip3$R1
neg_flip3$C2 <- -neg_flip3$C2
neg_flip3$R2 <- -neg_flip3$R2
neg_flip3$C3 <- -neg_flip3$C3
neg_flip3$R3 <- -neg_flip3$R3
flip3 <- rbind(pos3,neg_flip3)

#compute CI - trial 1
flip1$R1R0 <-flip1$R1 - flip1$R0
flip1$C1R0 <-flip1$C1 - flip1$R0

flip1$CI<-(flip1$R1R0/flip1$C1R0)
flip1$tan <-atan(flip1$CI)*180/pi

flip1$angle <- case_when (flip1$R1R0>0 & flip1$C1R0>0 ~ flip1$tan+0,
                          flip1$R1R0>0 & flip1$C1R0<0 ~ flip1$tan+180,
                          flip1$R1R0<0 & flip1$C1R0<0 ~ flip1$tan+180,
                          flip1$R1R0<0 & flip1$C1R0>0 ~ flip1$tan+360,
                          flip1$R1R0>0 & flip1$C1R0==0 ~ as.numeric(90),
                          flip1$R1R0<0 & flip1$C1R0==0 ~ as.numeric(270),
                          flip1$R1R0==0 & flip1$C1R0>0 ~ as.numeric(0), 
                          flip1$R1R0==0 & flip1$C1R0<0 ~ as.numeric(180),  
                          flip1$R1R0==0 & flip1$C1R0 ==0 ~as.numeric(0),
)

#compute CI - trial 2
flip2$R2R1 <-flip2$R2 - flip2$R1
flip2$C2R1 <-flip2$C2 - flip2$R1

flip2$CI<-(flip2$R2R1/flip2$C2R1)
flip2$tan <-atan(flip2$CI)*180/pi

flip2$angle <- case_when (flip2$R2R1>0 & flip2$C2R1>0 ~ flip2$tan+0,
                          flip2$R2R1>0 & flip2$C2R1<0 ~ flip2$tan+180,
                          flip2$R2R1<0 & flip2$C2R1<0 ~ flip2$tan+180,
                          flip2$R2R1<0 & flip2$C2R1>0 ~ flip2$tan+360,
                          flip2$R2R1>0 & flip2$C2R1==0 ~ as.numeric(90),
                          flip2$R2R1<0 & flip2$C2R1==0 ~ as.numeric(270),
                          flip2$R2R1==0 & flip2$C2R1>0 ~ as.numeric(0), 
                          flip2$R2R1==0 & flip2$C2R1<0 ~ as.numeric(180),  
                          flip2$R2R1==0 & flip2$C2R1 ==0 ~as.numeric(0),
)

#compute CI - trial 3
flip3$R3R2 <-flip3$R3 - flip3$R2
flip3$C3R2 <-flip3$C3 - flip3$R2

flip3$CI<-(flip3$R3R2/flip3$C3R2)
flip3$tan <-atan(flip3$CI)*180/pi

flip3$angle <- case_when (flip3$R3R2>0 & flip3$C3R2>0 ~ flip3$tan+0,
                          flip3$R3R2>0 & flip3$C3R2<0 ~ flip3$tan+180,
                          flip3$R3R2<0 & flip3$C3R2<0 ~ flip3$tan+180,
                          flip3$R3R2<0 & flip3$C3R2>0 ~ flip3$tan+360,
                          flip3$R3R2>0 & flip3$C3R2==0 ~ as.numeric(90),
                          flip3$R3R2<0 & flip3$C3R2==0 ~ as.numeric(270),
                          flip3$R3R2==0 & flip3$C3R2>0 ~ as.numeric(0), 
                          flip3$R3R2==0 & flip3$C3R2<0 ~ as.numeric(180),  
                          flip3$R3R2==0 & flip3$C3R2 ==0 ~as.numeric(0),
)

######################################################################
#classifying Rpre and C
flip1$R0group <- case_when (flip1$R0==0 ~ as.numeric(0),
                            flip1$R0>0 & flip1$R0<31 ~ as.numeric(1),
                            flip1$R0>30 & flip1$R0<61 ~ as.numeric(2),
                            flip1$R0>60 & flip1$R0<101 ~ as.numeric(3),
)

flip1$C1group <- case_when (flip1$C1==0 ~ as.numeric(0),
                            flip1$C1>0 & flip1$C1<31 ~ as.numeric(1),
                            flip1$C1>30 & flip1$C1<61 ~ as.numeric(2),
                            flip1$C1>60 & flip1$C1<101 ~ as.numeric(3),
                            flip1$C1<0 & flip1$C1>31*-1 ~ as.numeric(4),
                            flip1$C1<30*-1 & flip1$C1>61*-1 ~ as.numeric(5),
                            flip1$C1<60*-1 & flip1$C1>101*-1 ~ as.numeric(6),
)

flip2$R1group <- case_when (flip2$R1==0 ~ as.numeric(0),
                            flip2$R1>0 & flip2$R1<31 ~ as.numeric(1),
                            flip2$R1>30 & flip2$R1<61 ~ as.numeric(2),
                            flip2$R1>60 & flip2$R1<101 ~ as.numeric(3),
)

flip2$C2group <- case_when (flip2$C2==0 ~ as.numeric(0),
                            flip2$C2>0 & flip2$C2<31 ~ as.numeric(1),
                            flip2$C2>30 & flip2$C2<61 ~ as.numeric(2),
                            flip2$C2>60 & flip2$C2<101 ~ as.numeric(3),
                            flip2$C2<0 & flip2$C2>31*-1 ~ as.numeric(4),
                            flip2$C2<30*-1 & flip2$C2>61*-1 ~ as.numeric(5),
                            flip2$C2<60*-1 & flip2$C2>101*-1 ~ as.numeric(6),
)

flip3$R2group <- case_when (flip3$R2==0 ~ as.numeric(0),
                            flip3$R2>0 & flip3$R2<31 ~ as.numeric(1),
                            flip3$R2>30 & flip3$R2<61 ~ as.numeric(2),
                            flip3$R2>60 & flip3$R2<101 ~ as.numeric(3),
)

flip3$C3group <- case_when (flip3$C3==0 ~ as.numeric(0),
                            flip3$C3>0 & flip3$C3<31 ~ as.numeric(1),
                            flip3$C3>30 & flip3$C3<61 ~ as.numeric(2),
                            flip3$C3>60 & flip3$C3<101 ~ as.numeric(3),
                            flip3$C3<0 & flip3$C3>31*-1 ~ as.numeric(4),
                            flip3$C3<30*-1 & flip3$C3>61*-1 ~ as.numeric(5),
                            flip3$C3<60*-1 & flip3$C3>101*-1 ~ as.numeric(6),
)

######################################################################
# CI --> naming conforming behavior 

flip1$CIgroup <- case_when (flip1$CI<0 ~ "anti",
                            flip1$CI==0 ~ "no",
                            flip1$CI>0 & flip1$CI<1 ~ "under",
                            flip1$CI==1 ~ "perfect",
                            flip1$CI>1 ~ "over",
)
flip2$CIgroup <- case_when (flip2$CI<0 ~ "anti",
                            flip2$CI==0 ~ "no",
                            flip2$CI>0 & flip2$CI<1 ~ "under",
                            flip2$CI==1 ~ "perfect",
                            flip2$CI>1 ~ "over",
)
flip3$CIgroup <- case_when (flip3$CI<0 ~ "anti",
                            flip3$CI==0 ~ "no",
                            flip3$CI>0 & flip3$CI<1 ~ "under",
                            flip3$CI==1 ~ "perfect",
                            flip3$CI>1 ~ "over",
)


######################################################################
### Group data by R0 and C1 conditions in trial 1 -omitted C1=R0

group1at1 <- subset(flip1,R0>0 & C1<0) 
group2at1 <- subset(flip1,R0>0 & C1>0 & R0>=C1)
group3at1 <- subset(flip1,R0>0 & C1>0 & R0<C1)
group4at1 <- subset(flip1,R0==0 & C1>0)
group5at1 <- subset(flip1, C1==0 & R0>0)

### Group data by R1 and C2 conditions in trial 2 -omitted C2=R1

group1at2 <- subset(flip2,R1>0 & C2<0) 
group2at2 <- subset(flip2,R1>0 & C2>0 & R1>=C2)
group3at2 <- subset(flip2,R1>0 & C2>0 & R1<C2)
group4at2 <- subset(flip2,R1==0 & C2>0)
group5at2 <- subset(flip2, C2==0 & R1>0)

###Group data by R2 and C3 conditions in trial 3 -omitted C3=R2
group1at3 <- subset(flip3,R2>0 & C3<0) 
group2at3 <- subset(flip3,R2>0 & C3>0 & R2>=C3)
group3at3 <- subset(flip3,R2>0 & C3>0 & R2<C3)
group4at3 <- subset(flip3,R2==0 & C3>0)
group5at3 <- subset(flip3, C3==0 & R2>0)

#CDF - group 1
#trial 1
ordergroup1t1 <- group1at1[order(group1at1$CI,group1at1$R0, group1at1$C1),]
ordergroup1t1$ID <- seq.int(nrow(ordergroup1t1))
ordergroup1t1$ID<-ordergroup1t1$ID/521*100
ordergroup1t1$newC1R0 <- ordergroup1t1$C1R0*(10/400)
ordergroup1t1$R0 <- ordergroup1t1$R0*(10/200)
ordergroup1t1$C1 <- ordergroup1t1$C1*(10/200)

#creating rolling mean - R0
rollmeant1g1<-rollapply(ordergroup1t1$R0,20,mean,partial = TRUE, align=c("left"))
t1g1R0 <- data.frame(matrix(unlist(rollmeant1g1), nrow=length(rollmeant1g1), byrow=T))
t1g1R0$ID <- seq.int(nrow(t1g1R0))
t1g1R0$ID<-t1g1R0$ID/521*100
names(t1g1R0)[1] <-"AverageR"

#creating rolling mean - C1
rollmeant1g1c<-rollapply(ordergroup1t1$C1,20,mean,partial = TRUE, align=c("left"))
t1g1C1 <- data.frame(matrix(unlist(rollmeant1g1c), nrow=length(rollmeant1g1c), byrow=T))
t1g1C1$ID <- seq.int(nrow(t1g1C1))
t1g1C1$ID<-t1g1C1$ID/521*100
names(t1g1C1)[1] <-"AverageC"

#trial 2
ordergroup1t2 <- group1at2[order(group1at2$CI,group1at2$R1,group1at2$C2),]
ordergroup1t2$ID <- seq.int(nrow(ordergroup1t2))
ordergroup1t2$ID<-ordergroup1t2$ID/647*100
ordergroup1t2$newC2R1 <- ordergroup1t2$C2R1*(10/400)
ordergroup1t2$R1 <- ordergroup1t2$R1*(10/200)
ordergroup1t2$C2 <- ordergroup1t2$C2*(10/200)

#creating rolling mean - R1
rollmeant2g1<-rollapply(ordergroup1t2$R1,20,mean,partial = TRUE, align=c("left"))
t2g1R1 <- data.frame(matrix(unlist(rollmeant2g1), nrow=length(rollmeant2g1), byrow=T))
t2g1R1$ID <- seq.int(nrow(t2g1R1))
t2g1R1$ID<-t2g1R1$ID/647*100
names(t2g1R1)[1] <-"AverageR"

#creating rolling mean - C2
rollmeant2g1c<-rollapply(ordergroup1t2$C2,20,mean,partial = TRUE, align=c("left"))
t2g1C2 <- data.frame(matrix(unlist(rollmeant2g1c), nrow=length(rollmeant2g1c), byrow=T))
t2g1C2$ID <- seq.int(nrow(t2g1C2))
t2g1C2$ID<-t2g1C2$ID/647*100
names(t2g1C2)[1] <-"AverageC"

#trial 3
ordergroup1t3 <- group1at3[order(group1at3$CI,group1at3$R2,group1at3$C3),]
ordergroup1t3$ID <- seq.int(nrow(ordergroup1t3))
ordergroup1t3$ID<-ordergroup1t3$ID/899*100
ordergroup1t3$newC3R2 <- ordergroup1t3$C3R2*(10/400)
ordergroup1t3$R2 <- ordergroup1t3$R2*(10/200)
ordergroup1t3$C3 <- ordergroup1t3$C3*(10/200)

#creating rolling mean - R2
rollmeant3g1<-rollapply(ordergroup1t3$R2,20,mean,partial = TRUE, align=c("left"))
t3g1R2 <- data.frame(matrix(unlist(rollmeant3g1), nrow=length(rollmeant3g1), byrow=T))
t3g1R2$ID <- seq.int(nrow(t3g1R2))
t3g1R2$ID<-t3g1R2$ID/899*100
names(t3g1R2)[1] <-"AverageR"

#creating rolling mean - C3
rollmeant3g1c<-rollapply(ordergroup1t3$C3,20,mean,partial = TRUE, align=c("left"))
t3g1C3 <- data.frame(matrix(unlist(rollmeant3g1c), nrow=length(rollmeant3g1c), byrow=T))
t3g1C3$ID <- seq.int(nrow(t3g1C3))
t3g1C3$ID<-t3g1C3$ID/899*100
names(t3g1C3)[1] <-"AverageC"

figfig1<-ggplot()+geom_bar(t1g1C1, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t1g1R0, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup1t1,mapping=aes(CI,ID),size=1.5) +xlab('T1') + theme_light()+scale_x_continuous(breaks=seq(-5, 5, 1))
figfig2<-ggplot()+geom_bar(t2g1C2, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t2g1R1, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup1t2,mapping=aes(CI,ID),size=1.5) +xlab('T2') + theme_light()+scale_x_continuous(breaks=seq(-5, 5, 1))
figfig3<-ggplot()+geom_bar(t3g1C3, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t3g1R2, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup1t3,mapping=aes(CI,ID),size=1.5) +xlab('T3') + theme_light()+scale_x_continuous(breaks=seq(-5, 5, 1))

plot1<-ggarrange(figfig1,figfig2,figfig3,ncol=1)

#CDF - group 2
#trial 1
group2at1e<-subset(group2at1, group2at1$R0!=group2at1$C1)
ordergroup2t1 <- group2at1e[order(group2at1e$CI,group2at1e$R0, group2at1e$C1),]
ordergroup2t1$ID <- seq.int(nrow(ordergroup2t1))
ordergroup2t1$ID<-ordergroup2t1$ID/1665*100
ordergroup2t1$newC1R0 <- ordergroup2t1$C1R0*(100/400)
ordergroup2t1$R0 <- ordergroup2t1$R0*(100/200)
ordergroup2t1$C1 <- ordergroup2t1$C1*(100/200)

#creating rolling mean - R0
rollmeant1g2<-rollapply(ordergroup2t1$R0,20,mean,partial = TRUE, align=c("left"))
t1g2R0 <- data.frame(matrix(unlist(rollmeant1g2), nrow=length(rollmeant1g2), byrow=T))
t1g2R0$ID <- seq.int(nrow(t1g2R0))
t1g2R0$ID<-t1g2R0$ID/1665*100
names(t1g2R0)[1] <-"AverageR"

#creating rolling mean - C1
rollmeant1g2c<-rollapply(ordergroup2t1$C1,20,mean,partial = TRUE, align=c("left"))
t1g2C1 <- data.frame(matrix(unlist(rollmeant1g2c), nrow=length(rollmeant1g2c), byrow=T))
t1g2C1$ID <- seq.int(nrow(t1g2C1))
t1g2C1$ID<-t1g2C1$ID/1665*100
names(t1g2C1)[1] <-"AverageC"

#trial 2
group2at2e<-subset(group2at2, group2at2$R1!=group2at2$C2)
ordergroup2t2 <- group2at2e[order(group2at2e$CI,group2at2e$R1, group2at2e$C2),]
ordergroup2t2$ID <- seq.int(nrow(ordergroup2t2))
ordergroup2t2$ID<-ordergroup2t2$ID/1731*100
ordergroup2t2$newC2R1 <- ordergroup2t2$C2R1*(100/400)
ordergroup2t2$R1 <- ordergroup2t2$R1*(100/200)
ordergroup2t2$C2 <- ordergroup2t2$C2*(100/200)

#creating rolling mean - R1
rollmeant2g2<-rollapply(ordergroup2t2$R1,20,mean,partial = TRUE, align=c("left"))
t2g2R1 <- data.frame(matrix(unlist(rollmeant2g2), nrow=length(rollmeant2g2), byrow=T))
t2g2R1$ID <- seq.int(nrow(t2g2R1))
t2g2R1$ID<-t2g2R1$ID/1731*100
names(t2g2R1)[1] <-"AverageR"

#creating rolling mean - C2
rollmeant2g2c<-rollapply(ordergroup2t2$C2,20,mean,partial = TRUE, align=c("left"))
t2g2C2 <- data.frame(matrix(unlist(rollmeant2g2c), nrow=length(rollmeant2g2c), byrow=T))
t2g2C2$ID <- seq.int(nrow(t2g2C2))
t2g2C2$ID<-t2g2C2$ID/1731*100
names(t2g2C2)[1] <-"AverageC"

#trial 3
group2at3e<-subset(group2at3, group2at3$R2!=group2at3$C3)
ordergroup2t3 <- group2at3e[order(group2at3e$CI,group2at3e$R2,group2at3e$C3),]
ordergroup2t3$ID <- seq.int(nrow(ordergroup2t3))
ordergroup2t3$ID<-ordergroup2t3$ID/1497*100
ordergroup2t3$newC3R2 <- ordergroup2t3$C3R2*(100/400)
ordergroup2t3$R2 <- ordergroup2t3$R2*(100/200)
ordergroup2t3$C3 <- ordergroup2t3$C3*(100/200)

#creating rolling mean - R2
rollmeant3g2<-rollapply(ordergroup2t3$R2,20,mean,partial = TRUE, align=c("left"))
t3g2R2 <- data.frame(matrix(unlist(rollmeant3g2), nrow=length(rollmeant3g2), byrow=T))
t3g2R2$ID <- seq.int(nrow(t3g2R2))
t3g2R2$ID<-t3g2R2$ID/1497*100
names(t3g2R2)[1] <-"AverageR"

#creating rolling mean - C3
rollmeant3g2c<-rollapply(ordergroup2t3$C3,20,mean,partial = TRUE, align=c("left"))
t3g2C3 <- data.frame(matrix(unlist(rollmeant3g2c), nrow=length(rollmeant3g2c), byrow=T))
t3g2C3$ID <- seq.int(nrow(t3g2C3))
t3g2C3$ID<-t3g2C3$ID/1497*100
names(t3g2C3)[1] <-"AverageC"

figfig4<-ggplot()+geom_bar(t1g2R0, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) +geom_bar(t1g2C1, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+ geom_line(ordergroup2t1,mapping=aes(CI,ID),size=1.5) +xlab('T1') + theme_light()+xlim(-50, 50)
figfig5<-ggplot()+geom_bar(t2g2R1, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) +geom_bar(t2g2C2, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+ geom_line(ordergroup2t2,mapping=aes(CI,ID),size=1.5) +xlab('T2') + theme_light()+xlim(-50, 50)
figfig6<-ggplot()+geom_bar(t3g2R2, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) +geom_bar(t3g2C3, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+ geom_line(ordergroup2t3,mapping=aes(CI,ID),size=1.5) +xlab('T3') + theme_light()+xlim(-50, 50)

plot2<-ggarrange(figfig4,figfig5,figfig6,ncol=1)

#CDF - group 3
#trial 1
ordergroup3t1 <- group3at1[order(group3at1$CI,group3at1$R0, group3at1$C1),]
ordergroup3t1$ID <- seq.int(nrow(ordergroup3t1))
ordergroup3t1$ID<-ordergroup3t1$ID/1079*100
ordergroup3t1$newC1R0 <- ordergroup3t1$C1R0*(100/400)
ordergroup3t1$R0 <- ordergroup3t1$R0*(100/200)
ordergroup3t1$C1 <- ordergroup3t1$C1*(100/200)

#creating rolling mean - R0
rollmeant1g3<-rollapply(ordergroup3t1$R0,20,mean,partial = TRUE, align=c("left"))
#t1g1R0<- rollmeant1g3[seq(1, length(rollmeant1g3), 30)]
t1g3R0 <- data.frame(matrix(unlist(rollmeant1g3), nrow=length(rollmeant1g3), byrow=T))
t1g3R0$ID <- seq.int(nrow(t1g3R0))
t1g3R0$ID<-t1g3R0$ID/1079*100
names(t1g3R0)[1] <-"AverageR"

#creating rolling mean - C1
rollmeant1g3c<-rollapply(ordergroup3t1$C1,20,mean,partial = TRUE, align=c("left"))
#t1g1C1<- rollmeant1g3c[seq(1, length(rollmeant1g3c), 30)]
t1g3C1 <- data.frame(matrix(unlist(rollmeant1g3c), nrow=length(rollmeant1g3c), byrow=T))
t1g3C1$ID <- seq.int(nrow(t1g3C1))
t1g3C1$ID<-t1g3C1$ID/1079*100
names(t1g3C1)[1] <-"AverageC"

#trial 2
ordergroup3t2 <- group3at2[order(group3at2$CI,group3at2$R1, group3at2$C2),]
ordergroup3t2$ID <- seq.int(nrow(ordergroup3t2))
ordergroup3t2$ID<-ordergroup3t2$ID/940*100
ordergroup3t2$newC2R1 <- ordergroup3t2$C2R1*(100/400)
ordergroup3t2$R1 <- ordergroup3t2$R1*(100/200)
ordergroup3t2$C2 <- ordergroup3t2$C2*(100/200)

#creating rolling mean - R1
rollmeant2g3<-rollapply(ordergroup3t2$R1,20,mean,partial = TRUE, align=c("left"))
t2g3R1 <- data.frame(matrix(unlist(rollmeant2g3), nrow=length(rollmeant2g3), byrow=T))
t2g3R1$ID <- seq.int(nrow(t2g3R1))
t2g3R1$ID<-t2g3R1$ID/940*100
names(t2g3R1)[1] <-"AverageR"

#creating rolling mean - C2
rollmeant2g3c<-rollapply(ordergroup3t2$C2,20,mean,partial = TRUE, align=c("left"))
t2g3C2 <- data.frame(matrix(unlist(rollmeant2g3c), nrow=length(rollmeant2g3c), byrow=T))
t2g3C2$ID <- seq.int(nrow(t2g3C2))
t2g3C2$ID<-t2g3C2$ID/940*100
names(t2g3C2)[1] <-"AverageC"

#trial 3
ordergroup3t3 <- group3at3[order(group3at3$CI,group3at3$R2,group3at3$C3),]
ordergroup3t3$ID <- seq.int(nrow(ordergroup3t3))
ordergroup3t3$ID<-ordergroup3t3$ID/916*100
ordergroup3t3$newC3R2 <- ordergroup3t3$C3R2*(100/400)
ordergroup3t3$R2 <- ordergroup3t3$R2*(100/200)
ordergroup3t3$C3 <- ordergroup3t3$C3*(100/200)

#creating rolling mean - R2
rollmeant3g3<-rollapply(ordergroup3t3$R2,20,mean,partial = TRUE, align=c("left"))
t3g3R2 <- data.frame(matrix(unlist(rollmeant3g3), nrow=length(rollmeant3g3), byrow=T))
t3g3R2$ID <- seq.int(nrow(t3g3R2))
t3g3R2$ID<-t3g3R2$ID/916*100
names(t3g3R2)[1] <-"AverageR"

#creating rolling mean - C3
rollmeant3g3c<-rollapply(ordergroup3t3$C3,20,mean,partial = TRUE, align=c("left"))
t3g3C3 <- data.frame(matrix(unlist(rollmeant3g3c), nrow=length(rollmeant3g3c), byrow=T))
t3g3C3$ID <- seq.int(nrow(t3g3C3))
t3g3C3$ID<-t3g3C3$ID/916*100
names(t3g3C3)[1] <-"AverageC"

figfig7<-ggplot()+geom_bar(t1g3C1, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t1g3R0, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup3t1,mapping=aes(CI,ID),size=1.5) +xlab('T1') + theme_light()+xlim(-50, 50)
figfig8<-ggplot()+geom_bar(t2g3C2, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t2g3R1, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup3t2,mapping=aes(CI,ID),size=1.5) +xlab('T2') + theme_light()+xlim(-50, 50)
figfig9<-ggplot()+geom_bar(t3g3C3, mapping=aes(AverageC,ID),fill = "#0072B2",stat="identity",orientation ="y",alpha = 0.7)+geom_bar(t3g3R2, mapping=aes(AverageR,ID),fill = "#D55E00",stat="identity",orientation ="y",alpha = 0.7) + geom_line(ordergroup3t3,mapping=aes(CI,ID),size=1.5) +xlab('T3') + theme_light()+xlim(-50, 50)

plot3<-ggarrange(figfig7,figfig8,figfig9,ncol=1)

cdfallg1 <- ggplot()+geom_vline(xintercept = 0)+geom_hline(yintercept = 0)+ geom_line(ordergroup1t1,mapping=aes(CI,ID),color = "steelblue", size=1,alpha = 0.3) +
  geom_line(ordergroup1t2,mapping=aes(CI,ID),color = "steelblue",size=1,alpha = 0.6) +
  geom_line(ordergroup1t3,mapping=aes(CI,ID),color = "steelblue",size=1) +
  geom_vline(xintercept = 1, linetype="dotted")+
  scale_x_continuous(limits=c(-5,5), breaks=seq(-5, 5, 1))+ theme_light() +xlab('CI')+ylab('Percentage')
cdfallg2 <- ggplot()+geom_vline(xintercept = 0)+geom_hline(yintercept = 0)+geom_line(ordergroup2t1,mapping=aes(CI,ID),color = "chocolate1", size=1,alpha = 0.3) +
  geom_line(ordergroup2t2,mapping=aes(CI,ID),color = "chocolate1",size=1,alpha = 0.6) +
  geom_line(ordergroup2t3,mapping=aes(CI,ID),color = "chocolate1",size=1) +
  geom_vline(xintercept = 1, linetype="dotted")+
  scale_x_continuous(limits=c(-5,5), breaks=seq(-5, 5, 1))+ theme_light() +xlab('CI')+ylab('Percentage')
cdfallg3 <- ggplot()+geom_vline(xintercept = 0)+geom_hline(yintercept = 0)+geom_line(ordergroup3t1,mapping=aes(CI,ID),color = "springgreen4", size=1,alpha = 0.3) +
  geom_line(ordergroup3t2,mapping=aes(CI,ID),color = "springgreen4", size=1,alpha = 0.6) +
  geom_line(ordergroup3t3,mapping=aes(CI,ID),color = "springgreen4", size=1) + 
  geom_vline(xintercept = 1, linetype="dotted")+
  scale_x_continuous(limits=c(-5,5), breaks=seq(-5, 5, 1))+ theme_light() +xlab('CI')+ylab('Percentage')
