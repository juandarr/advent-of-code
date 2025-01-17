from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    rows = values.rstrip().split("\n")
    a = []
    b = []
    for row in rows:
        tmp = row.split("   ")
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    print(a,b)
    return [a,b]


def sumDifference(l):
    total = 0
    return total


def main(filename):
    l = parseInformation(filename)
    total = sumDifference(l)
    return total


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 1, [0], main)
    else:
        total = getAnswer(2024, 1, main)
        print("The addition of differences of the sorted lists is: {0}".format(total))