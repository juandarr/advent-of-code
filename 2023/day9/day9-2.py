from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    sequence = []
    for line in lines:
        sequence.append(line.strip().split())
    return sequence


def checkZeroes(ar):
    allZeroes = True
    for x in ar:
        if x != 0:
            allZeroes = False
            break
    return allZeroes


def sumExtrapolatedValues(sequence):
    net = 0
    for ar in sequence:
        cur = []
        for x in ar:
            cur.append(int(x))
        allZeroes = checkZeroes(cur)
        levels = [cur]
        while not (allZeroes):
            tmp = []
            c = 0
            while c < len(cur) - 1:
                tmp.append(cur[c + 1] - cur[c])
                c += 1
            cur = tmp
            levels.append(cur)
            allZeroes = checkZeroes(cur)
        c = len(levels) - 2
        extra = []
        extra.append(0)
        while c >= 0:
            extra.append(-extra[-1] + levels[c][0])
            c -= 1
        net += extra[-1]
    return net


def main(filename):
    sequence = parseInformation(filename)
    s = sumExtrapolatedValues(sequence)
    return s


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 9, [2], main)
    else:
        ans = getAnswer(2023, 9, main)
        print("The sum of extrapolated values is: {0}".format(ans))
