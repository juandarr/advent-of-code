from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and extract every position and velocity for each hailstone
    hailstones = []
    for line in lines:
        tmp = line.strip().split("@")
        tmp = {
            "pos": [int(i) for i in tmp[0].strip().split(",")],
            "vel": [int(i) for i in tmp[1].strip().split(",")],
        }
        hailstones.append(tmp)
    return hailstones


def findEstimate(hailstones, limits):
    i = 0
    c = 0
    while i < len(hailstones) - 1:
        p1 = hailstones[i]
        j = i + 1
        while j < len(hailstones):
            p2 = hailstones[j]
            m = -1 * p2["vel"][1] / p2["vel"][0]
            num = m * (p2["pos"][0] - p1["pos"][0]) + p2["pos"][1] - p1["pos"][1]
            den = p1["vel"][1] + m * p1["vel"][0]
            if den != 0:
                t1 = num / den
                num = p1["vel"][1] * t1 - p2["pos"][1] + p1["pos"][1]
                den = p2["vel"][1]
                if den != 0:
                    t2 = num / den
                    if t1 > 0 and t2 > 0:
                        x = p1["vel"][0] * t1 + p1["pos"][0]
                        y = p1["vel"][1] * t1 + p1["pos"][1]
                        if (
                            x >= limits[0]
                            and x <= limits[1]
                            and y >= limits[0]
                            and y <= limits[1]
                        ):
                            c += 1
            j += 1
        i += 1
    return c


def main(filename, limits):
    hailstones = parseInformation(filename)
    c = findEstimate(hailstones, limits)
    return c


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 24, [2], main, [7, 27])
    else:
        ans = getAnswer(2023, 24, main, [200000000000000, 400000000000000])
        print("The number of intersections within the test area is: {0}".format(ans))
