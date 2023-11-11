import random
import math
import timeit

#Defining 2 points x and y
class pointsXY:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distanceXY(a, b):
    '''
    This function provides the distance between 2 points from the given input.
    
    Args:
        a,b : 2 points a and b.

    Returns:
        Distance between those points.

    '''
    X = a.x - b.x
    Y = a.y - b.y
    return math.sqrt(X * X + Y * Y)


def shortestXY(p, dl, dr):
    '''
    This function determines the closest set points and the distance between them from the given input array.
    
    Args:
        p, dl, dr : Point p, Left region, Right region.

    Returns:
        minDistance : Minimum Distance between those points.

    '''
    minDistance = float("inf")
    for g in range(dl, dr):
        for h in range(g + 1, dr):
            distance = distanceXY(p[g], p[h])
            if distance < minDistance:
                minDistance = distance
    return minDistance


def closestXY(p, dl, dr):
    '''
    closestXY : Function to find the closest pair of points in the delta region
    Args :
        p, dl, dr : Point p, Left region, Right region.
        
    Returns:
        minDistance : Minimum Distance between those points.
    '''
    if dr - dl <= 3:
        return shortestXY(p, dl, dr)
    mid = (dl + dr) // 2
    mid_point = p[mid]
    deltaL = closestXY(p, dl, mid)
    deltaR = closestXY(p, mid, dr)
    minDistance = min(deltaL, deltaR)
    deltaLR = []
    for g in range(dl, dr + 1):
        if abs(p[g].x - mid_point.x) < minDistance:
            deltaLR.append(p[g])
    deltaLR.sort(key=lambda p1: p1.y)
    for g in range(len(deltaLR)):
        for h in range(g + 1, len(deltaLR)):
            if deltaLR[h].y - deltaLR[g].y < minDistance:
                dist = distanceXY(deltaLR[g], deltaLR[h])
                if dist < minDistance:
                    minDistance = dist
    return minDistance


def closestPair(points):
    '''
    Function to find the closest pair of points
    '''
    p.sort(key=lambda point: point.x)
    return closestXY(p, 0, len(p) - 1)


if __name__ == "__main__":
    n = 50
    p = [pointsXY(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]
    begin = timeit.default_timer()
    shortestDistance = closestPair(p)
    end = timeit.default_timer()
    print(end-begin)
    print(f"The distance between the closest pair of points is: {shortestDistance}")