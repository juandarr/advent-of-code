from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


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
    netMax = -float("inf")
    for j in range(len(m[0])):
        start = [0, j]
        startDir = (1, 0)
        visited = set()
        visited = runBeam(m, start, startDir, visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final) > netMax:
            netMax = len(final)
    for j in range(len(m[0])):
        start = [len(m) - 1, j]
        startDir = (-1, 0)
        visited = set()
        visited = runBeam(m, start, startDir, visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final) > netMax:
            netMax = len(final)
    for i in range(len(m)):
        start = [i, 0]
        startDir = (0, 1)
        visited = set()
        visited = runBeam(m, start, startDir, visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final) > netMax:
            netMax = len(final)
    for i in range(len(m)):
        start = [i, len(m[0]) - 1]
        startDir = (0, -1)
        visited = set()
        visited = runBeam(m, start, startDir, visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final) > netMax:
            netMax = len(final)
    return netMax


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
        performTests(2023, 16, [51], main)
    else:
        ans = getAnswer(2023, 16, main)
        print("The number of energized tiles is: {0}".format(ans))
