import random
from statistics import mean


def sim():
    match = random.randint(0, 100)
    if match < 7:
        return 0
    elif 7 <= match < 18:
        return 1
    else:
        return 3


total_points = []
for i in range(1000000):  # number of season simulations
    season_scores = []
    for j in range(7):  # 7 matches on small fields
        season = sim()
        season_scores.append(season)
    total_points.append(sum(season_scores))
print(mean(total_points))
