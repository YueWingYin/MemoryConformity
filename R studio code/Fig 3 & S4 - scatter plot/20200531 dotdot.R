library(plotly)
packageVersion('plotly')

### Please import data from excel file "Memory conformity Raw data", sheet "Data"

data <- Memory_conformity_Raw_data_

### Group data by R0 and C1 conditions in trial 1 

group1at1 <- subset(data,R0>0 & C1<0) 
group1bt1 <- subset(data,R0<0 & C1>0)
group1t1<-rbind(group1at1,group1bt1) # C1 on opposite side of R0 and less confident than or as confident as R0

group2at1 <- subset(data,R0>0 & C1>0 & R0>=C1)
group2bt1 <- subset(data,R0<0 & C1<0 & R0<=C1)
group2t1<-rbind(group2at1,group2bt1) # C1 on same side of R0 and less confident than or as confident as R0

group3at1 <- subset(data,R0>0 & C1>0 & R0<C1)
group3bt1 <- subset(data,R0<0 & C1<0 & R0>C1)
group3t1<-rbind(group3at1,group3bt1) # C1 on same side of R0 and more confident than R0

group4at1 <- subset(data,R0==0 & C1>0)
group4bt1 <- subset(data,R0==0 & C1<0)
group4t1 <- rbind(group4at1,group4bt1) # R0 = 0

group5at1 <- subset(data, C1==0 & R0>0)
group5bt1 <-subset(data, C1==0 & R0<0)
group5t1 <- rbind(group5at1,group5bt1) # C1 = 0

group4comparet1 <-rbind(group1t1,group2t1,group3t1,group5t1)

### Group data by R1 and C2 conditions in trial 2 

group1at2 <- subset(data,R1>0 & C2<0) 
group1bt2 <- subset(data,R1<0 & C2>0)
group1t2<-rbind(group1at2,group1bt2) # C2 on opposite side of R1 and less confident than or as confident as R1

group2at2 <- subset(data,R1>0 & C2>0 & R1>=C2)
group2bt2 <- subset(data,R1<0 & C2<0 & R1<=C2)
group2t2<-rbind(group2at2,group2bt2) # C2 on same side of R1 and less confident than or as confident as R1

group3at2 <- subset(data,R1>0 & C2>0 & R1<C2)
group3bt2 <- subset(data,R1<0 & C2<0 & R1>C2)
group3t2<-rbind(group3at2,group3bt2) # C2 on same side of R1 and more confident than R1

group4at2 <- subset(data,R1==0 & C2>0)
group4bt2 <- subset(data,R1==0 & C2<0)
group4t2 <- rbind(group4at2,group4bt2) # R1 = 0

group5at2 <- subset(data, C2==0 & R1>0)
group5bt2 <-subset(data, C2==0 & R1<0)
group5t2 <- rbind(group5at2,group5bt2) # C2 = 0

group4comparet2 <-rbind(group1t2,group2t2,group3t2,group5t2)

###trial 3
group1at3 <- subset(data,R2>0 & C3<0) 
group1bt3 <- subset(data,R2<0 & C3>0)
group1t3<-rbind(group1at3,group1bt3) # C3 on opposite side of R2 and less confident than or as confident as R2

group2at3 <- subset(data,R2>0 & C3>0 & R2>=C3)
group2bt3 <- subset(data,R2<0 & C3<0 & R2<=C3)
group2t3<-rbind(group2at3,group2bt3) # C3 on same side of R2 and less confident than or as confident as R2

group3at3 <- subset(data,R2>0 & C3>0 & R2<C3)
group3bt3 <- subset(data,R2<0 & C3<0 & R2>C3)
group3t3<-rbind(group3at3,group3bt3) # C3 on same side of R2 and more confident than R2

group4at3 <- subset(data,R2==0 & C3>0)
group4bt3 <- subset(data,R2==0 & C3<0)
group4t3 <- rbind(group4at3,group4bt3) # R2 = 0

group5at3 <- subset(data, C3==0 & R2>0)
group5bt3 <-subset(data, C3==0 & R2<0)
group5t3 <- rbind(group5at3,group5bt3) # C3 = 0

group4comparet3 <-rbind(group1t3,group2t3,group3t3,group5t3)


### Setting up plots for trial 1

### Trial 1 group 1
datat1g1au <- group1t1$R1 - group1t1$R0 # Calculate R1-R0 (y-axis)
datat1g1ad <- group1t1$C1 - group1t1$R0 # Calculate C1-R0 (x-axis) 
fitt1g1 <- lm(datat1g1au ~ 0+datat1g1ad) # Fit with a line that passes through the origin
slopet1g1 <- summary(fitt1g1)$coefficients[1]
slopeAt1g1<-slopet1g1*-230
slopeBt1g1<-slopet1g1*230

### Trial 1 group 2
datat1g2au <- group2t1$R1 - group2t1$R0
datat1g2ad <- group2t1$C1 - group2t1$R0
fitt1g2 <- lm(datat1g2au ~ 0+datat1g2ad)
slopet1g2 <- summary(fitt1g2)$coefficients[1]
slopeAt1g2<-slopet1g2*-230
slopeBt1g2<-slopet1g2*230

### Trial 1 group 3
datat1g3au <- group3t1$R1 - group3t1$R0
datat1g3ad <- group3t1$C1 - group3t1$R0
fitt1g3 <- lm(datat1g3au ~ 0+datat1g3ad)
slopet1g3 <- summary(fitt1g3)$coefficients[1]
slopeAt1g3<-slopet1g3*-230
slopeBt1g3<-slopet1g3*230

### Trial 1 group 4
datat1g4au <- group4t1$R1 - group4t1$R0
datat1g4ad <- group4t1$C1 - group4t1$R0
fitt1g4 <- lm(datat1g4au ~ 0+datat1g4ad)
slopet1g4 <- summary(fitt1g4)$coefficients[1]
slopeAt1g4<-slopet1g4*-230
slopeBt1g4<-slopet1g4*230

datat1g4aucompare <- group4comparet1$R1 - group4comparet1$R0
datat1g4adcompare <- group4comparet1$C1 - group4comparet1$R0
fitt1g4compare <- lm(datat1g4aucompare ~ 0+datat1g4adcompare)
slopet1g4compare <- summary(fitt1g4compare)$coefficients[1]
slopeAt1g4compare<-slopet1g4compare*-230
slopeBt1g4compare<-slopet1g4compare*230


### Trial 1 group 5
datat1g5au <- group5t1$R1 - group5t1$R0
datat1g5ad <- group5t1$C1 - group5t1$R0
fitt1g5 <- lm(datat1g5au ~ 0+datat1g5ad)
slopet1g5 <- summary(fitt1g5)$coefficients[1]
slopeAt1g5<-slopet1g5*-230
slopeBt1g5<-slopet1g5*230


### Setting up plots for trial 2

### Trial 2 group 1
datat2g1au <- group1t2$R2 - group1t2$R1
datat2g1ad <- group1t2$C2 - group1t2$R1
fitt2g1 <- lm(datat2g1au ~ 0+datat2g1ad)
slopet2g1 <- summary(fitt2g1)$coefficients[1]
slopeAt2g1<-slopet2g1*-230
slopeBt2g1<-slopet2g1*230

### Trial 2 group 2
datat2g2au <- group2t2$R2 - group2t2$R1
datat2g2ad <- group2t2$C2 - group2t2$R1
fitt2g2 <- lm(datat2g2au ~ 0+datat2g2ad)
slopet2g2 <- summary(fitt2g2)$coefficients[1]
slopeAt2g2<-slopet2g2*-230
slopeBt2g2<-slopet2g2*230

### Trial 2 group 3
datat2g3au <- group3t2$R2 - group3t2$R1
datat2g3ad <- group3t2$C2 - group3t2$R1
fitt2g3 <- lm(datat2g3au ~ 0+datat2g3ad)
slopet2g3 <- summary(fitt2g3)$coefficients[1]
slopeAt2g3<-slopet2g3*-230
slopeBt2g3<-slopet2g3*230

### Trial 2 group 4
datat2g4au <- group4t2$R2 - group4t2$R1
datat2g4ad <- group4t2$C2 - group4t2$R1
fitt2g4 <- lm(datat2g4au ~ 0+datat2g4ad)
slopet2g4 <- summary(fitt2g4)$coefficients[1]
slopeAt2g4<-slopet2g4*-230
slopeBt2g4<-slopet2g4*230

datat2g4aucompare <- group4comparet2$R2 - group4comparet2$R1
datat2g4adcompare <- group4comparet2$C2 - group4comparet2$R1
fitt2g4compare <- lm(datat2g4aucompare ~ 0+datat2g4adcompare)
slopet2g4compare <- summary(fitt2g4compare)$coefficients[1]
slopeAt2g4compare<-slopet2g4compare*-230
slopeBt2g4compare<-slopet2g4compare*230

### Trial 2 group 5
datat2g5au <- group5t2$R2 - group5t2$R1
datat2g5ad <- group5t2$C2 - group5t2$R1
fitt2g5 <- lm(datat2g5au ~ 0+datat2g5ad)
slopet2g5 <- summary(fitt2g5)$coefficients[1]
slopeAt2g5<-slopet2g5*-230
slopeBt2g5<-slopet2g5*230


### Setting up plots for trial 3

### Trial 3 group 1
datat3g1au <- group1t3$R3 - group1t3$R2
datat3g1ad <- group1t3$C3 - group1t3$R2
fitt3g1 <- lm(datat3g1au ~ 0+datat3g1ad)
slopet3g1 <- summary(fitt3g1)$coefficients[1]
slopeAt3g1<-slopet3g1*-230
slopeBt3g1<-slopet3g1*230

### Trial 3 group 2
datat3g2au <- group2t3$R3 - group2t3$R2
datat3g2ad <- group2t3$C3 - group2t3$R2
fitt3g2 <- lm(datat3g2au ~ 0+datat3g2ad)
slopet3g2 <- summary(fitt3g2)$coefficients[1]
slopeAt3g2<-slopet3g2*-230
slopeBt3g2<-slopet3g2*230

### Trial 3 group 3
datat3g3au <- group3t3$R3 - group3t3$R2
datat3g3ad <- group3t3$C3 - group3t3$R2
fitt3g3 <- lm(datat3g3au ~ 0+datat3g3ad)
slopet3g3 <- summary(fitt3g3)$coefficients[1]
slopeAt3g3<-slopet3g3*-230
slopeBt3g3<-slopet3g3*230

### Trial 3 group 4
datat3g4au <- group4t3$R3 - group4t3$R2
datat3g4ad <- group4t3$C3 - group4t3$R2
fitt3g4 <- lm(datat3g4au ~ 0+datat3g4ad)
slopet3g4 <- summary(fitt3g4)$coefficients[1]
slopeAt3g4<-slopet3g4*-230
slopeBt3g4<-slopet3g4*230

datat3g4aucompare <- group4comparet3$R3 - group4comparet3$R2
datat3g4adcompare <- group4comparet3$C3 - group4comparet3$R2
fitt3g4compare <- lm(datat3g4aucompare ~ 0+datat3g4adcompare)
slopet3g4compare <- summary(fitt3g4compare)$coefficients[1]
slopeAt3g4compare<-slopet3g4compare*-230
slopeBt3g4compare<-slopet3g4compare*230

### Trial 3 group 5
datat3g5au <- group5t3$R3 - group5t3$R2
datat3g5ad <- group5t3$C3 - group5t3$R2
fitt3g5 <- lm(datat3g5au ~ 0+datat3g5ad)
slopet3g5 <- summary(fitt3g5)$coefficients[1]
slopeAt3g5<-slopet3g5*-230
slopeBt3g5<-slopet3g5*230


### Generate plots

### Trial 1
t1g1 <-group1t1%>%
  plot_ly(x = ~datat1g1ad) %>%
  add_markers(y = ~datat1g1au) %>%
  add_markers(x=~group1at1$C1 - group1at1$R0, y=~group1at1$R1 - group1at1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group1bt1$C1 - group1bt1$R0, y=~group1bt1$R1 - group1bt1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y= slopeAt1g1, yend = slopeBt1g1, mode = 'line', line = list(color = 'rgb(255, 65, 54)', visible = TRUE)) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-210", "-100", "0", "100", "210"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t1g2 <-group2t1%>%
  plot_ly(x = ~datat1g2ad) %>%
  add_markers(y = ~datat1g2au) %>%
  add_markers(x=~group2at1$C1 - group2at1$R0, y=~group2at1$R1 - group2at1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group2bt1$C1 - group2bt1$R0, y=~group2bt1$R1 - group2bt1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt1g2, yend = slopeBt1g2, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  #add_segments(x= -210, xend = 210, y = slopeAt1g2A, yend = slopeBt1g2A, name = 'slope', mode = 'line',  line=list(color = 'rgb(180, 180, 180)', dash = 'dot'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t1g3 <-group3t1%>%
  plot_ly(x = ~datat1g3ad) %>%
  add_markers(y = ~datat1g3au) %>%
  add_markers(x=~group3at1$C1 - group3at1$R0, y=~group3at1$R1 - group3at1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group3bt1$C1 - group3bt1$R0, y=~group3bt1$R1 - group3bt1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt1g3, yend = slopeBt1g3, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t1g4 <-group4t1%>%
  plot_ly(x = ~datat1g4ad) %>%
  add_markers(y = ~datat1g4au) %>%
  add_markers(x=~group4at1$C1 - group4at1$R0, y=~group4at1$R1 - group4at1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group4bt1$C1 - group4bt1$R0, y=~group4bt1$R1 - group4bt1$R0, type = 'scatter', mode = 'markers', marker = list(color =  'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt1g4, yend = slopeBt1g4, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t1g5 <-group5t1%>%
  plot_ly(x = ~datat1g5ad) %>%
  add_markers(y = ~datat1g5au) %>%
  add_markers(x=~group5at1$C1 - group5at1$R0, y=~group5at1$R1 - group5at1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group5bt1$C1 - group5bt1$R0, y=~group5bt1$R1 - group5bt1$R0, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt1g5, yend = slopeBt1g5, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)


### Trial 2
t2g1 <-group1t2%>%
  plot_ly(x = ~datat2g1ad) %>%
  add_markers(y = ~datat2g1au) %>%
  add_markers(x=~group1at2$C2 - group1at2$R1, y=~group1at2$R2 - group1at2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group1bt2$C2 - group1bt2$R1, y=~group1bt2$R2 - group1bt2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y= slopeAt2g1, yend = slopeBt2g1, mode = 'line', line = list(color = 'rgb(255, 65, 54)', visible = TRUE)) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t2g2 <-plot_ly(x=~group2at2$C2 - group2at2$R1, y=~group2at2$R2 - group2at2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group2bt2$C2 - group2bt2$R1, y=~group2bt2$R2 - group2bt2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt2g2, yend = slopeBt2g2, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t2g3 <-plot_ly(x=~group3at2$C2 - group3at2$R1, y=~group3at2$R2 - group3at2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group3bt2$C2 - group3bt2$R1, y=~group3bt2$R2 - group3bt2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt2g3, yend = slopeBt2g3, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t2g4 <-plot_ly(x=~group4at2$C2 - group4at2$R1, y=~group4at2$R2 - group4at2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group4bt2$C2 - group4bt2$R1, y=~group4bt2$R2 - group4bt2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt2g4, yend = slopeBt2g4, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  #add_segments(x= -200, xend = 200, y = slopeAt2g4compare, yend = slopeBt2g4compare, name = 'slope', mode = 'line', line=list(color = 'rgb(180, 180, 180)', dash = 'dot'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-210, -100, 0, 100, 210),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t2g5 <-plot_ly(x=~group5at2$C2 - group5at2$R1, y=~group5at2$R2 - group5at2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group5bt2$C2 - group5bt2$R1, y=~group5bt2$R2 - group5bt2$R1, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt2g5, yend = slopeBt2g5, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)


### Trial 3
t3g1 <-plot_ly(x=~group1at3$C3 - group1at3$R2, y=~group1at3$R3 - group1at3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group1bt3$C3 - group1bt3$R2, y=~group1bt3$R3 - group1bt3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y= slopeAt3g1, yend = slopeBt3g1, mode = 'line', line = list(color = 'rgb(255, 65, 54)', visible = TRUE)) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t3g2 <-plot_ly(x=~group2at3$C3 - group2at3$R2, y=~group2at3$R3 - group2at3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group2bt3$C3 - group2bt3$R2, y=~group2bt3$R3 - group2bt3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt3g2, yend = slopeBt3g2, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t3g3 <-plot_ly(x=~group3at3$C3 - group3at3$R2, y=~group3at3$R3 - group3at3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group3bt3$C3 - group3bt3$R2, y=~group3bt3$R3 - group3bt3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments( x= -210, xend = 210, y = slopeAt3g3, yend = slopeBt3g3, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t3g4 <-plot_ly(x=~group4at3$C3 - group4at3$R2, y=~group4at3$R3 - group4at3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group4bt3$C3 - group4bt3$R2, y=~group4bt3$R3 - group4bt3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt3g4, yend = slopeBt3g4, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  #add_segments(x= -210, xend = 210, y = slopeAt3g4compare, yend = slopeBt3g4compare, name = 'slope', mode = 'line', line=list(color = 'rgb(180, 180, 180)', dash = 'dot'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)

t3g5 <-plot_ly(x=~group5at3$C3 - group5at3$R2, y=~group5at3$R3 - group5at3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 230, 160)')) %>%
  add_markers(x=~group5bt3$C3 - group5bt3$R2, y=~group5bt3$R3 - group5bt3$R2, type = 'scatter', mode = 'markers', marker = list(color = 'rgb(50, 160, 230)')) %>%
  add_segments(x = -210, xend = 210, y = -210, yend = 210, name = 'diagonal', color = I('black'), visible = TRUE) %>%
  add_segments(x= -210, xend = 210, y = slopeAt3g5, yend = slopeBt3g5, name = 'slope', mode = 'line', line=list(color = 'rgb(255, 65, 54)'), visible = TRUE) %>%
  layout(xaxis = list(range = c(-205,205),zeroline = TRUE,zerolinewidth = 4, size = 20, title = 'C - Rpre', tickangle = 45), yaxis = list(showticklabels = FALSE, ticktext = list("-200", "-100", "0", "100", "200"), tickvals = list(-200, -100, 0, 100, 200),zeroline = TRUE, zerolinewidth = 4, tick0 = 0, dtick = 50, ticklen = 5, tickwidth = 2,title = 'Rpost - Rpre', zeroline = F, range = c(-205, 205))) %>%
  layout(showlegend = F)


trial1 <-subplot(t1g1,t1g2,t1g3,t1g4,t1g5)
trial2 <-subplot(t2g1,t2g2,t2g3,t2g4,t2g5)
trial3 <-subplot(t3g1,t3g2,t3g3,t3g4,t3g5)
