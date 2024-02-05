from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    return open(filename, "r")


def addValues(lines):
    digits = "123456789"
    digitsWords = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    net = 0
    c = 0
    for line in lines:
        start = [float("inf"), None]
        for d in digits:
            tmp = line.find(d)
            if tmp >= 0 and tmp < start[0]:
                start = [tmp, d]
        for dw in digitsWords:
            tmp = line.find(dw)
            if tmp >= 0 and tmp < start[0]:
                start = [tmp, digitsWords[dw]]
        end = [float("inf"), None]
        lineReversed = line[::-1]
        for d in digits:
            tmp = lineReversed.find(d)
            if tmp >= 0 and tmp < end[0]:
                end = [tmp, d]
        for dw in digitsWords:
            tmp = lineReversed.find(dw[::-1])
            if tmp >= 0 and tmp + len(dw) - 1 < end[0]:
                end = [tmp + len(dw) - 1, digitsWords[dw]]
        val = int("{0}{1}".format(start[1], end[1]))
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
        performTests(1, [142, 281], main)
    else:
        biggest = getAnswer(1, main)
        print("The sum of the calibration values is: {0}".format(biggest))
