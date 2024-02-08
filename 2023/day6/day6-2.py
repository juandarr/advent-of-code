from math import sqrt, ceil, floor
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    c = 0
    time = []
    distance = []
    for line in lines:
        if c == 0:
            time = line.strip().split(":")[1].strip().split()
            c += 1
        else:
            distance = line.strip().split(":")[1].strip().split()
    return time, distance


def waysToBeatRecord(times, distances):
    times = ["".join(times)]
    distances = ["".join(distances)]
    print(times, distances)
    c = 0
    net = 1
    while c < len(times):
        time = int(times[c])
        distance = int(distances[c])
        ways = 0
        x2 = (time + sqrt(time**2 - 4 * distance)) / 2.0
        x1 = (time - sqrt(time**2 - 4 * distance)) / 2.0
        # If solution is integer increase the value
        if x1 == int(x1):
            x1 = int(x1) + 1
        # Else take the ceil of the float
        else:
            x1 = ceil(x1)
        # If solution is integer increase the value
        if x2 == int(x2):
            x2 = int(x2) - 1
        # Else take the ceil of the float
        else:
            x2 = floor(x2)
        net *= x2 - x1 + 1
        c += 1
    return net


def main(filename):
    times, distances = parseInformation(filename)
    ways = waysToBeatRecord(times, distances)
    return ways


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 6, [71503], main)
    else:
        ans = getAnswer(2023, 6, main)
        print("The number of ways to beat record is: {0}".format(ans))
