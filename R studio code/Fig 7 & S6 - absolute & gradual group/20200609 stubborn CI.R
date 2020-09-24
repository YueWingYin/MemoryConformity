library(plotly)
library(dplyr)
library(ggplot2)
library(ggpubr)
library(zoo)
library(tidyverse)
library(IDPmisc)
library(ggrepel)

### Please import data from excel file "Memory conformity Raw data", sheet "Data"

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
flip1 <- rbind(pos1,neg_flip1)

#compute CI - trial 1
flip1$R1R0 <-flip1$R1 - flip1$R0
flip1$C1R0 <-flip1$C1 - flip1$R0
flip1$R2R1 <-flip1$R2 - flip1$R1
flip1$C2R1 <-flip1$C2 - flip1$R1
flip1$R3R2 <-flip1$R3 - flip1$R2
flip1$C3R2 <-flip1$C3 - flip1$R2

flip1$CI<-(flip1$R1R0/flip1$C1R0)
flip1$CI2<-(flip1$R2R1/flip1$C2R1)
flip1$CI3<-(flip1$R3R2/flip1$C3R2)

flip1<-flip1[complete.cases(flip1), ]
######################################################################
#classifying high/med/low R and C
flip1$R0group <- case_when (flip1$R0>=0 & flip1$R0<=29 ~ as.numeric(1),
                            flip1$R0>=30 & flip1$R0<=59 ~ as.numeric(2),
                            flip1$R0>=60 & flip1$R0<=100 ~ as.numeric(3),
)

flip1$C1group <- case_when (flip1$R0>=0 & flip1$R0<=29 ~ as.numeric(1),
                            flip1$R0>=30 & flip1$R0<=59 ~ as.numeric(2),
                            flip1$R0>=60 & flip1$R0<=100 ~ as.numeric(3),
                            flip1$R0<0 & flip1$R0>=29*-1 ~ as.numeric(4),
                            flip1$R0<=30*-1 & flip1$R0>=59*-1 ~ as.numeric(5),
                            flip1$R0<=60*-1 & flip1$R0>=100*-1 ~ as.numeric(6),
)


flip1$R1group <- case_when (flip1$R1>=0 & flip1$R1<=29 ~ as.numeric(1),
                            flip1$R1>=30 & flip1$R1<=59 ~ as.numeric(2),
                            flip1$R1>=60 & flip1$R1<=100 ~ as.numeric(3),
                            flip1$R1<0 & flip1$R1>=29*-1 ~ as.numeric(4),
                            flip1$R1<=30*-1 & flip1$R1>=59*-1 ~ as.numeric(5),
                            flip1$R1<=60*-1 & flip1$R1>=100*-1 ~ as.numeric(6),
)


flip1$R2group <- case_when (flip1$R2>=0 & flip1$R2<=29 ~ as.numeric(1),
                            flip1$R2>=30 & flip1$R2<=59 ~ as.numeric(2),
                            flip1$R2>=60 & flip1$R2<=100 ~ as.numeric(3),
                            flip1$R2<0 & flip1$R2>=29*-1 ~ as.numeric(4),
                            flip1$R2<=30*-1 & flip1$R2>=59*-1 ~ as.numeric(5),
                            flip1$R2<=60*-1 & flip1$R2>=100*-1 ~ as.numeric(6),
)

flip1$C3group <- case_when (flip1$C3>=0 & flip1$C3<=29 ~ as.numeric(1),
                            flip1$C3>=30 & flip1$C3<=59 ~ as.numeric(2),
                            flip1$C3>=60 & flip1$C3<=100 ~ as.numeric(3),
                            flip1$C3<0 & flip1$C3>=29*-1 ~ as.numeric(4),
                            flip1$C3<=30*-1 & flip1$C3>=59*-1 ~ as.numeric(5),
                            flip1$C3<=60*-1 & flip1$C3>=100*-1 ~ as.numeric(6),
)

######################################################################
# CI --> conforming behavior naming

flip1$CIgroup <- case_when (flip1$CI<0 ~ "anti",
                            flip1$CI==0 ~ "no",
                            flip1$CI>0 & flip1$CI<1 ~ "under",
                            flip1$CI==1 ~ "perfect",
                            flip1$CI>1 ~ "over",
)

######################################################################
### Group data by R0 and C1 conditions in trial 1 -omitted C1=R0

###trial 3 -omitted C1=R0
group1at3 <- subset(flip1,R2>0 & C3<0 | R2<0 & C3>0) 
group2at3 <- subset(flip1,R2>0 & C3>0 | R2<0 & C3<0)

#################################################################
# when Rpre starts with high confidence or Rpre = high confidence that was gradually achieved - trial 3 group 1

RpreGt3 <- subset(group1at3, group1at3$R2group==3 & group1at3$R0group!=3 & group1at3$R0 < group1at3$R1 & group1at3$R1 < group1at3$R2 |group1at3$R2group==6 & group1at3$R0group!=6 & group1at3$R0 > group1at3$R1 & group1at3$R1 > group1at3$R2)
RpreAt3 <- subset(group1at3, group1at3$R2group==3 & group1at3$R0group==3 & group1at3$R1group==3 & group1at3$Participant != 32 | group1at3$R2group==6 & group1at3$R0group==6 & group1at3$R1group==6 & group1at3$Participant != 32)

RpreGid7t3 <- subset(RpreGt3, RpreGt3$C3group==4|RpreGt3$C3group==1)
RpreGid8t3 <- subset(RpreGt3, RpreGt3$C3group==5|RpreGt3$C3group==2)
RpreGid9t3 <- subset(RpreGt3, RpreGt3$C3group==6|RpreGt3$C3group==3)
RpreAid7t3 <- subset(RpreAt3, RpreAt3$C3group==4|RpreAt3$C3group==1)
RpreAid8t3 <- subset(RpreAt3, RpreAt3$C3group==5|RpreAt3$C3group==2)
RpreAid9t3 <- subset(RpreAt3, RpreAt3$C3group==6|RpreAt3$C3group==3)

RpreGid7t3count<-count(RpreGid7t3, CIgroup)
RpreGid7t3count$percent<-RpreGid7t3count$n/21
RpreGid7t3count$group<-"gradual"
RpreGid8t3count<-count(RpreGid8t3, CIgroup)
RpreGid8t3count$percent<-RpreGid8t3count$n/10
RpreGid8t3count$group<-"gradual"
RpreGid9t3count<-count(RpreGid9t3, CIgroup)
RpreGid9t3count$percent<-RpreGid9t3count$n/9
RpreGid9t3count$group<-"gradual"

RpreAid7t3count<-count(RpreAid7t3, CIgroup)
RpreAid7t3count$percent<-RpreAid7t3count$n/179
RpreAid7t3count$group<-"Absolute"
RpreAid8t3count<-count(RpreAid8t3, CIgroup)
RpreAid8t3count$percent<-RpreAid8t3count$n/108
RpreAid8t3count$group<-"Absolute"
RpreAid9t3count<-count(RpreAid9t3, CIgroup)
RpreAid9t3count$percent<-RpreAid9t3count$n/32
RpreAid9t3count$group<-"Absolute"

Rpreid7t3<-rbind(RpreGid7t3count,RpreAid7t3count)
Rpreid8t3<-rbind(RpreGid8t3count,RpreAid8t3count)
Rpreid9t3<-rbind(RpreGid9t3count,RpreAid9t3count)

figRpreid7t3<-ggplot()+geom_bar(aes(fill=Rpreid7t3$CIgroup,x=Rpreid7t3$group, y = Rpreid7t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
figRpreid8t3<-ggplot()+geom_bar(aes(fill=Rpreid8t3$CIgroup,x=Rpreid8t3$group, y = Rpreid8t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
figRpreid9t3<-ggplot()+geom_bar(aes(fill=Rpreid9t3$CIgroup,x=Rpreid9t3$group, y = Rpreid9t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
G1<-ggarrange(
  figRpreid7t3, figRpreid8t3,figRpreid9t3,
  common.legend = TRUE, legend = "bottom",nrow = 1
)


########################################################################
# when Rpre starts with high confidence or Rpre = high confidence that was gradually achieved - trial 3 group 2
RpreGt3g2 <- subset(group2at3, group2at3$R2group==3 & group2at3$R0group!=3 & group2at3$R0 < group2at3$R1 & group2at3$R1 < group2at3$R2|group2at3$R2group==6 & group2at3$R0group!=6 & group2at3$R0 > group2at3$R1 & group2at3$R1 > group2at3$R2)
RpreAt3g2 <- subset(group2at3, group2at3$R2group==3 & group2at3$R0group==3 & group2at3$R1group==3& group2at3$Participant != 32 | group2at3$R2group==6 & group2at3$R0group==6 & group2at3$R1group==6& group2at3$Participant != 32)

RpreGid7t3g2 <- subset(RpreGt3g2, RpreGt3g2$C3group==1|RpreGt3g2$C3group==4)
RpreGid8t3g2 <- subset(RpreGt3g2, RpreGt3g2$C3group==2|RpreGt3g2$C3group==5)
RpreGid9t3g2 <- subset(RpreGt3g2, RpreGt3g2$C3group==3|RpreGt3g2$C3group==6)
RpreAid7t3g2 <- subset(RpreAt3g2, RpreAt3g2$C3group==1|RpreAt3g2$C3group==4)
RpreAid8t3g2 <- subset(RpreAt3g2, RpreAt3g2$C3group==2|RpreAt3g2$C3group==5)
RpreAid9t3g2 <- subset(RpreAt3g2, RpreAt3g2$C3group==3|RpreAt3g2$C3group==6)

RpreGid7t3g2count<-count(RpreGid7t3g2, CIgroup)
RpreGid7t3g2count$percent<-RpreGid7t3g2count$n/34
RpreGid7t3g2count$group<-"gradual"
RpreGid8t3g2count<-count(RpreGid8t3g2, CIgroup)
RpreGid8t3g2count$percent<-RpreGid8t3g2count$n/66
RpreGid8t3g2count$group<-"gradual"
RpreGid9t3g2count<-count(RpreGid9t3g2, CIgroup)
RpreGid9t3g2count$percent<-RpreGid9t3g2count$n/190
RpreGid9t3g2count$group<-"gradual"

RpreAid7t3g2count<-count(RpreAid7t3g2, CIgroup)
RpreAid7t3g2count$percent<-RpreAid7t3g2count$n/89
RpreAid7t3g2count$group<-"Absolute"
RpreAid8t3g2count<-count(RpreAid8t3g2, CIgroup)
RpreAid8t3g2count$percent<-RpreAid8t3g2count$n/282
RpreAid8t3g2count$group<-"Absolute"
RpreAid9t3g2count<-count(RpreAid9t3g2, CIgroup)
RpreAid9t3g2count$percent<-RpreAid9t3g2count$n/319
RpreAid9t3g2count$group<-"Absolute"

Rpreid7g2t3<-rbind(RpreGid7t3g2count,RpreAid7t3g2count)
Rpreid8g2t3<-rbind(RpreGid8t3g2count,RpreAid8t3g2count)
Rpreid9g2t3<-rbind(RpreGid9t3g2count,RpreAid9t3g2count)

figRpreid7t3g2<-ggplot()+geom_bar(aes(fill=Rpreid7g2t3$CIgroup,x=Rpreid7g2t3$group, y = Rpreid7g2t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
figRpreid8t3g2<-ggplot()+geom_bar(aes(fill=Rpreid8g2t3$CIgroup,x=Rpreid8g2t3$group, y = Rpreid8g2t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
figRpreid9t3g2<-ggplot()+geom_bar(aes(fill=Rpreid9g2t3$CIgroup,x=Rpreid9g2t3$group, y = Rpreid9g2t3$percent),position="stack",stat = "identity") +   
  scale_fill_manual(values=c("anti"="#0302CA", "no"="#887500", "under"="#FFD402", "perfect"="#FFA202", "over"="#FF4502"), 
                    guide="none") + theme_minimal()
G2<-ggarrange(
  figRpreid7t3g2, figRpreid8t3g2,figRpreid9t3g2,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

#####################################################################
#calculate the SD of each participant
flip1<-NaRV.omit(flip1)

CI1diffmean<-aggregate( CI ~ Participant, flip1, mean)
CI1diffsd<-aggregate( CI ~ Participant, flip1, sd)

CI2diffmean<-aggregate( CI2 ~ Participant, flip1, mean)
CI2diffsd<-aggregate( CI2 ~ Participant, flip1, sd)

CI3diffmean<-aggregate( CI3 ~ Participant, flip1, mean)
CI3diffsd<-aggregate( CI3 ~ Participant, flip1, sd)

CImeansd<-cbind(CI1diffmean, CI1diffsd)
names(CImeansd)[2] <-"mean"
names(CImeansd)[4] <-"sd"
CI2meansd<-cbind(CI2diffmean, CI2diffsd)
names(CI2meansd)[2] <-"mean"
names(CI2meansd)[4] <-"sd"
CI3meansd<-cbind(CI3diffmean, CI3diffsd)
names(CI3meansd)[2] <-"mean"
names(CI3meansd)[4] <-"sd"


Partig1<-RpreAt3$Participant
Partig1<-Partig1[!duplicated(Partig1)]

Partig2<-RpreAt3g2$Participant
Partig2<-Partig2[!duplicated(Partig2)]

Partig3<-RpreAt3g3$Participant
Partig3<-Partig3[!duplicated(Partig3)]

Parti<-c(Partig1,Partig2,Partig3)
Parti<-Parti[!duplicated(Parti)]

PartiCImeansi<-CImeansd[is.element(CImeansd$Participant, Parti),]
PartiCI2meansi<-CI2meansd[is.element(CI2meansd$Participant, Parti),]
PartiCI3meansi<-CI3meansd[is.element(CI3meansd$Participant, Parti),]

Parti32t1<-subset(CImeansd, CImeansd$Participant==32)
Parti32t2<-subset(CI2meansd, CI2meansd$Participant==32)
Parti32t3<-subset(CI3meansd, CI3meansd$Participant==32)

CImeansd[3] <- NULL 
CI2meansd[3] <- NULL 
CI3meansd[3] <- NULL 

CIPartiMeanSd<-ggplot()+ geom_hline(yintercept=0, size=0.5)+geom_vline(xintercept=0, size=0.5)+geom_point(aes(x = CImeansd$sd, y =CImeansd$mean, label = CImeansd$Participant),size=2, colour="#038AF6")+geom_text_repel(data=CImeansd, aes(x = CImeansd$sd, y =CImeansd$mean, label = CImeansd$Participant),size=2)+
  geom_point(aes(x=PartiCImeansi$sd, y=PartiCImeansi$mean),size=2, colour="#F690DD")+
  geom_point(aes(x=Parti32t1$sd, y=Parti32t1$mean),size=2, colour="#F61A03")+ xlim(0,5)+ ylim(-1.5,1.5)+theme_minimal()
CI2PartiMeanSd<-ggplot()+ geom_hline(yintercept=0, size=0.5)+geom_vline(xintercept=0, size=0.5)+geom_point(aes(x = CI2meansd$sd, y =CI2meansd$mean, label = CI2meansd$Participant),size=2, colour="#038AF6")+geom_text_repel(data=CI2meansd, aes(x = CI2meansd$sd, y =CI2meansd$mean, label = CI2meansd$Participant),size=2)+
  geom_point(aes(x=PartiCI2meansi$sd, y=PartiCI2meansi$mean),size=2, colour="#F690DD")+
  geom_point(aes(x=Parti32t2$sd, y=Parti32t2$mean),size=2, colour="#F61A03")+ xlim(0,5)+ ylim(-1.5,1.5)+theme_minimal()
CI3PartiMeanSd<-ggplot()+ geom_hline(yintercept=0, size=0.5)+geom_vline(xintercept=0, size=0.5)+geom_point(aes(x = CI3meansd$sd, y =CI3meansd$mean, label = CI3meansd$Participant),size=2, colour="#038AF6")+geom_text_repel(data=CI3meansd, aes(x = CI3meansd$sd, y =CI3meansd$mean, label = CI3meansd$Participant),size=2)+
  geom_point(aes(x=PartiCI3meansi$sd, y=PartiCI3meansi$mean),size=2, colour="#F690DD")+
  geom_point(aes(x=Parti32t3$sd, y=Parti32t3$mean),size=2, colour="#F61A03")+ xlim(0,5)+ ylim(-1.5,1.5)+theme_minimal()


Stubborn<-ggarrange(
  CIPartiMeanSd, CI2PartiMeanSd,CI3PartiMeanSd,
  common.legend = TRUE, legend = "bottom",nrow = 1
)