from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    routes = data.rstrip().split('\n')
    print(routes)
    return routes


def shortestDistance(routes):
    return 0

def main(filename):
    routes = parseInformation(filename)
    d = shortestDistance(routes)
    return d

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 9, [605], main, test=["1"])
    else:
        d = getAnswer(2015, 9, main)
        print("The shortest travel distane visiting every node at least once is {0}".format(d))