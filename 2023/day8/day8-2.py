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


def primeDecomposition(number):
    primes = {}
    tmp = number
    c = 0
    while tmp % 2 == 0:
        tmp /= 2
        c += 1
    if c > 0:
        primes[2] = c
    div = 3
    while tmp > 1:
        c = 0
        while tmp % div == 0:
            tmp /= div
            c += 1
        if c > 0:
            primes[div] = c
        div += 2
    return primes


def stepsToReachGoal(nodes, directions):
    dirsIndex = {"L": 0, "R": 1}
    endChar = "Z"
    curNodes = []
    endSteps = []
    completed = []
    for node in nodes:
        if node[-1] == "A":
            curNodes.append(node)
            endSteps.append(0)
            completed.append("f")
    steps = 0
    end = False
    net = 0
    while not (end):
        for d in directions:
            end = True
            for index, node in enumerate(curNodes):
                curNodes[index] = nodes[node][dirsIndex[d]]
                if curNodes[index][-1] != endChar:
                    end = False
                else:
                    if endSteps[index] == 0:
                        endSteps[index] = steps + 1
                        completed[index] = "t"
                    if "".join(completed) == "t" * len(endSteps):
                        end = True
                        break
            steps += 1
            if end is True:
                if "".join(completed) == "t" * len(endSteps):
                    for index, step in enumerate(endSteps):
                        endSteps[index] = primeDecomposition(step)
                    commonMultiple = {}
                    for stepDict in endSteps:
                        for key in stepDict:
                            if key in commonMultiple:
                                if commonMultiple[key] < stepDict[key]:
                                    commonMultiple[key] = stepDict[key]
                            else:
                                commonMultiple[key] = stepDict[key]
                    net = 1
                    for key in commonMultiple:
                        net *= key ** commonMultiple[key]
                break
    return net


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
        performTests(2023, 8, [6], main, test=["3"])
    else:
        ans = getAnswer(2023, 8, main)
        print("The steps required to nodes ending with Z are: {0}".format(ans))
