from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    steps = []
    for line in lines:
        if line.strip() != "":
            steps = list(line.strip().split(","))
    return steps


def hash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def sumOfResults(steps):
    net = 0
    for step in steps:
        net += hash(step)
    return net


def main(filename):
    steps = parseInformation(filename)
    net = sumOfResults(steps)
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
        performTests(2023, 15, [1320], main)
    else:
        ans = getAnswer(2023, 15, main)
        print("The sum of results is: {0}".format(ans))
