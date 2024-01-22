from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    rockLines = []
    for row in tmp:
        rockLines.append(row)
    return rockLines


def mapFromRockStructure(rockLines):
    sandSource = (500, 0)
    map = ["+"]
    routes = []
    x = [float("inf"), -float("inf")]
    y = [0, -float("inf")]
    for path in rockLines:
        path = path.strip().split(" -> ")
        for idx, p in enumerate(path):
            p = p.split(",")
            xt = int(p[0])
            yt = int(p[1])
            x[0] = min(xt, x[0])
            x[1] = max(xt, x[1])
            y[1] = max(yt, y[1])
            path[idx] = [xt, yt]
        routes.append(path)
    map = []
    for _ in range(y[1] - y[0] + 1):
        row = "." * (int(x[1]) - int(x[0]) + 1)
        map.append(list(row))
    xOffset = int(x[0])
    yOffset = int(y[0])
    map[sandSource[1] - yOffset][sandSource[0] - xOffset] = "+"
    for route in routes:
        tmp = []
        for node in route:
            if tmp == []:
                tmp = node
                continue
            if tmp[0] == node[0]:
                mini = min(tmp[1], node[1])
                maxi = max(tmp[1], node[1])
                for i in range(mini, maxi + 1):
                    map[i - yOffset][tmp[0] - xOffset] = "#"
            elif tmp[1] == node[1]:
                mini = min(tmp[0], node[0])
                maxi = max(tmp[0], node[0])
                for j in range(mini, maxi + 1):
                    map[tmp[1] - yOffset][j - xOffset] = "#"
            tmp = node
    limits = [x, y]
    return [map, limits]


def sandSimulation(rockLines):
    map, limits = mapFromRockStructure(rockLines)
    sandSource = (500, 0)
    sandSourceLocal = (sandSource[1] - limits[1][0], sandSource[0] - limits[0][0])
    blocks = ["*", "#"]
    sandUnit = 1
    while True:
        coords = list(sandSourceLocal)
        abyss = False
        while (
            (map[coords[0] + 1][coords[1]] not in blocks)
            or (map[coords[0] + 1][coords[1] - 1] not in blocks)
            or (map[coords[0] + 1][coords[1] + 1] not in blocks)
        ):
            if map[coords[0] + 1][coords[1]] == ".":
                map[coords[0]][coords[1]] = "."
                coords[0] += 1
                map[coords[0]][coords[1]] = "*"
            elif map[coords[0] + 1][coords[1] - 1] == ".":
                map[coords[0]][coords[1]] = "."
                coords[0] += 1
                coords[1] -= 1
                map[coords[0]][coords[1]] = "*"
            elif map[coords[0] + 1][coords[1] + 1] == ".":
                map[coords[0]][coords[1]] = "."
                coords[0] += 1
                coords[1] += 1
                map[coords[0]][coords[1]] = "*"
            if (
                coords[0] + 1 >= len(map)
                or coords[1] + 1 >= len(map[0])
                or coords[1] - 1 < 0
            ):
                abyss = True
                break
        if abyss:
            break
        sandUnit += 1
    return sandUnit - 1


def main(filename):
    rockLines = parseInformation(filename)
    unitsBeforeAbyss = sandSimulation(rockLines)
    return unitsBeforeAbyss


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(14, [24], main)
    else:
        ans = getAnswer(14, main)
        print(
            "The number of units of sand comming to rest before overflow is {0}".format(
                ans
            )
        )
