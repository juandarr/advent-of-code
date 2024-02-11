from time import time
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    # Read lines and expand by rows
    for line in lines:
        tmp = line.strip().split()
        m.append([list(tmp[0]), tmp[1].split(",")])
    return m


mem = {}


def findSequence(path, sequence):
    key = ("".join(path), ",".join(sequence))
    if key in mem:
        return mem[key]
    if sequence == []:
        valid = True
        for s in "".join(path):
            if s not in [".", "?"]:
                valid = False
                break
        if valid:
            return 1
        else:
            return 0
    seqVal = int(sequence[0])
    c = 0
    i = 0
    while c < len(path):
        if path[c] == "#":
            i += 1
            if i > seqVal:
                break
        elif path[c] == ".":
            if i == seqVal:
                s = findSequence(path[c + 1 :], sequence[1:])
                mem[key] = s
                return s
            elif i > 0 and i < seqVal:
                break
        elif path[c] == "?":
            if i == seqVal:
                path[c] = "."
                s = findSequence(path[c + 1 :], sequence[1:])
                mem[key] = s
                return s
            elif i == 0:
                net = 0
                for s in [".", "#"]:
                    path[c] = s
                    if s == ".":
                        net += findSequence(path[c + 1 :], sequence)
                    elif s == "#":
                        net += findSequence(path[c:], sequence)
                mem[key] = net
                return net
            elif i < seqVal:
                path[c] = "#"
                i += 1
        c += 1
    if i == seqVal and len(sequence) == 1:
        return 1
    return 0


def sumOfPossibleArrangements(m):
    net = 0
    for row in m:
        path = row[0].copy()
        sequence = row[1].copy()
        for _ in range(4):
            path += ["?"] + row[0].copy()
            sequence += row[1].copy()
        net += findSequence(path, sequence)
    return net


def main(filename):
    m = parseInformation(filename)
    net = sumOfPossibleArrangements(m)
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
        performTests(2023, 12, [525152], main)
    else:
        ans = getAnswer(2023, 12, main)
        print("The sum of possible arrangements is: {0}".format(ans))
