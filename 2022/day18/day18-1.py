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


def surfaceArea(positions):
    surfacePerCube = {}
    dimensions = [0, 1, 2]
    increments = [-1, 1]
    for position in positions:
        surfacePerCube[tuple(position)] = 6
    for position in positions:
        for dimension in dimensions:
            for increment in increments:
                tmp = position.copy()
                tmp[dimension] += increment
                tmp = tuple(tmp)
                if tmp in surfacePerCube:
                    surfacePerCube[tuple(position)] -= 1
    area = 0
    for i in surfacePerCube:
        area += surfacePerCube[i]
    return area


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
        performTests(18, [64], main)
    else:
        ans = getAnswer(18, main)
        print("The total surface area is {0}".format(ans))
