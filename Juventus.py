#2017/2018 Season Simulation for the club: Juventus FC
import random
from statistics import mean

#formation
def sim_formation():
    formation = random.randint(0, 100)
    if formation <= 5:
        return "3-4-3"
    elif 5 < formation < 30:
        return "4-4-2"
    elif 30 < formation < 59:
        return "4-5-1"
    elif 59 < formation < 85:
        return "4-3-3"
    elif 85 < formation < 89:
        return "3-5-2"
    else:
        return "5-4-1"

#match function
def match():
    goals_for = random.randint(0, 100)
    goals_against = random.randint(0, 100)
    formation = sim_formation()
    #goals for
    if formation == "4-4-2":
        if goals_for <7:
            goals_for = 0
        elif 7 < goals_for < 37:
            goals_for = 1
        elif 37 < goals_for < 65:
            goals_for = 2
        elif 65 < goals_for < 84:
            goals_for = 3
        elif 84 < goals_for < 96:
            goals_for = 4
        else:
            goals_for = 5
    elif formation == "4-3-3":
        if goals_for < 6:
            goals_for = 0
        elif 6 < goals_for < 43:
            goals_for = 1
        elif 43 < goals_for < 71:
            goals_for = 2
        elif 71 < goals_for < 90:
            goals_for = 3
        elif 90 < goals_for < 99:
            goals_for = 4
        else:
            goals_for = 6
    elif formation == "3-5-2":
        if goals_for < 25:
            goals_for = 1
        elif 25 < goals_for < 50:
            goals_for = 2
        elif 50 < goals_for < 92:
            goals_for = 3
        else:
            goals_for = 4
    elif formation == "3-4-3":
        if goals_for < 8:
            goals_for = 0
        elif 8 < goals_for < 23:
            goals_for = 1
        elif 23< goals_for < 77:
            goals_for = 2
        elif 77 < goals_for < 92:
            goals_for = 3
        else:
            goals_for = 4
    elif formation == "4-5-1":
        if goals_for < 25:
            goals_for = 0
        elif 25 < goals_for < 59:
            goals_for = 1
        elif 59 < goals_for < 88:
            goals_for = 2
        elif 88 < goals_for < 94:
            goals_for = 3
        elif 94 < goals_for < 99:
            goals_for = 4
        else:
            goals_for = 7
    else:
        if goals_for < 21:
            goals_for = 1
        elif 21 < goals_for < 62:
            goals_for = 2
        elif 62 < goals_for < 86:
            goals_for = 3
        else:
            goals_for = 4
            
    #goals against
    if formation == "4-4-2":
        if goals_against < 49:
            goals_against = 0
        elif 49 < goals_against < 83:
            goals_against = 1
        elif 83 < goals_against < 96:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "3-4-3":
        if goals_against < 31:
            goals_against = 0
        elif 31 < goals_against < 69:
            goals_against = 1
        elif 69 < goals_against < 84:
            goals_against = 2
        elif 84 < goals_against < 92:
            goals_against = 3
        else:
            goals_against = 4
    elif formation == "3-5-2":
        if goals_against < 50:
            goals_against = 0
        elif 50 < goals_against < 58:
            goals_against = 1
        elif 58 < goals_against < 91:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "4-5-1":
        if goals_against < 57:
            goals_against = 0
        elif 57 < goals_against < 95:
            goals_against = 1
        else:
            goals_against = 2
    elif formation == "5-4-1":
        if goals_against < 34:
            goals_against = 0
        elif 34 < goals_against < 75:
            goals_against = 1
        elif 75 < goals_against < 89:
            goals_against = 2
        elif 89 < goals_against < 96:
            goals_against = 3
        else:
            goals_against = 4
    else:
        if goals_against < 50:
            goals_against = 0
        elif 50 < goals_against < 90:
            goals_against = 1
        elif 90 < goals_against < 97:
            goals_against = 2
        else:
            goals_against = 3
            
    #match result
    if goals_for > goals_against:
        return 3
    elif goals_for == goals_against:
        return 1
    else:
        return 0

#print(match())

total_points = []
for i in range(1000000):  # Number of season's simulations
    season_scores = []
    for j in range(38):  # Number of matches simulated per season
        season = match()
        season_scores.append(season)
    total_points.append(sum(season_scores))
    
print(mean(total_points), "approximate points in 2017/18 season")

