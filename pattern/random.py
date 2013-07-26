from utils import grid
from utils import naiveGeometry as ng

def getNextPoint(pathSoFar, pointsRemaining):
    currentPoint = pathSoFar[-1]
    while True:
        nextPoint = grid.getRandomPoint(pointsRemaining)
        pointsAfterNextPoint = set(pointsRemaining)
        pointsAfterNextPoint.remove(nextPoint)
        print 'currentPoint', currentPoint
        print 'nextPoint', nextPoint
        print 'pointsAfterNextPoint', pointsAfterNextPoint
        if all([not ng.pointIsBetweenOnLine(point, currentPoint, nextPoint) for point in pointsAfterNextPoint]):
            return nextPoint

def generateOne(source=None):
    if source is None:
        source = grid.getRandomPoint()
    pathSoFar = [source]
    pointsRemaining = grid.points()
    pointsRemaining.remove(source)
    print 'pathSoFar', pathSoFar
    print 'pointsRemaining', pointsRemaining
    while pointsRemaining:
        nextPoint = getNextPoint(pathSoFar, set(pointsRemaining))
        pathSoFar.append(nextPoint)
        pointsRemaining.remove(nextPoint)
        print 'pathSoFar', pathSoFar
        print 'pointsRemaining', pointsRemaining
    return pathSoFar
