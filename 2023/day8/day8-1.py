from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    directions = lines[0].strip()
    nodes = {}
    for line in lines[2:]:
        tmp = line.strip().split("=")
        key = tmp[0].strip()
        value = tmp[1].strip().split(",")
        nodes[key] = [value[0].strip()[1:], value[1].strip()[:-1]]
    return nodes, directions


def stepsToReachGoal(nodes, directions):
    dirsIndex = {"L": 0, "R": 1}
    startNode = "AAA"
    endNode = "ZZZ"
    curNode = startNode
    steps = 0
    while curNode != endNode:
        for d in directions:
            curNode = nodes[curNode][dirsIndex[d]]
            steps += 1
            if curNode == endNode:
                break
    return steps


def main(filename):
    nodes, directions = parseInformation(filename)
    steps = stepsToReachGoal(nodes, directions)
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
        performTests(2023, 8, [2, 6], main, test=["1", "2"])
    else:
        ans = getAnswer(2023, 8, main)
        print("The steps required to reach ZZZ are: {0}".format(ans))
