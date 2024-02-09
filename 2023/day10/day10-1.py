from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    origin = (0, 0)
    for line in lines:
        m.append(list(line.strip()))
        for index, v in enumerate(m[-1]):
            if "S" == v:
                origin = (len(m) - 1, index)
    return m, origin


def stepsFromStartPositionToFurthest(m, origin):
    shapes = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, -1), (1, 0)],
        "F": [(1, 0), (0, 1)],
    }
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    cur = origin
    candidates = []
    for d in dirs:
        i = cur[0] + d[0]
        j = cur[1] + d[1]
        if m[i][j] != ".":
            if (-d[0], -d[1]) in shapes[m[i][j]]:
                idx = shapes[m[i][j]].index((-d[0], -d[1]))
                candidates.append(((i, j), shapes[m[i][j]][abs(idx - 1)]))
    visited = {origin: 1}
    complete = False
    while candidates != [] and not (complete):
        cur = candidates.pop()
        curNode = cur[0]
        visited[curNode] = 1
        complete = False
        d = cur[1]
        i = curNode[0] + d[0]
        j = curNode[1] + d[1]
        if m[i][j] == "S" and len(visited) > 3:
            complete = True
            break
        if m[i][j] not in [".", "S"] and m[i][j] not in visited:
            if (-d[0], -d[1]) in shapes[m[i][j]]:
                idx = shapes[m[i][j]].index((-d[0], -d[1]))
                candidates.append(((i, j), shapes[m[i][j]][abs(idx - 1)]))
    return int(len(visited) / 2)


def main(filename):
    m, origin = parseInformation(filename)
    steps = stepsFromStartPositionToFurthest(m, origin)
    return steps


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 10, [8, 4], main, test=["1", "2"])
    else:
        ans = getAnswer(2023, 10, main)
        print(
            "The number of steps farthest from the starting position is: {0}".format(
                ans
            )
        )
