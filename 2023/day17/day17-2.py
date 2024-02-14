from os.path import dirname, abspath
import sys
import heapq

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


def inLimits(i, j, m):
    if i < 0 or i > len(m) - 1 or j < 0 or j > len(m[0]) - 1:
        return False
    return True


def explore(starts, m, minM):
    toExpand = []
    for start in starts:
        heapq.heappush(toExpand, start)
    visited = set()
    while toExpand:
        curEnergy, curNode, curDir, steps = heapq.heappop(toExpand)
        if curNode == (len(m) - 1, len(m[0]) - 1):
            return curEnergy
        if (curNode, curDir, steps) in visited:
            continue
        visited.add((curNode, curDir, steps))
        dir = (curDir, (curDir[1], curDir[0]), (-1 * curDir[1], -1 * curDir[0]))
        for d in dir:
            if steps < 4 and curDir != d:
                continue
            nextNode = (curNode[0] + d[0], curNode[1] + d[1])
            straight = 1
            if curDir == d:
                straight += steps
            if not (inLimits(nextNode[0], nextNode[1], m)) or straight > 10:
                continue
            tmp = curEnergy + int(m[nextNode[0]][nextNode[1]])
            if tmp < minM[nextNode[0]][nextNode[1]]:
                minM[nextNode[0]][nextNode[1]] = tmp
            heapq.heappush(toExpand, (tmp, nextNode, d, straight))


def leastHeatLoss(m):
    minM = []
    for i in range(len(m)):
        minM.append([])
        for _ in range(len(m[0])):
            minM[i].append(float("inf"))
    minM[0][0] = 0
    m[0][0] = 0
    minM[0][1] = int(m[0][1])
    minM[1][0] = int(m[1][0])
    s = explore(
        ((int(m[0][1]), (0, 1), (0, 1), 1), (int(m[1][0]), (1, 0), (1, 0), 1)), m, minM
    )
    return s


def main(filename):
    m = parseInformation(filename)
    ans = leastHeatLoss(m)
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
        performTests(2023, 17, [94], main, test=["1"])
    else:
        ans = getAnswer(2023, 17, main)
        print("The least heat loss is: {0}".format(ans))
