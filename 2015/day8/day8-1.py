from os.path import dirname, abspath
import sys
import hashlib

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    strs = data.rstrip().split('\n')
    print(strs)
    return strs


def getDiff(strs):
    return 0

def main(filename):
    strs = parseInformation(filename)
    dif = getDiff(strs)
    return dif

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 8, [12], main, test=["1"])
    else:
        dif = getAnswer(2015, 8, main)
        print("The difference between number of characters of code and characters in memory is {0}".format(dif))

