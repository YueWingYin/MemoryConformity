library(reshape)
library(ggcorrplot)
library(corrplot)

data <- Memory_conformity_Raw_data_

data <- data[order(data$Participant, data$Order),]

#trial 1
data$C1R0 = data$C1 - data$R0 #confederate-vs-self confidence difference
data$R1R0 = data$R1 - data$R0 #participant's change of confidence

#arranging data
data_corr <- setNames(data.frame(matrix(ncol = 181, nrow = 38)), c("Participant",c(paste0("C1R0_", 1:90)),c(paste0("R1R0_", 1:90))))

for (i in 1:38) {
  data_corr[i,1] <- i  
  for (j in 1:90){
    r <- (i-1)*90+j
    data_corr[i,j+1] <- data[r,14]
    data_corr[i,j+91] <- data[r,15]
  }
}

corr_mat <- cor(data_corr[2:91],data_corr[92:181])
p.mat <- cor_pmat(corr_mat)

#plot
col1 <- colorRampPalette(c("#7F0000", "red", "#FF7F00", "yellow", "white",
                           "cyan", "#007FFF", "blue", "#00007F"))
col2 <- colorRampPalette(c("#67001F", "#B2182B", "#D6604D", "#F4A582",
                           "#FFFFFF", "#92C5DE",
                           "#4393C3", "#2166AC", "#053061"))
corrplot(corr_mat, method = "color",col = col2(100))
#, p.mat=p.mat

#trial 2
data$C2R1 = data$C2 - data$R1
data$R2R1 = data$R2 - data$R1

data_corr2 <- setNames(data.frame(matrix(ncol = 181, nrow = 38)), c("Participant",c(paste0("C2R1_", 1:90)),c(paste0("R2R1_", 1:90))))

for (i in 1:38) {
  data_corr2[i,1] <- i  
  for (j in 1:90){
    r <- (i-1)*90+j
    data_corr2[i,j+1] <- data[r,16]
    data_corr2[i,j+91] <- data[r,17]
  }
}

corr_mat2 <- cor(data_corr2[2:91],data_corr2[92:181])
p.mat2 <- cor_pmat(corr_mat2)

col1 <- colorRampPalette(c("#7F0000", "red", "#FF7F00", "yellow", "white",
                           "cyan", "#007FFF", "blue", "#00007F"))
col2 <- colorRampPalette(c("#67001F", "#B2182B", "#D6604D", "#F4A582",
                           "#FFFFFF", "#92C5DE",
                           "#4393C3", "#2166AC", "#053061"))
corrplot(corr_mat2, method = "color",col = col2(100))
#, p.mat=p.mat2

#trial 3
data$C3R2 = data$C3 - data$R2
data$R3R2 = data$R3 - data$R2

data_corr3 <- setNames(data.frame(matrix(ncol = 181, nrow = 38)), c("Participant",c(paste0("C3R2_", 1:90)),c(paste0("R3R2_", 1:90))))

for (i in 1:38) {
  data_corr3[i,1] <- i  
  for (j in 1:90){
    r <- (i-1)*90+j
    data_corr3[i,j+1] <- data[r,18]
    data_corr3[i,j+91] <- data[r,19]
  }
}

corr_mat3 <- cor(data_corr3[2:91],data_corr3[92:181])
p.mat3 <- cor_pmat(corr_mat3)

col1 <- colorRampPalette(c("#7F0000", "red", "#FF7F00", "yellow", "white",
                           "cyan", "#007FFF", "blue", "#00007F"))
col2 <- colorRampPalette(c("#67001F", "#B2182B", "#D6604D", "#F4A582",
                           "#FFFFFF", "#92C5DE",
                           "#4393C3", "#2166AC", "#053061"))
corrplot(corr_mat3, method = "color",col = col2(100))
