import numpy as np
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


def findEstimate(hailstones):
    A = np.zeros((6, 6))
    B = np.zeros((6, 1))
    points = {}
    c = 1
    for hailstone in hailstones:
        points[c] = hailstone
        c += 1
        if c == 4:
            break
    p1 = points[1]["pos"]
    p2 = points[2]["pos"]
    p3 = points[3]["pos"]
    v1 = points[1]["vel"]
    v2 = points[2]["vel"]
    v3 = points[3]["vel"]

    A[0, 0] = v2[1] - v1[1]
    A[0, 1] = v1[0] - v2[0]
    A[0, 2] = 0
    A[0, 3] = p1[1] - p2[1]
    A[0, 4] = p2[0] - p1[0]
    A[0, 5] = 0

    A[1, 0] = v2[2] - v1[2]
    A[1, 1] = 0
    A[1, 2] = v1[0] - v2[0]
    A[1, 3] = p1[2] - p2[2]
    A[1, 4] = 0
    A[1, 5] = p2[0] - p1[0]

    A[2, 0] = 0
    A[2, 1] = v2[2] - v1[2]
    A[2, 2] = v1[1] - v2[1]
    A[2, 3] = 0
    A[2, 4] = p1[2] - p2[2]
    A[2, 5] = p2[1] - p1[1]

    A[3, 0] = v3[1] - v1[1]
    A[3, 1] = v1[0] - v3[0]
    A[3, 2] = 0
    A[3, 3] = p1[1] - p3[1]
    A[3, 4] = p3[0] - p1[0]
    A[3, 5] = 0

    A[4, 0] = v3[2] - v1[2]
    A[4, 1] = 0
    A[4, 2] = v1[0] - v3[0]
    A[4, 3] = p1[2] - p3[2]
    A[4, 4] = 0
    A[4, 5] = p3[0] - p1[0]

    A[5, 0] = 0
    A[5, 1] = v3[2] - v1[2]
    A[5, 2] = v1[1] - v3[1]
    A[5, 3] = 0
    A[5, 4] = p1[2] - p3[2]
    A[5, 5] = p3[1] - p1[1]

    B[0, 0] = p2[0] * v2[1] - p2[1] * v2[0] - p1[0] * v1[1] + p1[1] * v1[0]
    B[1, 0] = p2[0] * v2[2] - p2[2] * v2[0] - p1[0] * v1[2] + p1[2] * v1[0]
    B[2, 0] = p2[1] * v2[2] - p2[2] * v2[1] - p1[1] * v1[2] + p1[2] * v1[1]
    B[3, 0] = p3[0] * v3[1] - p3[1] * v3[0] - p1[0] * v1[1] + p1[1] * v1[0]
    B[4, 0] = p3[0] * v3[2] - p3[2] * v3[0] - p1[0] * v1[2] + p1[2] * v1[0]
    B[5, 0] = p3[1] * v3[2] - p3[2] * v3[1] - p1[1] * v1[2] + p1[2] * v1[1]

    s = np.linalg.solve(A, B)
    ans = 0
    for i in range(3):
        ans += round(s[i, 0])
    return ans


def main(filename):
    hailstones = parseInformation(filename)
    c = findEstimate(hailstones)
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
        performTests(2023, 24, [47], main)
    else:
        ans = getAnswer(2023, 24, main)
        print(
            "The sum of x,y,z coordinates of the initial position is: {0}".format(ans)
        )
