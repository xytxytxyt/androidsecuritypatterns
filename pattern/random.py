from utils import grid
from utils import naiveGeometry as ng
import logging

def getNextPoint(pathSoFar, pointsRemaining):
    currentPoint = pathSoFar[-1]
    while True:
        nextPoint = grid.getRandomPoint(pointsRemaining)
        pointsAfterNextPoint = set(pointsRemaining)
        pointsAfterNextPoint.remove(nextPoint)

        logging.debug('currentPoint: %s' % str(currentPoint))
        logging.debug('nextPoint: %s' % str(nextPoint))
        logging.debug('pointsAfterNextPoint: %s' % str(pointsAfterNextPoint))

        if all([not ng.pointIsBetweenOnLine(point, currentPoint, nextPoint) for point in pointsAfterNextPoint]):
            return nextPoint

def generateOne(source=None):
    if source is None:
        source = grid.getRandomPoint()
    pathSoFar = [source]
    pointsRemaining = grid.points()
    pointsRemaining.remove(source)

    logging.debug('pathSoFar: %s' % str(pathSoFar))
    logging.debug('pointsRemaining: %s' % str(pointsRemaining))

    while pointsRemaining:
        nextPoint = getNextPoint(pathSoFar, set(pointsRemaining))
        pathSoFar.append(nextPoint)
        pointsRemaining.remove(nextPoint)

        logging.debug('pathSoFar: %s' % str(pathSoFar))
        logging.debug('pointsRemaining: %s' % str(pointsRemaining))
    return pathSoFar
