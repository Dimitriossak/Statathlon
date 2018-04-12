#Research parts:
#Part I: compare the teams within the championships
#Part II: (a) compare the Championships means and (b) the teams within the sample
#Part III: find the picks in II.b and search for the MVP to indentify the most imporant position for each month

rm(list=ls())

#####Data Preparation ###################################

Leagues_list <- c("09.10", "10.11", "11.12", "12.13", "13.14", "14.15", "15.16", "16.17")
Premier_Champions <- c("Chelsea", "Man United", "Man City", "Man United", "Man City", "Chelsea", "Leicester", "Chelsea")
Serie_Champions <- c("Inter", "Milan", "Juventus", "Juventus", "Juventus", "Juventus", "Juventus", "Juventus")
Bundesliga_Champions <- c("Bayern Munich", "Dortmund", "Dortmund", "Bayern Munich", "Bayern Munich", "Bayern Munich", "Bayern Munich", "Bayern Munich")
Primera_Champions <- c("Barcelona", "Barcelona", "Real Madrid", "Barcelona", "Ath Madrid", "Barcelona", "Barcelona", "Real Madrid")

#Create the file for each season per league
league_function <- function(x, y, z) {
  #Home Stats
  x_Home <- subset(x, x['HomeTeam']==y)
  x_Home['shots_for'] <- x_Home['HS']
  x_Home['shots_against'] <- x_Home['AS']
  x_Home['goals_for'] <- x_Home['FTHG']
  x_Home['goals_against'] <- x_Home['FTAG']
  x_Home['Opponent'] <- x_Home['AwayTeam']
  #Away Stats
  x_Away <- subset(x, x['AwayTeam']==y)
  x_Away['shots_for'] <- x_Away['AS']
  x_Away['shots_against'] <- x_Away['HS']
  x_Away['goals_for'] <- x_Away['FTAG']
  x_Away['goals_against'] <- x_Away['FTHG']
  x_Away['Opponent'] <- x_Away['HomeTeam']
  #Full_season
  x <- rbind(x_Home, x_Away)
  x['Season'] <- z
  x['Champion'] <- y
  x <- x[,c("Season", "Date", "Opponent", "goals_for", "goals_against", "shots_for", "shots_against", 'Champion')]
  return(x)
}

#Combine all_seasons - Premier League
for (i in 1:8) {
  Premier_temp <- read.csv(paste0("C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//", "PL ", Leagues_list[i], ".csv"), header = T)
  if (i==1) {
    Premier_league <- league_function(Premier_temp,Premier_Champions[i], Leagues_list[i])
  }
  else {
    Premier_temp <- league_function(Premier_temp, Premier_Champions[i], Leagues_list[i])
    Premier_league <- rbind(Premier_league, Premier_temp)
  }
}

#Combine all_seasons - Serie A
for (i in 1:8) {
  Serie_temp <- read.csv(paste0("C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//", "SA ", Leagues_list[i], ".csv"), header = T)
  na.omit(Serie_temp)
  if (i==1) {
    Serie_A <- league_function(Serie_temp,Serie_Champions[i], Leagues_list[i])
  }
  else {
    Serie_temp <- league_function(Serie_temp, Serie_Champions[i], Leagues_list[i])
    Serie_A <- rbind(Serie_A, Serie_temp)
  }
}

#Combine all_seasons - Bundesliga
for (i in 1:8) {
  Bundesliga_temp <- read.csv(paste0("C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//", "BU ", Leagues_list[i], ".csv"), header = T)
  na.omit(Bundesliga_temp)
  if (i==1) {
    Bundesliga <- league_function(Bundesliga_temp,Bundesliga_Champions[i], Leagues_list[i])
  }
  else {
    Bundesliga_temp <- league_function(Bundesliga_temp, Bundesliga_Champions[i], Leagues_list[i])
    Bundesliga <- rbind(Bundesliga, Bundesliga_temp)
  }
}

#Combine all_seasons - Primera Division
for (i in 1:8) {
  Primera_temp <- read.csv(paste0("C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//", "PD ", Leagues_list[i], ".csv"), header = T)
  na.omit(Primera_temp)
  if (i==1) {
    Primera_Division <- league_function(Primera_temp,Primera_Champions[i], Leagues_list[i])
  }
  else {
    Primera_temp <- league_function(Primera_temp, Primera_Champions[i], Leagues_list[i])
    Primera_Division <- rbind(Primera_Division, Primera_temp)
  }
}

#Add the league column to each league
Premier_league$league <- "Premier League"
Primera_Division$league <- "Primera Division"
Serie_A$league <- "Serie A"
Bundesliga$league <- "Bundesliga"

#Combine all the Champions
four_leagues <- rbind(Premier_league, Primera_Division, Serie_A, Bundesliga)
#write.csv(four_leagues, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//four_leagues.csv", row.names = F)

#Calculate the ratio per League
four_leagues$ratio <- 0.6*four_leagues$goals_for+0.4*four_leagues$shots_for-0.6*four_leagues$goals_against-0.4*four_leagues$shots_against

#Add the month column to each league
four_leagues$month <- as.numeric(strftime(as.Date(four_leagues$Date), "%m"))

#Keep only the months with full activities (drop 8th and 6th)
four_leagues <- subset(four_leagues, four_leagues$month != 8 & four_leagues$month != 6)

Premier_league <- subset(four_leagues, four_leagues$league == "Premier League")
Primera_Division <- subset(four_leagues, four_leagues$league == "Primera Division")
Serie_A <- subset(four_leagues, four_leagues$league == "Serie A")
Bundesliga <- subset(four_leagues, four_leagues$league == "Bundesliga")

#Combine all the Champions
#four_leagues <- rbind(Premier_league, Primera_Division, Serie_A, Bundesliga)
#write.csv(four_leagues, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//four_leagues.csv", row.names = F)

########Part I: Find the best month for each champion per League######

#Create the pivot for Premier League
Premier_League_pivot <- as.data.frame(tapply(Premier_league$ratio, list(Premier_league$Champion, Premier_league$month), mean))

#Create the pivot for Primera Division
Primera_Division_pivot <- as.data.frame(tapply(Primera_Division$ratio, list(Primera_Division$Champion, Primera_Division$month), mean))

#Create the pivot for Serie A
Serie_A_pivot <- as.data.frame(tapply(Serie_A$ratio, list(Serie_A$Champion, Serie_A$month), mean))

#Create the pivot for Bundesliga
Bundesliga_pivot <- as.data.frame(tapply(Bundesliga$ratio, list(Bundesliga$Champion, Bundesliga$month), mean))

########Part II: Comparisons##################

#Part II.I: Total Comparison in sample (leagues)
#Create the comparison per league and combine it into one data.frame
championship_comparison <- as.data.frame(tapply(four_leagues$ratio, list(four_leagues$league, four_leagues$month), mean))

#write.csv(championship_comparison, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//championship_comparison.csv", row.names = T)

#Part II.II: Total Comparison in sample (clubs)
#Combine all pivots in one file
all_leagues_pivot <- rbind(Premier_League_pivot, Primera_Division_pivot, Serie_A_pivot, Bundesliga_pivot)

#write.csv(all_leagues_pivot, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//all_leagues_pivot.csv", row.names = T)

########Part III: Most valuable players for each month##################

Best_champions_per_month <- c("Barcelona", "Real Madrid", "Dortmund", "Inter", "Man City", "Bayern Munich", "Bayern Munich", "Dortmund", "Bayern Munich")

#Find the best period in 7 years per each club-winner
#Extract the best season in order to find online the MVP for the month
for (i in 1:9) {
  if (i==1) {
    months <- setNames(aggregate(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i)[, 'ratio'], list(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i)$Season), mean), c("Season", "mean_Ratio"))
    months <- months[which.max(months$mean_Ratio),]
  }
  else if (i<6) {
    months_temp<- setNames(aggregate(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i)[, 'ratio'], list(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i)$Season), mean), c("Season", "mean_Ratio"))
    months_temp <- months_temp[which.max(months_temp$mean_Ratio),]
    months <- rbind(months, months_temp)
  }
  else {
    months_temp<- setNames(aggregate(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i+3)[, 'ratio'], list(subset(four_leagues, four_leagues$Champion==Best_champions_per_month[i] & four_leagues$month==i+3)$Season), mean), c("Season", "mean_Ratio"))
    months_temp <- months_temp[which.max(months_temp$mean_Ratio),]
    months <- rbind(months, months_temp)
  }
}

for (i in 1:9) {
  months$champion[i] <- Best_champions_per_month[i]
  if (i<6) {
    months$month[i] <- i
  }
  else{
    months$month[i] <- i+3
  }
}


#### Export Results###########
#Part I: Combine all the Champions
#write.csv(four_leagues, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//four_leagues.csv", row.names = F)

#Part II: Comparisons
#Create the comparison per league
#write.csv(all_leagues_pivot, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//all_leagues_pivot.csv", row.names = T)
#Combine all Pivots
#write.csv(all_leagues_pivot, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//all_leagues_pivot.csv", row.names = T)

#Part III: The best team per month - MVP to be added
#write.csv(months, "C://Users//GR828ZN//Documents//Technical Improvement//All_leagues//best_clubs_per_month.csv", row.names = F)
