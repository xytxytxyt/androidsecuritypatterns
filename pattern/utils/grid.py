import random

random.seed()


thePoints = set([
    (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (1, 3),
    (2, 3),
    (3, 3),
])


def points():
    return set(thePoints)


def getRandomPoint(pointsPopulation=None):
    if pointsPopulation is None:
        pointsPopulation = thePoints
    return random.sample(pointsPopulation, 1)[0]
