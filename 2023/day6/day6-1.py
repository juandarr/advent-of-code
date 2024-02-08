from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    c = 0
    times = []
    distances = []
    for line in lines:
        if c == 0:
            times = line.strip().split(":")[1].strip().split()
            c += 1
        else:
            distances = line.strip().split(":")[1].strip().split()
    return times, distances


def waysToBeatRecord(times, distances):
    c = 0
    net = 1
    while c < len(times):
        time = int(times[c])
        distance = int(distances[c])
        ways = 0
        for t in range(1, time):
            if t * (time - t) > distance:
                ways += 1
        net *= ways
        c += 1
    return net


def main(filename):
    times, distances = parseInformation(filename)
    mul = waysToBeatRecord(times, distances)
    return mul


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 6, [288], main)
    else:
        ans = getAnswer(2023, 6, main)
        print("The product of ways to beat record is: {0}".format(ans))
