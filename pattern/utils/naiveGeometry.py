def getSlope(a, b):
    dy = b[1] - a[1]
    dx = b[0] - a[0]
    if dx == 0:
        return float('inf')
    else:
        return float(dy / dx)


def pointIsBetweenOnLine(point, linePointA, linePointB):
    lineSlope = getSlope(linePointA, linePointB)
    testSlope = getSlope(linePointA, point)
    differencesx = [point[0] - linePointA[0], linePointB[0] - point[0]]
    differencesy = [point[1] - linePointA[1], linePointB[1] - point[1]]
    return all([
        lineSlope == testSlope,
        (all(d >= 0 for d in differencesx) or all(d < 0 for d in differencesx)),
        (all(d >= 0 for d in differencesy) or all(d < 0 for d in differencesy))
    ])
