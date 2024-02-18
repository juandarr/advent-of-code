from copy import deepcopy
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    bricks = {}
    c = 1
    for line in lines:
        points = line.strip().split("~")
        p = []
        for point in points:
            x, y, z = point.split(",")
            p.append([int(x), int(y), int(z)])
        bricks[c] = [[p[0][0], p[1][0]], [p[0][1], p[1][1]], [p[0][2], p[1][2]]]
        c += 1
    return bricks


def printLevel(lev, bricks, maxLevel):
    labels = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
    }
    c = 0
    mx = []
    my = []
    while c <= maxLevel:
        mx.append(list("." * 20))
        my.append(list("." * 20))
        if c in lev:
            for i in lev[c]:
                for x in range(bricks[i][0][0], bricks[i][0][1] + 1):
                    if mx[-1][x] != ".":
                        mx[-1][x] = "?"
                    else:
                        mx[-1][x] = labels[i]
                for y in range(bricks[i][1][0], bricks[i][1][1] + 1):
                    if my[-1][y] != ".":
                        my[-1][y] = "?"
                    else:
                        my[-1][y] = labels[i]
        c += 1
    print("\nx vs z : \n")
    for i in reversed(mx):
        print("".join(i))
    print("\ny vs z : \n")
    for i in reversed(my):
        print("".join(i))


def fallSimulation(bricks, lev, maxLev):
    movingDown = True
    down = set()
    while movingDown:
        movingDown = False
        curLevel = 2
        while curLevel <= maxLev:
            belowLevel = curLevel - 1
            goingDown = []
            if curLevel in lev:
                for b in lev[curLevel]:
                    brick = bricks[b]
                    goesBelow = True
                    if belowLevel in lev:
                        for bBelow in lev[belowLevel]:
                            brickBelow = bricks[bBelow]
                            blocked = [False, False]
                            for idx in range(2):
                                m = list(
                                    range(
                                        max(brick[idx][0], brickBelow[idx][0]),
                                        min(brick[idx][1], brickBelow[idx][1]) + 1,
                                    )
                                )
                                if m != []:
                                    blocked[idx] = True
                                if blocked[0] is True and blocked[1] is True:
                                    goesBelow = False
                                    break
                            if not (goesBelow):
                                break
                    if goesBelow:
                        movingDown = True
                        i = curLevel
                        while i <= maxLev:
                            if i in lev:
                                if b in lev[i]:
                                    goingDown.append((b, i))
                            else:
                                break
                            i += 1
            if len(goingDown) > 0:
                for val in goingDown:
                    down.add(val[0])
                    b = val[0]
                    level = val[1]
                    lowLevel = level - 1
                    del lev[level][b]
                    if lev[level] == {}:
                        del lev[level]
                    if lowLevel in lev:
                        lev[lowLevel][b] = True
                    else:
                        lev[lowLevel] = {b: True}
            curLevel += 1
    return len(down)


def exploreFall(bricks, test):
    lev = {}
    minLev = float("inf")
    maxLev = -float("inf")
    for label in bricks:
        brick = bricks[label]
        levels = list(range(brick[2][0], brick[2][1] + 1))
        minLev = min(minLev, brick[2][0])
        maxLev = max(maxLev, brick[2][1])
        for level in levels:
            if level in lev:
                lev[level][label] = True
            else:
                lev[level] = {label: True}
    # if test:
    #     print("Initial state: ", lev)
    #     printLevel(lev, bricks, maxLev)
    fallSimulation(bricks, lev, maxLev)
    # if test:
    #     print("End state: ", lev)
    #     printLevel(lev, bricks, maxLev)
    c = 1
    simulate = []
    while c + 1 in lev:
        for b in lev[c]:
            toTest = lev[c].copy()
            del toTest[b]
            goesBelow = False
            for bAbove in lev[c + 1]:
                if b == bAbove:
                    continue
                brick = bricks[bAbove]
                goesBelow = True
                for bBelow in toTest:
                    brickBelow = bricks[bBelow]
                    blocked = [False, False]
                    for idx in range(2):
                        m = list(
                            range(
                                max(brick[idx][0], brickBelow[idx][0]),
                                min(brick[idx][1], brickBelow[idx][1]) + 1,
                            )
                        )
                        if m != []:
                            blocked[idx] = True
                    if blocked[0] is True and blocked[1] is True:
                        goesBelow = False
                        break
                else:
                    break
            if goesBelow:
                simulate.append((b, c))
        c += 1
    net = 0
    for s in simulate:
        levToSimulate = deepcopy(lev)
        b = s[0]
        c = s[1]
        while b in levToSimulate[c]:
            del levToSimulate[c][b]
            if levToSimulate[c] == {}:
                del levToSimulate[c]
            c += 1
        net += fallSimulation(bricks, levToSimulate, maxLev)
    return net


def main(filename):
    bricks = parseInformation(filename)
    p = exploreFall(bricks, test)
    return p


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 22, [7], main, test=["1"])
    else:
        ans = getAnswer(2023, 22, main)
        print(
            "The sum of the number of other bricks that would fall is: {0}".format(ans)
        )
