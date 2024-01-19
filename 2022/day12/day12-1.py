from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    map = []
    for row in tmp:
        map.append(list(row))
    return map


def minimalRoute(map):
    elevationKey = {}
    for i in range(97, 97 + 26):
        elevationKey[chr(i)] = i - 97
    map2d = []
    start = (-1, -1)
    end = (-1, -1)
    for i, row in enumerate(map):
        if start == (-1, -1) or end == (-1, -1):
            for j, elem in enumerate(row):
                if elem == "S":
                    row[j] = "Sa"
                    start = (i, j)
                elif elem == "E":
                    row[j] = "Ez"
                    end = (i, j)
        map2d.append(row)

    ## Create steps maps
    stepsMap = []
    for i in range(len(map2d)):
        stepsMap.append([float("inf")] * len(map2d[i]))
    ## Let's start from the end
    # Up, down, right, left
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    toExpand = [end]
    stepsMap[end[0]][end[1]] = 0
    while toExpand != []:
        newToExpand = []
        for node in toExpand:
            steps = stepsMap[node[0]][node[1]]
            height = elevationKey[map2d[node[0]][node[1]][-1]]
            for direction in directions:
                newNode = (node[0] + direction[0], node[1] + direction[1])
                if (
                    newNode[0] < 0
                    or newNode[0] == len(stepsMap)
                    or newNode[1] < 0
                    or newNode[1] == len(stepsMap[0])
                ):
                    continue
                newHeight = elevationKey[map2d[newNode[0]][newNode[1]][-1]]
                if (
                    height - 1 <= newHeight
                    and (steps + 1) < stepsMap[newNode[0]][newNode[1]]
                ):
                    stepsMap[newNode[0]][newNode[1]] = steps + 1
                    newToExpand.append(newNode)
        toExpand = []
        toExpand.extend(newToExpand)

    return stepsMap[start[0]][start[1]]


def main(filename):
    map = parseInformation(filename)
    steps = minimalRoute(map)
    return steps


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(12, [31], main)
    else:
        ans = getAnswer(12, main)
        print("The minimal route value is {0}".format(ans))
