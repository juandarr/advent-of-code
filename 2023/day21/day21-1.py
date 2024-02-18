from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    m = []
    c = 0
    start = ()
    for line in lines:
        tmp = list(line.strip())
        for idx, val in enumerate(tmp):
            if val == "S":
                start = (c, idx)
        c += 1
        m.append(tmp)
    return m, start


def steps(s, step, m, dir, limit):
    counter = 0
    branches = set()
    branches.add(s)
    tmp = set()
    while step <= limit:
        tmp = set()
        for b in branches:
            for d in dir:
                i = b[0] + dir[d][0]
                j = b[1] + dir[d][1]
                if i < 0 or i > len(m) - 1:
                    continue
                if j < 0 or j > len(m[0]) - 1:
                    continue
                if m[i][j] in [".", "S"]:
                    tmp.add((i, j))
        counter += len(tmp)
        branches = tmp
        step += 1
    return len(tmp)


def main(filename, limit):
    m, start = parseInformation(filename)
    dir = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    s = steps(start, 1, m, dir, limit)
    return s


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 21, [16], main, 6)
    else:
        ans = getAnswer(2023, 21, main, 64)
        print("The number of garden plots reached is: {0}".format(ans))
