from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    return list(tmp[0])


rocks = [
    ["####"],
    [".#.", "###", ".#."],
    ["###", "..#", "..#"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]
rockProfileLimit = {
    ">": [[3], [1, 2, 1], [2, 2, 2], [0, 0, 0, 0], [1, 1]],
    "<": [[0], [1, 0, 1], [0, 2, 2], [0, 0, 0, 0], [0, 0]],
    "^": [[0, 0, 0, 0], [1, 0, 1], [0, 0, 0], [0], [0, 0]],
}


def moveAndFall(map, rockId, rockPosition, dir):
    locked = False
    rock = rocks[rockId]
    # simulate move of rock until no movement is allowed
    if dir == ">":
        canMove = True
        for idxRow, row in enumerate(rock):
            if rockPosition[1] + len(row) > 6:
                canMove = False
                break
            if (
                map[rockPosition[0] + idxRow][
                    rockPosition[1] + rockProfileLimit[">"][rockId][idxRow] + 1
                ]
                == "#"
            ):
                canMove = False
                break
        if canMove:
            rockPosition = [rockPosition[0], rockPosition[1] + 1]
    else:
        canMove = True
        for idxRow, row in enumerate(rock):
            if rockPosition[1] == 0:
                canMove = False
                break
            if (
                map[rockPosition[0] + idxRow][
                    rockPosition[1] + rockProfileLimit["<"][rockId][idxRow] - 1
                ]
                == "#"
            ):
                canMove = False
                break
        if canMove:
            rockPosition = [rockPosition[0], rockPosition[1] - 1]
    # simulate fall of rock until no movement is allowed
    canMove = True
    for idxCol, _ in enumerate(rock[0]):
        if rockPosition[0] == 0:
            canMove = False
            break
        if (
            map[rockPosition[0] + rockProfileLimit["^"][rockId][idxCol] - 1][
                rockPosition[1] + idxCol
            ]
            == "#"
        ):
            canMove = False
            break
    if canMove:
        rockPosition = [rockPosition[0] - 1, rockPosition[1]]
    else:
        locked = True
        for idxRow, row in enumerate(rock):
            for idxCol, col in enumerate(row):
                if col == "#":
                    map[rockPosition[0] + idxRow][rockPosition[1] + idxCol] = "#"
        while "".join(map[-1][:]) == ".......":
            map.pop()
    return map, rockPosition, locked


def simulateFall(dirs, r):
    map = [list("#" * 7)]
    idxRock = 0
    idxDir = 0
    rockId = idxRock % len(rocks)
    rockPosition = [len(map) + 3, 2]
    for _ in range(len(rocks[rockId]) + 3):
        map.append(list("." * 7))
    locked = False
    rockCounter = 1
    while True:
        dir = dirs[idxDir % len(dirs)]
        # When rock is locked move to the next rock and expand the map
        if locked:
            rockCounter += 1
            if rockCounter == r:
                break
            locked = False
            idxRock += 1
            rockId = idxRock % len(rocks)
            for _ in range(len(rocks[rockId]) + 3):
                map.append(list("." * 7))
            rockPosition = [len(map) - len(rocks[rockId]), 2]
        map, rockPosition, locked = moveAndFall(map, rockId, rockPosition, dir)
        idxDir += 1
    return len(map) - 1


def main(filename):
    dirs = parseInformation(filename)
    r = 2023
    height = simulateFall(dirs, r)
    return height


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(17, [3068], main)
    else:
        ans = getAnswer(17, main)
        print("The height of the tower of rocks is {0}".format(ans))
