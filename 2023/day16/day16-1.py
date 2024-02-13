from os.path import dirname, abspath
import sys

# sys.setrecursionlimit(10**5)

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402
from time import sleep, time


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.read()
    # Read lines and expand by rows
    lines = lines.split("\n")
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m


def inLimits(m, i, j):
    if i < 0 or i > len(m) - 1 or j < 0 or j > len(m[0]) - 1:
        return False
    return True


def changeDir(d, mirror):
    tmp = []
    if mirror == "\\":
        tmp = (d[1], d[0])
    elif mirror == "/":
        tmp = (-1 * d[1], -1 * d[0])
    return tuple(tmp)


def runBeam(m, start, dir, visited):
    i = start[0]
    j = start[1]
    curDir = dir
    while inLimits(m, i, j) and ((i, j), curDir) not in visited:
        visited.add(((i, j), curDir))
        if m[i][j] != ".":
            if m[i][j] in ["|", "-"]:
                if m[i][j] == "|" and curDir in [(0, 1), (0, -1)]:
                    visited.union(runBeam(m, [i - 1, j], (-1, 0), visited))
                    visited.union(runBeam(m, [i + 1, j], (1, 0), visited))
                    break
                if m[i][j] == "-" and curDir in [(1, 0), (-1, 0)]:
                    visited.union(runBeam(m, [i, j + 1], (0, 1), visited))
                    visited.union(runBeam(m, [i, j - 1], (0, -1), visited))
                    break
            else:
                curDir = changeDir(curDir, m[i][j])
        i += curDir[0]
        j += curDir[1]
    return visited


def energizedTiles(m):
    startDir = (0, 1)
    start = [0, 0]
    visited = set()
    visited = runBeam(m, start, startDir, visited)
    final = set()
    for i in visited:
        final.add(i[0])
    return len(final)


def main(filename):
    m = parseInformation(filename)
    ans = energizedTiles(m)
    return ans


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 16, [46], main)
    else:
        ans = getAnswer(2023, 16, main)
        print("The focusing power is: {0}".format(ans))
