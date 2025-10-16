from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    rows = [row.split(' ') for row in data.rstrip().split('\n')]
    print(rows)
    return rows 


def iterateCalls(rows):
    return 0 

def main(filename):
    rows = parseInformation(filename)
    sequence = iterateCalls(rows)
    return sequence 

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 10, [6], main, test=["1"])
    else:
        iterations = getAnswer(2015, 10, main)
        print("The length of the final sequence after the defined iterations is {0}".format(iterations))