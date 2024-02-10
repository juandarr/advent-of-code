from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename, rows):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    r = []
    # Read lines
    row = 0
    expansionFactor = rows
    # The effective expansion, since the original row and column are preserved
    expansion = expansionFactor - 1
    for line in lines:
        tmp = line.strip()
        if tmp == "." * len(tmp):
            r.append(row)
        m.append(list(tmp))
        row += 1
    galaxies = []
    c = []
    j = 0
    # Expand by columns and store location of galaxies
    while j < len(m[0]):
        allDots = True
        for i in range(len(m)):
            if m[i][j] != ".":
                allDots = False
                break
        if allDots:
            c.append(j)
        else:
            for i in range(len(m)):
                if m[i][j] == "#":
                    galaxies.append(
                        (
                            i + expansion * len([val for val in r if val < i]),
                            j + expansion * len([val for val in c if val < j]),
                        )
                    )
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


def main(filename, rows):
    m, galaxies = parseInformation(filename, rows)
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
        performTests(2023, 11, [8410], main, 100)
    else:
        ans = getAnswer(2023, 11, main)
        print("The sum of shortest paths is: {0}".format(ans))
