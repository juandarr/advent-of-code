from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    expansion = 2
    # Read lines and expand by rows
    for line in lines:
        tmp = line.strip()
        if tmp == "." * len(tmp):
            for _ in range(expansion):
                m.append(list(tmp))
        else:
            m.append(list(tmp))
    expanded = []
    for _ in range(len(m)):
        expanded.append([])
    j = 0
    galaxies = []
    # Expand by columns and store location of galaxies
    while j < len(m[0]):
        allDots = True
        for i in range(len(m)):
            if m[i][j] != ".":
                allDots = False
                break
        if allDots:
            for i in range(len(expanded)):
                for _ in range(expansion):
                    expanded[i].append(".")
        else:
            for i in range(len(expanded)):
                expanded[i].append(m[i][j])
                if expanded[i][-1] == "#":
                    galaxies.append((i, len(expanded[i]) - 1))
        j += 1
    return m, galaxies


def sumShortestPath(m, galaxies):
    net = 0
    for idx, galaxy in enumerate(galaxies):
        i = idx + 1
        while i < len(galaxies):
            galaxy2 = galaxies[i]
            d = abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
            net += d
            i += 1
    return net


def main(filename):
    m, galaxies = parseInformation(filename)
    net = sumShortestPath(m, galaxies)
    return net


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 11, [374], main)
    else:
        ans = getAnswer(2023, 11, main)
        print("The sum of shortest paths is: {0}".format(ans))
