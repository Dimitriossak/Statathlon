#Code created by Dimitrios Sakellaris for Statathlon | All rights reserved.
import random
from statistics import mean


def sim_large():
    match = random.randint(0, 100)
    if match <= 18:
        return 0
    elif 18 < match < 64:
        return 1
    else:
        return 3


def sim_small():
    match = random.randint(0, 100)
    if match < 7:
        return 0
    elif 7 <= match < 18:
        return 1
    else:
        return 3


total_points_large = []
for i in range(1000000):  # Number of seasons simulated
    season_scores = []
    for j in range(31):  # Number of matches simulated per season
        season = sim_large()
        season_scores.append(season)
    total_points_large.append(sum(season_scores))
print(mean(total_points_large), "in large fields")

total_points_small = []
for i in range(1000000):  # Number of seasons simulated
    season_scores = []
    for j in range(7):  # Number of matches simulated per season
        season = sim_small()
        season_scores.append(season)
    total_points_small.append(sum(season_scores))
print(mean(total_points_small), "in small fields")

print (mean(total_points_large) + mean(total_points_small), "in total")
