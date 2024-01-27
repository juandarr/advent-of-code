from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    positions = []
    for position in tmp:
        positions.append([int(i) for i in position.strip().split(",")])
    return positions


def readLocations(positions):
    mins = [1000, 1000, 1000]
    maxs = [-1000, -1000, -1000]
    for position in positions:
        for idx, i in enumerate(position):
            if mins[idx] > i:
                mins[idx] = i
            if maxs[idx] < i:
                maxs[idx] = i
    minMax = {}
    for x in range(mins[0], maxs[0] + 1):
        for y in range(mins[1], maxs[1] + 1):
            for z in range(mins[2], maxs[2] + 1):
                minMax[(x, y, "")] = [1000, -1000]
                minMax[(x, "", z)] = [1000, -1000]
                minMax[("", y, z)] = [1000, -1000]
    for p in positions:
        if minMax[(p[0], p[1], "")][0] > p[2]:
            minMax[(p[0], p[1], "")][0] = p[2]
        if minMax[(p[0], p[1], "")][1] < p[2]:
            minMax[(p[0], p[1], "")][1] = p[2]
        if minMax[(p[0], "", p[2])][0] > p[1]:
            minMax[(p[0], "", p[2])][0] = p[1]
        if minMax[(p[0], "", p[2])][1] < p[1]:
            minMax[(p[0], "", p[2])][1] = p[1]
        if minMax[("", p[1], p[2])][0] > p[0]:
            minMax[("", p[1], p[2])][0] = p[0]
        if minMax[("", p[1], p[2])][1] < p[0]:
            minMax[("", p[1], p[2])][1] = p[0]
    return positions, minMax


def surfaceArea(positions):
    positions, minMax = readLocations(positions)
    surfacePerCube = {}
    dimensions = [0, 1, 2]
    increments = [-1, 1]
    area = 0
    for position in positions:
        surfacePerCube[tuple(position)] = 6
    airPockets = {}
    for position in positions:
        for dimension in dimensions:
            for increment in increments:
                tmp = position.copy()
                tmp[dimension] += increment
                tmp = tuple(tmp)
                if tmp in surfacePerCube:
                    surfacePerCube[tuple(position)] -= 1
                else:
                    airPockets[tmp] = {"blockedSides": 0, "connectedTo": {}}
                    for dimension2 in dimensions:
                        for increment2 in increments:
                            tmp2 = list(tmp)
                            tmp2[dimension2] += increment2
                            tmp2 = tuple(tmp2)
                            if tmp2 in surfacePerCube:
                                airPockets[tmp]["blockedSides"] += 1
                            else:
                                airPockets[tmp]["connectedTo"][tmp2] = 1
    visited = {}
    for airPocket in airPockets:
        if airPockets[airPocket]["blockedSides"] == 6:
            visited[airPocket] = 1
            area -= 6
        # For each airpocket we need to traverse all possible connections looking for
        # an exit. If not exit is found, the surface area of all the airpockets connected are sumed and subtracted
        # from the surface area
    internalSurface = findAirPockets(airPockets, minMax, visited)
    for i in surfacePerCube:
        area += surfacePerCube[i]
    return area - internalSurface


def findAirPockets(airPockets, minMax, visited):
    internalSurface = 0
    for airPocket in airPockets:
        if airPocket not in visited:
            isAirPocket = True
            locallyVisited = {}
            toExpand = [airPocket]
            while toExpand != []:
                currentNode = toExpand[-1]
                if currentNode not in airPockets:
                    x, y, z = currentNode
                    # If currentNode is not between the internal limits of the structure,
                    # It is not an air pocket (since it is located outside the limits)
                    if (
                        (x, y, "") not in minMax
                        or (x, "", z) not in minMax
                        or ("", y, z) not in minMax
                    ) or (
                        minMax[(x, y, "")][0] > z
                        or minMax[(x, y, "")][1] < z
                        or minMax[(x, "", z)][0] > y
                        or minMax[(x, "", z)][1] < y
                        or minMax[("", y, z)][0] > x
                        or minMax[("", y, z)][1] < x
                    ):
                        isAirPocket = False
                        break
                    # Otherwise it is inside the 3d structure, continue expansion
                    locallyVisited[currentNode] = 1
                    toExpand.pop()
                    continue
                for i in airPockets[currentNode]["connectedTo"]:
                    if i not in locallyVisited:
                        toExpand.insert(0, i)
                locallyVisited[currentNode] = 1
                toExpand.pop()
            if isAirPocket:
                for v in locallyVisited:
                    if v in airPockets:
                        internalSurface += airPockets[v]["blockedSides"]
                    visited[v] = 1
    return internalSurface


def main(filename):
    positions = parseInformation(filename)
    area = surfaceArea(positions)
    return area


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(18, [58], main)
    else:
        ans = getAnswer(18, main)
        print("The exterior surface area is {0}".format(ans))
