#2017/2018 Season Simulation for the club: Napoli FC
import random
from statistics import mean

#formation
def sim_formation():
    formation = random.randint(0, 100)
    if formation <= 8:
        return "3-4-3"
    elif 8 < formation < 32:
        return "4-4-2"
    elif 32 < formation < 61:
        return "4-5-1"
    elif 61 < formation < 85:
        return "4-3-3"
    elif 85 < formation < 92:
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
        if goals_for <14:
            goals_for = 0
        elif 14 < goals_for < 36:
            goals_for = 1
        elif 36 < goals_for < 58:
            goals_for = 2
        elif 58 < goals_for < 83:
            goals_for = 3
        elif 83 < goals_for < 92:
            goals_for = 4
        elif 92 < goals_for < 97:
            goals_for = 5
        else:
            goals_for = 6
    elif formation == "4-3-3":
        if goals_for < 9:
            goals_for = 0
        elif 9 < goals_for < 36:
            goals_for = 1
        elif 36 < goals_for < 74:
            goals_for = 2
        elif 74 < goals_for < 83:
            goals_for = 3
        elif 83 < goals_for < 94:
            goals_for = 4
        else:
            goals_for = 5
    elif formation == "3-5-2":
        if goals_for < 11:
            goals_for = 0
        elif 11 < goals_for < 44:
            goals_for = 1
        elif 44 < goals_for < 61:
            goals_for = 2
        elif 61 < goals_for < 83:
            goals_for = 3
        elif 83 < goals_for < 94:
            goals_for = 4
        else:
            goals_for = 5
    elif formation == "3-4-3":
        if goals_for < 30:
            goals_for = 0
        elif 30 < goals_for < 55:
            goals_for = 1
        elif 55 < goals_for < 70:
            goals_for = 2
        elif 70 < goals_for < 90:
            goals_for = 3
        elif 90 < goals_for < 95:
            goals_for = 5
        else:
            goals_for = 6
    elif formation == "4-5-1":
        if goals_for < 19:
            goals_for = 0
        elif 19 < goals_for < 47:
            goals_for = 1
        elif 47 < goals_for < 80:
            goals_for = 2
        elif 80 < goals_for < 95:
            goals_for = 3
        elif 95 < goals_for < 99:
            goals_for = 4
        else:
            goals_for = 7
    else:
        if goals_for < 14:
            goals_for = 0
        elif 14 < goals_for < 38:
            goals_for = 1
        elif 38 < goals_for < 62:
            goals_for = 2
        elif 62 < goals_for < 76:
            goals_for = 3
        elif 76 < goals_for < 90:
            goals_for = 4
        elif 76 < goals_for < 95:
            goals_for = 5
        else:
            goals_for = 6
            
    #goals against
    if formation == "4-4-2":
        if goals_against < 42:
            goals_against = 0
        elif 42 < goals_against < 73:
            goals_against = 1
        elif 73 < goals_against < 92:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "3-4-3":
        if goals_against < 25:
            goals_against = 0
        elif 25 < goals_against < 40:
            goals_against = 1
        elif 40 < goals_against < 65:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "3-5-2":
        if goals_against < 22:
            goals_against = 0
        elif 22 < goals_against < 61:
            goals_against = 1
        elif 61 < goals_against < 83:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "4-5-1":
        if goals_against < 30:
            goals_against = 0
        elif 30 < goals_against < 73:
            goals_against = 1
        elif 73 < goals_against < 91:
            goals_against = 2
        else:
            goals_against = 3
    elif formation == "5-4-1":
        if goals_against < 48:
            goals_against = 0
        elif 48 < goals_against < 76:
            goals_against = 1
        elif 76 < goals_against < 90:
            goals_against = 2
        else:
            goals_against = 3
    else:
        if goals_against < 36:
            goals_against = 0
        elif 36 < goals_against < 70:
            goals_against = 1
        elif 70 < goals_against < 92:
            goals_against = 2
        elif 92 < goals_against < 97:
            goals_against = 3
        else:
            goals_against = 4
            
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

