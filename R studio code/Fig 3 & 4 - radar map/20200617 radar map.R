library(plotly)
library(dplyr)
library(ggplot2)
library(ggpubr)

### Please import data from excel file "Memory conformity Raw data", sheet "Data"

data <- Memory_conformity_Raw_data_

#flip side  -- trial 1,2,3 (base on R0)
pos1 <- subset(data,(data$R0>=0))
neg1 <- subset(data,(data$R0<0))
neg_flip1 <- neg1
neg_flip1$R0 <- -neg_flip1$R0
neg_flip1$C1 <- -neg_flip1$C1
neg_flip1$R1 <- -neg_flip1$R1
flip1 <- rbind(pos1,neg_flip1)

pos2 <- subset(data,(data$R1>=0))
neg2 <- subset(data,(data$R1<0))
neg_flip2 <- neg2
neg_flip2$R1 <- -neg_flip2$R1
neg_flip2$C2 <- -neg_flip2$C2
neg_flip2$R2 <- -neg_flip2$R2
flip2 <- rbind(pos2,neg_flip2)

pos3 <- subset(data,(data$R2>=0))
neg3 <- subset(data,(data$R2<0))
neg_flip3 <- neg3
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

### Group data by R0 and C1 conditions in trial 1 -omitted C1=R0

group1t1 <- subset(flip1,R0>0 & C1<0) 
group2t1 <- subset(flip1,R0>0 & C1>0 & R0>=C1)
group3t1 <- subset(flip1,R0>0 & C1>0 & R0<C1)
group4t1 <- subset(flip1, C1==0 & R0>0)

### Group data by R1 and C2 conditions in trial 2 -omitted C1=R0

group1t2 <- subset(flip2,R1>0 & C2<0) 
group2t2 <- subset(flip2,R1>0 & C2>0 & R1>=C2)
group3t2 <- subset(flip2,R1>0 & C2>0 & R1<C2)
group4t2 <- subset(flip2, C2==0 & R1>0)

###trial 3 -omitted C1=R0
group1t3 <- subset(flip3,R2>0 & C3<0) 
group2t3 <- subset(flip3,R2>0 & C3>0 & R2>=C3)
group3t3 <- subset(flip3,R2>0 & C3>0 & R2<C3)
group4t3 <- subset(flip3, C3==0 & R2>0)

### Setting up plots for trial 1 

### Trial 1 group 1 - R0>0 & C1<0
#count
countt1g1 <- as.data.frame(table(cut(group1t1$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt1g1$percent <- countt1g1$Freq/521

datat1g1u <- group1t1$R1 - group1t1$R0 # Calculate R1-R0 (y-axis)
datat1g1d <- group1t1$C1 - group1t1$R0 # Calculate C1-R0 (x-axis) 
fitt1g1 <- lm(datat1g1u ~ 0+datat1g1d) # Fit with a line that passes through the origin
group1at1slope <-summary(fitt1g1)$coefficients[1]
group1at1slope1<-group1at1slope*-200

### Trial 1 group 2  
countt1g2 <- as.data.frame(table(cut(group2t1$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt1g2$percent <- countt1g2$Freq/1739

datat1g2u <- group2t1$R1 - group2t1$R0
datat1g2d <- group2t1$C1 - group2t1$R0
fitt1g2 <- lm(datat1g2u ~ 0+datat1g2d)
group2at1slope <-summary(fitt1g2)$coefficients[1]
group2at1slope1<-group2at1slope*-200

### Trial 1 group 3
countt1g3 <- as.data.frame(table(cut(group3t1$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt1g3$percent <- countt1g3$Freq/1079

datat1g3u <- group3t1$R1 - group3t1$R0
datat1g3d <- group3t1$C1 - group3t1$R0
fitt1g3 <- lm(datat1g3u ~ 0+datat1g3d)
group3at1slope <-summary(fitt1g3)$coefficients[1]
group3at1slope2<-group3at1slope*200

### Trial 1 group 4 
countt1g4 <- as.data.frame(table(cut(group4t1$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt1g4$percent <- countt1g4$Freq/21

datat1g4u <- group4t1$R1 - group4t1$R0
datat1g4d <- group4t1$C1 - group4t1$R0
fitt1g4 <- lm(datat1g4u ~ 0+datat1g4d)
group4at1slope <-summary(fitt1g4)$coefficients[1]
group4at1slope1<-group4at1slope*-200

#plot
fig <- plot_ly(type = 'scatterpolar', r = countt1g1$Freq, fill = 'toself', name="C1 opp R0")  %>% 
  add_trace(type = 'scatterpolar', r = countt1g2$Freq, fill = 'toself', name="C1 < R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt1g3$Freq, fill =  'toself',  name="C1 > R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt1g4$Freq, fill =  'toself',  name="C1 = 0") %>% 
  layout(polar = list(radialaxis = list(visible = T,showticklabels = FALSE, range = c(0,400))))

### Setting up plots for trial 2

### Trial 2 group 1 - R0>0 & C1<0
#count
countt2g1 <- as.data.frame(table(cut(group1t2$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt2g1$percent <- countt2g1$Freq/647

datat2g1u <- group1t2$R2 - group1t2$R1
datat2g1d <- group1t2$C2 - group1t2$R1
fitt2g1 <- lm(datat2g1u ~ 0+datat2g1d)
group1at2slope <-summary(fitt2g1)$coefficients[1]
group1at2slope1<-group1at2slope*-200

### Trial 2 group 2 
countt2g2 <- as.data.frame(table(cut(group2t2$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt2g2$percent <- countt2g2$Freq/1774

datat2g2u <- group2t2$R2 - group2t2$R1
datat2g2d <- group2t2$C2 - group2t2$R1
fitt2g2 <- lm(datat2g2u ~ 0+datat2g2d)
group2at2slope <-summary(fitt2g2)$coefficients[1]
group2at2slope1<-group2at2slope*-200

### Trial 2 group 3
countt2g3 <- as.data.frame(table(cut(group3t2$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt2g3$percent <- countt2g3$Freq/940

datat2g3u <- group3t2$R2 - group3t2$R1
datat2g3d <- group3t2$C2 - group3t2$R1
fitt2g3 <- lm(datat2g3u ~ 0+datat2g3d)
group3at2slope <-summary(fitt2g3)$coefficients[1]
group3at2slope2<-group3at2slope*200

### Trial 2 group 4
countt2g4 <- as.data.frame(table(cut(group4t2$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt2g4$percent <- countt2g4$Freq/15

datat2g4u <- group4t2$R2 - group4t2$R1
datat2g4d <- group4t2$C2 - group4t2$R1
fitt2g4 <- lm(datat2g4u ~ 0+datat2g4d)
group4at2slope <-summary(fitt2g4)$coefficients[1]
group4at2slope1<-group4at2slope*-200

#plot
fig2 <- plot_ly(type = 'scatterpolar', r = countt2g1$Freq, fill = 'toself', name="C1 opp R0")  %>% 
  add_trace(type = 'scatterpolar', r = countt2g2$Freq, fill = 'toself', name="C1 < R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt2g3$Freq, fill =  'toself',  name="C1 > R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt2g4$Freq, fill =  'toself',  name="C1 = 0") %>% 
  layout(polar = list(radialaxis = list(visible = T,showticklabels = FALSE, range = c(0,400))))

### Setting up plots for trial 3

### Trial 3 group 1 - R0>0 & C1<0
#count
countt3g1 <- as.data.frame(table(cut(group1t3$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt3g1$percent <- countt3g1$Freq/899

datat3g1u <- group1t3$R3 - group1t3$R2
datat3g1d <- group1t3$C3 - group1t3$R2
fitt3g1 <- lm(datat3g1u ~ 0+datat3g1d)
group1at3slope <-summary(fitt3g1)$coefficients[1]
group1at3slope1<-group1at3slope*-200

### Trial 3 group 2  
countt3g2 <- as.data.frame(table(cut(group2t3$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt3g2$percent <- countt3g2$Freq/1538

datat3g2u <- group2t3$R3 - group2t3$R2
datat3g2d <- group2t3$C3 - group2t3$R2
fitt3g2 <- lm(datat3g2u ~ 0+datat3g2d)
group2at3slope <-summary(fitt3g2)$coefficients[1]
group2at3slope1<-group2at3slope*-200

### Trial 3 group 3  
countt3g3 <- as.data.frame(table(cut(group3t3$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt3g3$percent <- countt3g3$Freq/916

datat3g3u <- group3t3$R3 - group3t3$R2
datat3g3d <- group3t3$C3 - group3t3$R2
fitt3g3 <- lm(datat3g3u ~ 0+datat3g3d)
group3at3slope <-summary(fitt3g3)$coefficients[1]
group3at3slope2<-group3at3slope*200

### Trial 3 group 4 
countt3g4 <- as.data.frame(table(cut(group4t3$angle, seq(0,360,10),include.lowest = TRUE, right=FALSE)))
countt3g4$percent <- countt3g4$Freq/12

datat3g4u <- group4t3$R3 - group4t3$R2
datat3g4d <- group4t3$C3 - group4t3$R2
fitt3g4 <- lm(datat3g4u ~ 0+datat3g4d)
group4at3slope <-summary(fitt3g4)$coefficients[1]
group4at3slope1<-group4at3slope*-200

#plot
fig3 <- plot_ly(type = 'scatterpolar', r = countt3g1$Freq, fill = 'toself', name="C1 opp R0")  %>% 
  add_trace(type = 'scatterpolar', r = countt3g2$Freq, fill = 'toself', name="C1 < R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt3g3$Freq, fill =  'toself',  name="C1 > R0 sameside") %>% 
  add_trace(type = 'scatterpolar', r = countt3g4$Freq, fill =  'toself',  name="C1 = 0") %>% 
  layout(polar = list(radialaxis = list(visible = T,showticklabels = FALSE, range = c(0,400))))

