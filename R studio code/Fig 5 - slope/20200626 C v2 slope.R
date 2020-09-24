library(plotly)
library(dplyr)
library(ggplot2)
library(zoo)
library(ggrepel)
library(tidyverse)
library(ggpubr)
library(rstatix)
library(plyr)
library(writexl)


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

#calculating slope of C across trial - taking mean of slope of C1C2 and C2C3
flip1$C1C2 <- (flip1$C2-flip1$C1)
flip1$C2C3 <-(flip1$C3-flip1$C2)
flip1$slope <- ((flip1$C2-flip1$C1)+(flip1$C3-flip1$C2))/2
flip1 <- subset(flip1,abs(flip1$C1C2-flip1$C2C3) <20)

flip1$group <- case_when (flip1$slope>=0 & flip1$slope<11 ~ as.numeric(1),
                          flip1$slope>10 & flip1$slope<21 ~ as.numeric(2),
                          flip1$slope>20 & flip1$slope<31 ~ as.numeric(3),
                          flip1$slope>30 & flip1$slope<41 ~ as.numeric(4),
                          flip1$slope>40 & flip1$slope<51 ~ as.numeric(5),
                          flip1$slope>50 & flip1$slope<61 ~ as.numeric(6),
                          flip1$slope>60 & flip1$slope<71 ~ as.numeric(7),
                          flip1$slope>70 & flip1$slope<81 ~ as.numeric(8),
                          flip1$slope<0 & flip1$slope>11*-1 ~ as.numeric(1),
                          flip1$slope<10*-1 & flip1$slope>21*-1 ~ as.numeric(2),
                          flip1$slope<20*-1 & flip1$slope>31*-1 ~ as.numeric(3),
                          flip1$slope<30*-1 & flip1$slope>41*-1 ~ as.numeric(4),
                          flip1$slope<40*-1 & flip1$slope>51*-1 ~ as.numeric(5),
                          flip1$slope<50*-1 & flip1$slope>61*-1 ~ as.numeric(6),
                          flip1$slope<60*-1 & flip1$slope>71*-1 ~ as.numeric(7),
                          flip1$slope<70*-1 & flip1$slope>81*-1 ~ as.numeric(8),
                          
)

#calculating rate of increase/ decrease
flip1$rate <- (flip1$R3-flip1$R0)/flip1$slope

#take out Cs with trends
down<-subset(flip1, flip1$R0 > flip1$C1 & flip1$C1 > flip1$C2 & flip1$C2 > flip1$C3 & flip1$group!=6 & flip1$group!=7 & flip1$group!=8)
up<-subset(flip1, flip1$R0 < flip1$C1 & flip1$C1 < flip1$C2 & flip1$C2 < flip1$C3 & flip1$group!=6 & flip1$group!=7 & flip1$group!=8)

downH <- subset(down, down$R0 >59)
downM <- subset(down, down$R0 >29 & down$R0<60)
downL <- subset(down, down$R0 >=0 & down$R0<30)

upH <- subset(up, up$R0 >59)
upM <- subset(up, up$R0 >29 & up$R0<60)
upL <- subset(up, up$R0 >=0 & up$R0<30)
####################################################################
#downward confederate trend - High R0
downHmean<-aggregate(downH$slope, list(downH$group),mean)
downHmean$R0<-mean(downH$R0)
downHmean$no <- 0
downHmeanT1<-downHmean
downHmeanT1$R0 <- downHmean$R0+(downHmean$x)
downHmeanT1$no <- 1
downHmeanT2<-downHmean
downHmeanT2$R0 <- downHmean$R0+(downHmean$x)*2
downHmeanT2$no <- 2
downHmeanT3<-downHmean
downHmeanT3$R0 <- downHmean$R0+(downHmean$x)*3
downHmeanT3$no <- 3
downHmean<-rbind(downHmean,downHmeanT1,downHmeanT2,downHmeanT3)

DHsd<-aggregate(downH$slope, list(downH$group),sd)
DHsd$x<-format(round(DHsd$x, 2), nsmall = 2)
DHsd$sd <- paste("sd =", DHsd$x)

downHmean$trial <- case_when (downHmean$no==1 ~ "R0",
                              downHmean$no==2 ~ "C1",
                              downHmean$no==3 ~ "C2",
                              downHmean$no==4 ~ "C3",
)

downHmeanR0<-downH %>% group_by(group) %>% summarise_at(vars(R0), funs(mean, sd))
downHmeanR0$sd<-sd(downH$R0)
downHmeanR0$mean<-mean(downH$R0)
downHmeanR0$min<-downHmeanR0$mean-downHmeanR0$sd
downHmeanR0$max<-downHmeanR0$mean+downHmeanR0$sd
downHmeanR0$no <- 0
downHmeanR1<-downH %>% group_by(group) %>% summarise_at(vars(R1), funs(mean, sd))
downHmeanR1$min<-downHmeanR1$mean-downHmeanR1$sd
downHmeanR1$max<-downHmeanR1$mean+downHmeanR1$sd
downHmeanR1$no <- 1
downHmeanR2<-downH %>% group_by(group) %>% summarise_at(vars(R2), funs(mean, sd))
downHmeanR2$min<-downHmeanR2$mean-downHmeanR2$sd
downHmeanR2$max<-downHmeanR2$mean+downHmeanR2$sd
downHmeanR2$no <- 2
downHmeanR3<-downH %>% group_by(group) %>% summarise_at(vars(R3), funs(mean, sd))
downHmeanR3$min<-downHmeanR3$mean-downHmeanR3$sd
downHmeanR3$max<-downHmeanR3$mean+downHmeanR3$sd
downHmeanR3$no <- 3

downHmeanplot<-rbind(downHmeanR0,downHmeanR1,downHmeanR2,downHmeanR3)

downHmeanplot$trial <- case_when (downHmeanplot$no==1 ~ "R0",
                                  downHmeanplot$no==2 ~ "R1",
                                  downHmeanplot$no==3 ~ "R2",
                                  downHmeanplot$no==4 ~ "R3",
)

DHCmean1<-subset(downHmean,downHmean$Group.1 ==1)
DHCmean2<-subset(downHmean,downHmean$Group.1 ==2)
DHCmean3<-subset(downHmean,downHmean$Group.1 ==3)
DHCmean4<-subset(downHmean,downHmean$Group.1 ==4)
DHCmean5<-subset(downHmean,downHmean$Group.1 ==5)

DHRmean1<-subset(downHmeanplot,downHmeanplot$group ==1)
DHRmean2<-subset(downHmeanplot,downHmeanplot$group ==2)
DHRmean3<-subset(downHmeanplot,downHmeanplot$group ==3)
DHRmean4<-subset(downHmeanplot,downHmeanplot$group ==4)
DHRmean5<-subset(downHmeanplot,downHmeanplot$group ==5)

DH1<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DHCmean1$no, y=DHCmean1$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DHRmean1$no, y=DHRmean1$mean), colour="#7AB317", size=0.5)+ geom_point(aes(x=DHRmean1$no, y=DHRmean1$mean), colour="#7AB317", size=0.5)+ geom_errorbar(data=DHRmean1,aes(x=DHRmean1$no, y=DHRmean1$mean, ymin=DHRmean1$min, ymax=DHRmean1$max), width = 0.2, colour="#7AB317")+
  geom_point(aes(x=DHCmean1$no, y=DHCmean1$R0), colour="#000000", size=0.5)+
  ylim(-116, 116)+ labs(y = "Confidence (DH1)", x = "Session")+
  theme_minimal()
DH2<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DHCmean2$no, y=DHCmean2$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DHRmean2$no, y=DHRmean2$mean), colour="#2FA524", size=0.5)+ geom_point(aes(x=DHRmean2$no, y=DHRmean2$mean), colour="#2FA524", size=0.5)+geom_errorbar(data=DHRmean2,aes(x=DHRmean2$no, y=DHRmean2$mean, ymin=DHRmean2$min, ymax=DHRmean2$max), width = 0.2, colour="#2FA524")+
  geom_point(aes(x=DHCmean2$no, y=DHCmean2$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DH2)", x = "Session")+
  theme_minimal()
DH3<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DHCmean3$no, y=DHCmean3$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DHRmean3$no, y=DHRmean3$mean), colour="#3192C6", size=0.5)+ geom_point(aes(x=DHRmean3$no, y=DHRmean3$mean), colour="#3192C6", size=0.5)+ geom_errorbar(data=DHRmean3,aes(x=DHRmean3$no, y=DHRmean3$mean, ymin=DHRmean3$min, ymax=DHRmean3$max), width = 0.2, colour="#3192C6")+ 
  geom_point(aes(x=DHCmean3$no, y=DHCmean3$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DH3)", x = "Session")+  
  theme_minimal()
DH4<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DHCmean4$no, y=DHCmean4$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DHRmean4$no, y=DHRmean4$mean), colour="#2D63BF", size=0.5)+ geom_point(aes(x=DHRmean4$no, y=DHRmean4$mean), colour="#2D63BF", size=0.5)+ geom_errorbar(data=DHRmean4,aes(x=DHRmean4$no, y=DHRmean4$mean, ymin=DHRmean4$min, ymax=DHRmean4$max), width = 0.2, colour="#2D63BF")+ 
  geom_point(aes(x=DHCmean4$no, y=DHCmean4$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DH4)", x = "Session")+
  theme_minimal()
DH5<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DHCmean5$no, y=DHCmean5$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DHRmean5$no, y=DHRmean5$mean), colour="#6C2DBF", size=0.5)+ geom_point(aes(x=DHRmean5$no, y=DHRmean5$mean), colour="#6C2DBF", size=0.5)+ geom_errorbar(data=DHRmean5,aes(x=DHRmean5$no, y=DHRmean5$mean, ymin=DHRmean5$min, ymax=DHRmean5$max), width = 0.2, colour="#6C2DBF")+ 
  geom_point(aes(x=DHCmean5$no, y=DHCmean5$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DH5)", x = "Session")+
  theme_minimal()


DH<-ggarrange(
  DH1, DH2,DH3,DH4,DH5,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

####################################################################
#downward confederate trend - Medium R0
downMmean<-aggregate(downM$slope, list(downM$group),mean)
downMmean$R0<-mean(downM$R0)
downMmean$no <- 0
downMmeanT1<-downMmean
downMmeanT1$R0 <- downMmean$R0+(downMmean$x)
downMmeanT1$no <- 1
downMmeanT2<-downMmean
downMmeanT2$R0 <- downMmean$R0+(downMmean$x)*2
downMmeanT2$no <- 2
downMmeanT3<-downMmean
downMmeanT3$R0 <- downMmean$R0+(downMmean$x)*3
downMmeanT3$no <- 3
downMmean<-rbind(downMmean,downMmeanT1,downMmeanT2,downMmeanT3)

DMsd<-aggregate(downM$slope, list(downM$group),sd)
DMsd$x<-format(round(DMsd$x, 2), nsmall = 2)
DMsd$sd <- paste("sd =", DMsd$x)

downMmean$trial <- case_when (downMmean$no==1 ~ "R0",
                              downMmean$no==2 ~ "C1",
                              downMmean$no==3 ~ "C2",
                              downMmean$no==4 ~ "C3",
)

downMmeanR0<-downM %>% group_by(group) %>% summarise_at(vars(R0), funs(mean, sd))
downMmeanR0$sd<-sd(downM$R0)
downMmeanR0$mean<-mean(downM$R0)
downMmeanR0$min<-downMmeanR0$mean-downMmeanR0$sd
downMmeanR0$max<-downMmeanR0$mean+downMmeanR0$sd
downMmeanR0$no <- 0
downMmeanR1<-downM %>% group_by(group) %>% summarise_at(vars(R1), funs(mean, sd))
downMmeanR1$min<-downMmeanR1$mean-downMmeanR1$sd
downMmeanR1$max<-downMmeanR1$mean+downMmeanR1$sd
downMmeanR1$no <- 1
downMmeanR2<-downM %>% group_by(group) %>% summarise_at(vars(R2), funs(mean, sd))
downMmeanR2$min<-downMmeanR2$mean-downMmeanR2$sd
downMmeanR2$max<-downMmeanR2$mean+downMmeanR2$sd
downMmeanR2$no <- 2
downMmeanR3<-downM %>% group_by(group) %>% summarise_at(vars(R3), funs(mean, sd))
downMmeanR3$min<-downMmeanR3$mean-downMmeanR3$sd
downMmeanR3$max<-downMmeanR3$mean+downMmeanR3$sd
downMmeanR3$no <- 3

downMmeanplot<-rbind(downMmeanR0,downMmeanR1,downMmeanR2,downMmeanR3)

downMmeanplot$trial <- case_when (downMmeanplot$no==1 ~ "R0",
                                  downMmeanplot$no==2 ~ "R1",
                                  downMmeanplot$no==3 ~ "R2",
                                  downMmeanplot$no==4 ~ "R3",
)

DMCmean1<-subset(downMmean,downMmean$Group.1 ==1)
DMCmean2<-subset(downMmean,downMmean$Group.1 ==2)
DMCmean3<-subset(downMmean,downMmean$Group.1 ==3)
DMCmean4<-subset(downMmean,downMmean$Group.1 ==4)
DMCmean5<-subset(downMmean,downMmean$Group.1 ==5)

DMRmean1<-subset(downMmeanplot,downMmeanplot$group ==1)
DMRmean2<-subset(downMmeanplot,downMmeanplot$group ==2)
DMRmean3<-subset(downMmeanplot,downMmeanplot$group ==3)
DMRmean4<-subset(downMmeanplot,downMmeanplot$group ==4)
DMRmean5<-subset(downMmeanplot,downMmeanplot$group ==5)

DM1<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DMCmean1$no, y=DMCmean1$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DMRmean1$no, y=DMRmean1$mean), colour="#7AB317", size=0.5)+ geom_point(aes(x=DMRmean1$no, y=DMRmean1$mean), colour="#7AB317", size=0.5)+ geom_errorbar(data=DMRmean1,aes(x=DMRmean1$no, y=DMRmean1$mean, ymin=DMRmean1$min, ymax=DMRmean1$max), width = 0.2, colour="#7AB317")+ 
  geom_point(aes(x=DMCmean1$no, y=DMCmean1$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DM1)", x = "Session")+
  theme_minimal()
DM2<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DMCmean2$no, y=DMCmean2$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DMRmean2$no, y=DMRmean2$mean), colour="#2FA524", size=0.5)+ geom_point(aes(x=DMRmean2$no, y=DMRmean2$mean), colour="#2FA524", size=0.5)+ geom_errorbar(data=DMRmean2,aes(x=DMRmean2$no, y=DMRmean2$mean, ymin=DMRmean2$min, ymax=DMRmean2$max), width = 0.2, colour="#2FA524")+ 
  geom_point(aes(x=DMCmean2$no, y=DMCmean2$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DM2)", x = "Session")+
  theme_minimal()
DM3<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DMCmean3$no, y=DMCmean3$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DMRmean3$no, y=DMRmean3$mean), colour="#3192C6", size=0.5)+ geom_point(aes(x=DMRmean3$no, y=DMRmean3$mean), colour="#3192C6", size=0.5)+ geom_errorbar(data=DMRmean3,aes(x=DMRmean3$no, y=DMRmean3$mean, ymin=DMRmean3$min, ymax=DMRmean3$max), width = 0.2, colour="#3192C6")+ 
  geom_point(aes(x=DMCmean3$no, y=DMCmean3$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DM3)", x = "Session")+
  theme_minimal()



DM<-ggarrange(
  DM1, DM2,DM3,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

####################################################################
#downward confederate trend - Low R0
downLmean<-aggregate(downL$slope, list(downL$group),mean)
downLmean$R0<-mean(downL$R0)
downLmean$no <- 0
downLmeanT1<-downLmean
downLmeanT1$R0 <- downLmean$R0+(downLmean$x)
downLmeanT1$no <- 1
downLmeanT2<-downLmean
downLmeanT2$R0 <- downLmean$R0+(downLmean$x)*2
downLmeanT2$no <- 2
downLmeanT3<-downLmean
downLmeanT3$R0 <- downLmean$R0+(downLmean$x)*3
downLmeanT3$no <- 3
downLmean<-rbind(downLmean,downLmeanT1,downLmeanT2,downLmeanT3)

DLsd<-aggregate(downL$slope, list(downL$group),sd)
DLsd$x<-format(round(DLsd$x, 2), nsmall = 2)
DLsd$sd <- paste("sd =", DLsd$x)

downLmean$trial <- case_when (downLmean$no==1 ~ "R0",
                              downLmean$no==2 ~ "C1",
                              downLmean$no==3 ~ "C2",
                              downLmean$no==4 ~ "C3",
)

downLmeanR0<-downL %>% group_by(group) %>% summarise_at(vars(R0), funs(mean, sd))
downLmeanR0$sd<-sd(downL$R0)
downLmeanR0$mean<-mean(downL$R0)
downLmeanR0$min<-downLmeanR0$mean-downLmeanR0$sd
downLmeanR0$max<-downLmeanR0$mean+downLmeanR0$sd
downLmeanR0$no <- 0
downLmeanR1<-downL %>% group_by(group) %>% summarise_at(vars(R1), funs(mean, sd))
downLmeanR1$min<-downLmeanR1$mean-downLmeanR1$sd
downLmeanR1$max<-downLmeanR1$mean+downLmeanR1$sd
downLmeanR1$no <- 1
downLmeanR2<-downL %>% group_by(group) %>% summarise_at(vars(R2), funs(mean, sd))
downLmeanR2$min<-downLmeanR2$mean-downLmeanR2$sd
downLmeanR2$max<-downLmeanR2$mean+downLmeanR2$sd
downLmeanR2$no <- 2
downLmeanR3<-downL %>% group_by(group) %>% summarise_at(vars(R3), funs(mean, sd))
downLmeanR3$min<-downLmeanR3$mean-downLmeanR3$sd
downLmeanR3$max<-downLmeanR3$mean+downLmeanR3$sd
downLmeanR3$no <- 3

downLmeanplot<-rbind(downLmeanR0,downLmeanR1,downLmeanR2,downLmeanR3)

downLmeanplot$trial <- case_when (downLmeanplot$no==1 ~ "R0",
                                  downLmeanplot$no==2 ~ "R1",
                                  downLmeanplot$no==3 ~ "R2",
                                  downLmeanplot$no==4 ~ "R3",
)

DLCmean1<-subset(downLmean,downLmean$Group.1 ==1)
DLCmean2<-subset(downLmean,downLmean$Group.1 ==2)
DLCmean3<-subset(downLmean,downLmean$Group.1 ==3)
DLCmean4<-subset(downLmean,downLmean$Group.1 ==4)
DLCmean5<-subset(downLmean,downLmean$Group.1 ==5)

DLRmean1<-subset(downLmeanplot,downLmeanplot$group ==1)
DLRmean2<-subset(downLmeanplot,downLmeanplot$group ==2)
DLRmean3<-subset(downLmeanplot,downLmeanplot$group ==3)
DLRmean4<-subset(downLmeanplot,downLmeanplot$group ==4)
DLRmean5<-subset(downLmeanplot,downLmeanplot$group ==5)

DL1<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DLCmean1$no, y=DLCmean1$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DLRmean1$no, y=DLRmean1$mean), colour="#7AB317", size=0.5)+ geom_point(aes(x=DLRmean1$no, y=DLRmean1$mean), colour="#7AB317", size=0.5)+ geom_errorbar(data=DLRmean1,aes(x=DLRmean1$no, y=DLRmean1$mean, ymin=DLRmean1$min, ymax=DLRmean1$max), width = 0.2, colour="#7AB317")+
  geom_point(aes(x=DLCmean1$no, y=DLCmean1$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DL1)", x = "Session")+
  theme_minimal()
DL2<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DLCmean2$no, y=DLCmean2$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DLRmean2$no, y=DLRmean2$mean), colour="#2FA524", size=0.5)+ geom_point(aes(x=DLRmean2$no, y=DLRmean2$mean), colour="#2FA524", size=0.5)+ geom_errorbar(data=DLRmean2,aes(x=DLRmean2$no, y=DLRmean2$mean, ymin=DLRmean2$min, ymax=DLRmean2$max), width = 0.2, colour="#2FA524")+ 
  geom_point(aes(x=DLCmean2$no, y=DLCmean2$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DL2)", x = "Session")+
  theme_minimal()
DL3<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DLCmean3$no, y=DLCmean3$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DLRmean3$no, y=DLRmean3$mean), colour="#3192C6", size=0.5)+ geom_point(aes(x=DLRmean3$no, y=DLRmean3$mean), colour="#3192C6", size=0.5)+ geom_errorbar(data=DLRmean3,aes(x=DLRmean3$no, y=DLRmean3$mean, ymin=DLRmean3$min, ymax=DLRmean3$max), width = 0.2, colour="#3192C6")+ 
  geom_point(aes(x=DLCmean3$no, y=DLCmean3$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DL3)", x = "Session")+
  theme_minimal()
DL4<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=DLCmean4$no, y=DLCmean4$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=DLRmean4$no, y=DLRmean4$mean), colour="#2D63BF", size=0.5)+ geom_point(aes(x=DLRmean4$no, y=DLRmean4$mean), colour="#2D63BF", size=0.5)+ geom_errorbar(data=DLRmean4,aes(x=DLRmean4$no, y=DLRmean4$mean, ymin=DLRmean4$min, ymax=DLRmean4$max), width = 0.2, colour="#2D63BF")+ 
  geom_point(aes(x=DLCmean4$no, y=DLCmean4$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (DL4)", x = "Session")+
  theme_minimal()


DL<-ggarrange(
  DL1, DL2,DL3,DL4,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

####################################################################
#Upward confederate trend - Medium R0
upMmean<-aggregate(upM$slope, list(upM$group),mean)
upMmean$R0<-mean(upM$R0)
upMmean$no <- 0
upMmeanT1<-upMmean
upMmeanT1$R0 <- upMmean$R0+(upMmean$x)
upMmeanT1$no <- 1
upMmeanT2<-upMmean
upMmeanT2$R0 <- upMmean$R0+(upMmean$x)*2
upMmeanT2$no <- 2
upMmeanT3<-upMmean
upMmeanT3$R0 <- upMmean$R0+(upMmean$x)*3
upMmeanT3$no <- 3
upMmean<-rbind(upMmean,upMmeanT1,upMmeanT2,upMmeanT3)

UMsd<-aggregate(upM$slope, list(upM$group),sd)
UMsd$x<-format(round(UMsd$x, 2), nsmall = 2)
UMsd$sd <- paste("sd =", UMsd$x)

upMmean$trial <- case_when (upMmean$no==1 ~ "R0",
                              upMmean$no==2 ~ "C1",
                              upMmean$no==3 ~ "C2",
                              upMmean$no==4 ~ "C3",
)

upMmeanR0<-upM %>% group_by(group) %>% summarise_at(vars(R0), funs(mean, sd))
upMmeanR0$sd<-sd(upM$R0)
upMmeanR0$mean<-mean(upM$R0)
upMmeanR0$min<-upMmeanR0$mean-upMmeanR0$sd
upMmeanR0$max<-upMmeanR0$mean+upMmeanR0$sd
upMmeanR0$no <- 0
upMmeanR1<-upM %>% group_by(group) %>% summarise_at(vars(R1), funs(mean, sd))
upMmeanR1$min<-upMmeanR1$mean-upMmeanR1$sd
upMmeanR1$max<-upMmeanR1$mean+upMmeanR1$sd
upMmeanR1$no <- 1
upMmeanR2<-upM %>% group_by(group) %>% summarise_at(vars(R2), funs(mean, sd))
upMmeanR2$min<-upMmeanR2$mean-upMmeanR2$sd
upMmeanR2$max<-upMmeanR2$mean+upMmeanR2$sd
upMmeanR2$no <- 2
upMmeanR3<-upM %>% group_by(group) %>% summarise_at(vars(R3), funs(mean, sd))
upMmeanR3$min<-upMmeanR3$mean-upMmeanR3$sd
upMmeanR3$max<-upMmeanR3$mean+upMmeanR3$sd
upMmeanR3$no <- 3

upMmeanplot<-rbind(upMmeanR0,upMmeanR1,upMmeanR2,upMmeanR3)

upMmeanplot$trial <- case_when (upMmeanplot$no==1 ~ "R0",
                                  upMmeanplot$no==2 ~ "R1",
                                  upMmeanplot$no==3 ~ "R2",
                                  upMmeanplot$no==4 ~ "R3",
)

UMCmean1<-subset(upMmean,upMmean$Group.1 ==1)
UMCmean2<-subset(upMmean,upMmean$Group.1 ==2)
UMCmean3<-subset(upMmean,upMmean$Group.1 ==3)
UMCmean4<-subset(upMmean,upMmean$Group.1 ==4)
UMCmean5<-subset(upMmean,upMmean$Group.1 ==5)

UMRmean1<-subset(upMmeanplot,upMmeanplot$group ==1)
UMRmean2<-subset(upMmeanplot,upMmeanplot$group ==2)
UMRmean3<-subset(upMmeanplot,upMmeanplot$group ==3)
UMRmean4<-subset(upMmeanplot,upMmeanplot$group ==4)
UMRmean5<-subset(upMmeanplot,upMmeanplot$group ==5)

UM1<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=UMCmean1$no, y=UMCmean1$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=UMRmean1$no, y=UMRmean1$mean), colour="#7AB317", size=0.5)+ geom_point(aes(x=UMRmean1$no, y=UMRmean1$mean), colour="#7AB317", size=0.5)+ geom_errorbar(data=UMRmean1,aes(x=UMRmean1$no, y=UMRmean1$mean, ymin=UMRmean1$min, ymax=UMRmean1$max), width = 0.2, colour="#7AB317")+ 
  geom_point(aes(x=UMCmean1$no, y=UMCmean1$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (UM1)", x = "Session")+
  theme_minimal()
UM2<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=UMCmean2$no, y=UMCmean2$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=UMRmean2$no, y=UMRmean2$mean), colour="#2FA524", size=0.5)+ geom_point(aes(x=UMRmean2$no, y=UMRmean2$mean), colour="#2FA524", size=0.5)+ geom_errorbar(data=UMRmean2,aes(x=UMRmean2$no, y=UMRmean2$mean, ymin=UMRmean2$min, ymax=UMRmean2$max), width = 0.2, colour="#2FA524")+ 
  geom_point(aes(x=UMCmean2$no, y=UMCmean2$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (UM2)", x = "Session")+
  theme_minimal()

UM<-ggarrange(
  UM1, UM2,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

####################################################################
#Upward confederate trend - Low R0
upLmean<-aggregate(upL$slope, list(upL$group),mean)
upLmean$R0<-mean(upL$R0)
upLmean$no <- 0
upLmeanT1<-upLmean
upLmeanT1$R0 <- upLmean$R0+(upLmean$x)
upLmeanT1$no <- 1
upLmeanT2<-upLmean
upLmeanT2$R0 <- upLmean$R0+(upLmean$x)*2
upLmeanT2$no <- 2
upLmeanT3<-upLmean
upLmeanT3$R0 <- upLmean$R0+(upLmean$x)*3
upLmeanT3$no <- 3
upLmean<-rbind(upLmean,upLmeanT1,upLmeanT2,upLmeanT3)

ULsd<-aggregate(upL$slope, list(upL$group),sd)
ULsd$x<-format(round(ULsd$x, 2), nsmall = 2)
ULsd$sd <- paste("sd =", ULsd$x)

upLmean$trial <- case_when (upLmean$no==1 ~ "R0",
                              upLmean$no==2 ~ "C1",
                              upLmean$no==3 ~ "C2",
                              upLmean$no==4 ~ "C3",
)

upLmeanR0<-upL %>% group_by(group) %>% summarise_at(vars(R0), funs(mean, sd))
upLmeanR0$sd<-sd(upL$R0)
upLmeanR0$mean<-mean(upL$R0)
upLmeanR0$min<-upLmeanR0$mean-upLmeanR0$sd
upLmeanR0$max<-upLmeanR0$mean+upLmeanR0$sd
upLmeanR0$no <- 0
upLmeanR1<-upL %>% group_by(group) %>% summarise_at(vars(R1), funs(mean, sd))
upLmeanR1$min<-upLmeanR1$mean-upLmeanR1$sd
upLmeanR1$max<-upLmeanR1$mean+upLmeanR1$sd
upLmeanR1$no <- 1
upLmeanR2<-upL %>% group_by(group) %>% summarise_at(vars(R2), funs(mean, sd))
upLmeanR2$min<-upLmeanR2$mean-upLmeanR2$sd
upLmeanR2$max<-upLmeanR2$mean+upLmeanR2$sd
upLmeanR2$no <- 2
upLmeanR3<-upL %>% group_by(group) %>% summarise_at(vars(R3), funs(mean, sd))
upLmeanR3$min<-upLmeanR3$mean-upLmeanR3$sd
upLmeanR3$max<-upLmeanR3$mean+upLmeanR3$sd
upLmeanR3$no <- 3

upLmeanplot<-rbind(upLmeanR0,upLmeanR1,upLmeanR2,upLmeanR3)

upLmeanplot$trial <- case_when (upLmeanplot$no==1 ~ "R0",
                                  upLmeanplot$no==2 ~ "R1",
                                  upLmeanplot$no==3 ~ "R2",
                                  upLmeanplot$no==4 ~ "R3",
)

ULCmean1<-subset(upLmean,upLmean$Group.1 ==1)
ULCmean2<-subset(upLmean,upLmean$Group.1 ==2)
ULCmean3<-subset(upLmean,upLmean$Group.1 ==3)
ULCmean4<-subset(upLmean,upLmean$Group.1 ==4)
ULCmean5<-subset(upLmean,upLmean$Group.1 ==5)

ULRmean1<-subset(upLmeanplot,upLmeanplot$group ==1)
ULRmean2<-subset(upLmeanplot,upLmeanplot$group ==2)
ULRmean3<-subset(upLmeanplot,upLmeanplot$group ==3)
ULRmean4<-subset(upLmeanplot,upLmeanplot$group ==4)
ULRmean5<-subset(upLmeanplot,upLmeanplot$group ==5)

UL1<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=ULCmean1$no, y=ULCmean1$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=ULRmean1$no, y=ULRmean1$mean), colour="#7AB317", size=0.5)+ geom_point(aes(x=ULRmean1$no, y=ULRmean1$mean), colour="#7AB317", size=0.5)+ geom_errorbar(data=ULRmean1,aes(x=ULRmean1$no, y=ULRmean1$mean, ymin=ULRmean1$min, ymax=ULRmean1$max), width = 0.2, colour="#7AB317")+
  geom_point(aes(x=ULCmean1$no, y=ULCmean1$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (UL1)", x = "Session")+
  theme_minimal()
UL2<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=ULCmean2$no, y=ULCmean2$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=ULRmean2$no, y=ULRmean2$mean), colour="#2FA524", size=0.5)+ geom_point(aes(x=ULRmean2$no, y=ULRmean2$mean), colour="#2FA524", size=0.5)+ geom_errorbar(data=ULRmean2,aes(x=ULRmean2$no, y=ULRmean2$mean, ymin=ULRmean2$min, ymax=ULRmean2$max), width = 0.2, colour="#2FA524")+ 
  geom_point(aes(x=ULCmean2$no, y=ULCmean2$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (UL2)", x = "Session")+
  theme_minimal()
UL3<-ggplot()+geom_hline(yintercept=0, size=0.5)+
  geom_vline(xintercept=0, size=0.5)+
  geom_line(aes(x=ULCmean3$no, y=ULCmean3$R0), colour="#000000", size=0.5)+
  geom_line(aes(x=ULRmean3$no, y=ULRmean3$mean), colour="#3192C6", size=0.5)+ geom_point(aes(x=ULRmean3$no, y=ULRmean3$mean), colour="#3192C6", size=0.5)+ geom_errorbar(data=ULRmean3,aes(x=ULRmean3$no, y=ULRmean3$mean, ymin=ULRmean3$min, ymax=ULRmean3$max), width = 0.2, colour="#3192C6")+
  geom_point(aes(x=ULCmean3$no, y=ULCmean3$R0), colour="#000000", size=0.5)+ 
  ylim(-116, 116)+ labs(y = "Confidence (UL2)", x = "Session")+
  theme_minimal()


UL<-ggarrange(
  UL1, UL2,UL3,
  common.legend = TRUE, legend = "bottom",nrow = 1
)

#Figure 5B
#to combine groups and to calculate mean and sd
downH$grouping <- 1
downM$grouping <- 2
downL$grouping <- 3
upM$grouping <- 4
upL$grouping <- 5
data2 <- rbind(downH,downM,downL,upM,upL)

data2$id <- case_when (data2$grouping==1 & data2$group==1 ~ as.numeric(1),
                      data2$grouping==1 & data2$group==2 ~ as.numeric(2),
                      data2$grouping==1 & data2$group==3 ~ as.numeric(3),
                      data2$grouping==1 & data2$group==4 ~ as.numeric(4),
                      data2$grouping==1 & data2$group==5 ~ as.numeric(5),
                      data2$grouping==2 & data2$group==1 ~ as.numeric(6),
                      data2$grouping==2 & data2$group==2 ~ as.numeric(7),
                      data2$grouping==2 & data2$group==3 ~ as.numeric(8),
                      data2$grouping==3 & data2$group==1 ~ as.numeric(9),
                      data2$grouping==3 & data2$group==2 ~ as.numeric(10),
                      data2$grouping==3 & data2$group==3 ~ as.numeric(11),
                      data2$grouping==3 & data2$group==4 ~ as.numeric(12),
                      data2$grouping==4 & data2$group==1 ~ as.numeric(13),
                      data2$grouping==4 & data2$group==2 ~ as.numeric(14),
                      data2$grouping==5 & data2$group==1 ~ as.numeric(15),
                      data2$grouping==5 & data2$group==2 ~ as.numeric(16),
                      data2$grouping==5 & data2$group==3 ~ as.numeric(17),
                          
)


summary<-ddply(data2,.(grouping,group),summarise,mean=mean(rate),sd=sd(rate))
summary$min <- summary$mean-summary$sd
summary$max <- summary$mean+summary$sd
summary$ID <- seq.int(nrow(summary))

pwttestdata2 <- data2 %>%
  pairwise_t_test(rate~id, p.adjust.method = "bonferroni")

fig5B<-ggplot()+geom_bar(aes(x=summary$ID, y = summary$mean,fill = summary$grouping),stat = "identity") + ylim(-10,15)+
  geom_errorbar(data=summary,aes(x=summary$ID, y=summary$mean, ymin=summary$min, ymax=summary$max), width = 0.2)+
  theme_minimal()

