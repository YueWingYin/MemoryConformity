library(plotly)
library(ggplot2)
library(dplyr)
library(akima)
library(reshape2)
library(party)

data <- Memory_conformity_Raw_data_

#flip side for more convenient sorting 
pos <- subset(data,(data$R0>0))
neg <- subset(data,(data$R0<0))
neg_flip1 <- neg
neg_flip1$R0 <- -neg_flip1$R0
neg_flip1$C1 <- -neg_flip1$C1
neg_flip1$R1 <- -neg_flip1$R1
neg_flip1$C2 <- -neg_flip1$C2
neg_flip1$R2 <- -neg_flip1$R2
neg_flip1$C3 <- -neg_flip1$C3
neg_flip1$R3 <- -neg_flip1$R3
flip1 <- rbind(pos,neg_flip1)

#Taking out points which the participant saw an opposite value -- trial 1 
Opp1 <- subset(flip1, flip1$R0*flip1$C1 <0 & flip1$R0 != 0 & flip1$C1!= 0)
Opp1$CI1 <- (Opp1$R1-Opp1$R0) / (Opp1$C1-Opp1$R0)
Opp2 <- subset(flip1, flip1$R0*flip1$C1 <0 & flip1$R0*flip1$C2 <0  & flip1$R0 != 0 & flip1$C1!= 0 & flip1$R1 != 0 & flip1$C2!= 0 & flip1$R2 != 0)
Opp2$CI2 <- (Opp2$R2-Opp2$R1) / (Opp2$C2-Opp2$R1)
Opp3 <- subset(flip1, flip1$R0*flip1$C1 <0 & flip1$R0*flip1$C2 <0 & flip1$R0*flip1$C3 <0 & flip1$R0 != 0 & flip1$C1!= 0 & flip1$R1 != 0 & flip1$C2!= 0 & flip1$R2 != 0 & flip1$C3!= 0 & flip1$R3 != 0)
Opp3$CI3 <- (Opp3$R3-Opp3$R2) / (Opp3$C3-Opp3$R2)

##trial 1 -- counting number of shift & no shift..... excluded R1 = 0
T1Shift <- subset (Opp1, Opp1$R0*Opp1$R1 <0)
T1NoShift <- subset (Opp1, Opp1$R0*Opp1$R1 >0)
T1<-rbind(T1Shift,T1NoShift)

CountT1Shift <- count(T1Shift)
CountT1NoShift <- count(T1NoShift)

for(i in 1:517){
  if(T1$R0[i]*T1$R1[i]<0){T1$Shift[i]<-1}
  else{T1$Shift[i]<-0}}

##trial 2 -- counting number of shift & no shift..... excluded R2 = 0
T2Shift <- subset (Opp2, Opp2$R0*Opp2$R2 <0)
T2NoShift <- subset (Opp2, Opp2$R0*Opp2$R2 >0)
T2 <-rbind(T2Shift,T2NoShift)

CountT2Shift <- count(T2Shift)
CountT2NoShift <- count(T2NoShift)

for(i in 1:370){
  if(T2$R0[i]*T2$R2[i]<0){T2$Shift[i]<-1}
  else{T2$Shift[i]<-0}}

##trial 3 -- counting number of shift & no shift..... excluded R3 = 0
T3Shift <- subset (Opp3, Opp3$R2*Opp3$R0 <0)
T3NoShift <- subset (Opp3, Opp3$R2*Opp3$R0 >0)
T3 <-rbind(T3Shift,T3NoShift)

CountT3Shift <- count(T3Shift)
CountT3NoShift <- count(T3NoShift)

for(i in 1:297){
  if(T3$R0[i]*T3$R3[i]<0){T3$Shift[i]<-1}
  else{T3$Shift[i]<-0}}

#calculating percentage -- trial 1
T1Shiftper <- as.numeric((CountT1Shift/(CountT1Shift+CountT1NoShift) *100))
T1NoShiftper <- as.numeric(((CountT1NoShift/(CountT1Shift+CountT1NoShift) *100)))

#calculating percentage -- trial 2
T2Shiftper <- as.numeric(CountT2Shift/(CountT2Shift+CountT2NoShift) *100)
T2NoShiftper <- as.numeric((CountT2NoShift/(CountT2Shift+CountT2NoShift) *100))

#calculating percentage -- trial 3
T3Shiftper <- as.numeric(CountT3Shift/(CountT3Shift+CountT3NoShift) *100)
T3NoShiftper <- as.numeric((CountT3NoShift/(CountT3Shift+CountT3NoShift) *100))

#grouping data to shift and no-shift group
Shiftall <- rbind(T1Shiftper, T2Shiftper, T3Shiftper)
NoShiftall <-rbind(T1NoShiftper,T2NoShiftper,T3NoShiftper)

#Preparing for the figure
y <- c('0','20','40','60','80','100')
x <- c('Session 1','Session 2','Session 3')
y1 <- Shiftall
y2 <- NoShiftall
datashift <- data.frame(x, y1, y2)

#Plotting Figure 2A
fig2a <- plot_ly(datashift, x = ~x, y = ~y1, type = 'bar', name = 'Shift',marker = list(color='rgba(127, 225, 0, 1)'))
fig2a <- fig2a %>% add_trace(y = ~y2, name = 'No Shift',marker = list(color='rgba(223,30,38,1)'))
fig2a <- fig2a %>% layout(yaxis = list(title = 'Percentage'),xaxis = list(title = 'Confederate Session'), barmode = 'stack')

#------------------------------------------------------------------------------------------#
#Figure 2B
#Classifying CI in trial 1

shiftcount <- length(which(T1$Shift==1))
noshiftcount <- length(which(T1$Shift==0))

T1$binCI1 <- case_when (0<T1$CI1 & T1$CI1 <1 ~"Under Conformity",
                        T1$CI1<0 ~"Anti Conformity",
                        T1$CI1>1 ~"Over Conformity",
                        T1$CI1==1 ~"Perfect Conformity",
                        T1$R1 == T1$C1 & T1$R0 == T1$C1~"Perfect Conformity",
                        T1$CI1 ==0 ~"No Conformity",
)

cc4 <- count(T1, T1$Shift, T1$binCI1)
cc4$nn <-case_when (cc4[,1] == 0 ~ noshiftcount,
                    cc4[,1] == 1 ~ shiftcount)

cc4$prop <- cc4$n/cc4$nn
#------------------------------------------------------------------------------------------#
#Classifying CI in trial 2

shiftcount2 <- length(which(T2$Shift==1))
noshiftcount2 <- length(which(T2$Shift==0))

T2$binCI2 <- case_when (0<T2$CI2 & T2$CI2 <1 ~"Under Conformity",
                             T2$CI2<0 ~"Anti Conformity",
                             T2$CI2>1 ~"Over Conformity",
                             T2$CI2==1 ~"Perfect Conformity",
                             T2$R2 == T2$C2 & T2$R1 == T2$C2~"Perfect Conformity",
                             T2$CI2 ==0 ~"No Conformity",
)

cc5 <- count(T2, T2$Shift, T2$binCI2)
cc5$nn <-case_when (cc5[,1] == 0 ~ noshiftcount2,
                    cc5[,1] == 1 ~ shiftcount2)

cc5$prop <- cc5$n/cc5$nn
#------------------------------------------------------------------------------------------#
#Classifying CI in trial 3
shiftcount3 <- length(which(T3$Shift==1))
noshiftcount3 <- length(which(T3$Shift==0))

T3$binCI3 <- case_when (0<T3$CI3 & T3$CI3 <1 ~"Under Conformity",
                             T3$CI3<0 ~"Anti Conformity",
                             T3$CI3>1 ~"Over Conformity",
                             T3$CI3==1 ~"Perfect Conformity",
                             T3$R3 == T3$C3 & T3$R2 == T3$C3~"Perfect Conformity",
                             T3$CI3 ==0 ~"No Conformity",
)

cc6 <- count(T3, T3$Shift, T3$binCI3)
cc6$nn <-case_when (cc6[,1] == 0 ~ noshiftcount3,
                    cc6[,1] == 1 ~ shiftcount3)

cc6$prop <- cc6$n/cc6$nn

#------------------------------------------------------------------------------------------#
#Plotting Figure 2B
set1 <- c("mediumblue","gold4","orangered","orange","gold")
fig2ballt1 <-plot_ly(x = ~cc4$`T1$Shift`, y = ~cc4$prop, color = ~cc4$`T1$binCI1`, colors = set1) %>%
  add_bars() %>%
  layout(barmode = "stack", yaxis = list(title="Percentage of subject-video (%)",ticktext=y, tickvals=list(0,0.2,0.4,0.6,0.8,1)), xaxis = list(title="T1",ticktext = x, tickvals = list(0,1)))

fig2ballt2 <-plot_ly(x = ~cc5$`T2$Shift`, y = ~cc5$prop, color = ~cc5$`T2$binCI2`, colors = set1) %>%
  add_bars() %>%
  layout(barmode = "stack", yaxis = list(title="Percentage of subject-video (%)",ticktext=y, tickvals=list(0,0.2,0.4,0.6,0.8,1)), xaxis = list(title="T2",ticktext = x, tickvals = list(0,1)))

fig2ballt3 <-plot_ly(x = ~cc6$`T3$Shift`, y = ~cc6$prop, color = ~cc6$`T3$binCI3`, colors = set1) %>%
  add_bars() %>%
  layout(barmode = "stack", yaxis = list(title="Percentage of subject-video (%)",ticktext=y, tickvals=list(0,0.2,0.4,0.6,0.8,1)), xaxis = list(title="T3",ticktext = x, tickvals = list(0,1)))
