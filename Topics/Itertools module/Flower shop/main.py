import itertools


for number in range(1, 4):
    for bouquet in itertools.combinations(flower_names, number):
        print(bouquet)
