from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    c = 0
    seeds = ""
    mapping = {}
    currentMapping = ""
    for line in lines:
        if c == 0:
            seeds = line.strip().split(":")[1].strip().split()
            c += 1
        else:
            tmp = line.strip()
            if tmp == "":
                continue
            if tmp != "" and tmp[-1] == ":":
                tmp = tmp.split(" ")
                currentMapping = tmp[0]
                mapping[currentMapping] = []
            else:
                tmp = tmp.split(" ")
                mapping[currentMapping].append(tmp)
    return seeds, mapping


def locationNumber(seeds, mapping):
    mappingLabels = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    minLocation = float("inf")
    for seed in seeds:
        currentNode = int(seed)
        for label in mappingLabels:
            for s in mapping[label]:
                if currentNode >= int(s[1]) and currentNode < int(s[1]) + int(s[2]):
                    dif = currentNode - int(s[1])
                    currentNode = int(s[0]) + dif
                    break
        if minLocation > currentNode:
            minLocation = currentNode
    return minLocation


def main(filename):
    seeds, mapping = parseInformation(filename)
    minLocation = locationNumber(seeds, mapping)
    return minLocation


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 5, [35], main)
    else:
        ans = getAnswer(2023, 5, main)
        print("The lowest location is: {0}".format(ans))
