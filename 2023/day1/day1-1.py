from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    return open(filename, "r")


def addValues(lines):
    digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    net = 0
    for line in lines:
        values = []
        for s in line:
            try:
                if int(s) in digits:
                    values.append(int(s))
            except:
                continue
        if len(values) > 0:
            val = int("{0}{1}".format(values[0], values[-1]))
            net += val
    return net


def main(filename):
    lines = parseInformation(filename)
    net = addValues(lines)
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
        performTests(1, [142, 209], main)
    else:
        biggest = getAnswer(1, main)
        print("The sum of the calibration values is: {0}".format(biggest))
