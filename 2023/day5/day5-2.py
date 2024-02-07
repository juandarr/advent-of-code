from time import time

from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    c = 0
    seedsRanges = ""
    mapping = {}
    currentMapping = ""
    for line in lines:
        if c == 0:
            tmp = line.strip().split(":")[1].strip().split()
            seedsRanges = [tmp[n : n + 2] for n in range(0, len(tmp), 2)]
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
    return seedsRanges, mapping


def locationNumber(seedsRanges, mapping):
    mappingLabels = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    inputRanges = seedsRanges
    outputRanges = []
    ln = 0
    for label in mappingLabels:
        if outputRanges != []:
            inputRanges = outputRanges.copy()
        outputRanges = []
        for s in mapping[label]:
            c = 0
            tmp = []
            while c < len(inputRanges):
                ranges = inputRanges[c]
                # Lists cases of range overlapping
                # outside to the left -works
                if int(s[1]) + int(s[2]) - 1 < int(ranges[0]):
                    # print('outside to the left', s, ranges)
                    tmp.append(inputRanges[c])
                # outside to the right - works
                if int(s[1]) > int(ranges[0]) + int(ranges[1]) - 1:
                    # print('outside to the right', s, ranges)
                    tmp.append(inputRanges[c])
                # intersection to the left - works
                if (
                    int(s[1]) < int(ranges[0])
                    and int(s[1]) + int(s[2]) - 1 < int(ranges[0]) + int(ranges[1]) - 1
                    and int(s[1]) + int(s[2]) - 1 >= int(ranges[0])
                ):
                    dif = int(ranges[0]) - int(s[1])
                    tmp.append(
                        [
                            int(s[1]) + int(s[2]),
                            int(ranges[0]) + int(ranges[1]) - int(s[1]) - int(s[2]),
                        ]
                    )
                    outputRanges.append(
                        [int(s[0]) + dif, int(s[1]) + int(s[2]) - int(ranges[0])]
                    )
                # intersection to the right - works
                if (
                    int(s[1]) + int(s[2]) - 1 > int(ranges[0]) + int(ranges[1]) - 1
                    and int(s[1]) <= int(ranges[0]) + int(ranges[1]) - 1
                    and int(s[1]) > int(ranges[0])
                ):
                    dif = int(ranges[0]) + int(ranges[1]) - int(s[1])
                    tmp.append([int(ranges[0]), int(ranges[1]) - dif])
                    outputRanges.append([int(s[0]), dif])
                # inside the range - works
                if (
                    int(s[1]) >= int(ranges[0])
                    and int(s[1]) + int(s[2]) - 1 <= int(ranges[0]) + int(ranges[1]) - 1
                ):
                    if int(s[1]) - int(ranges[0]) > 0:
                        tmp.append([int(ranges[0]), int(s[1]) - int(ranges[0])])
                    if (int(ranges[0]) + int(ranges[1])) - (int(s[1]) + int(s[2])) > 0:
                        tmp.append(
                            [
                                int(s[1]) + int(s[2]),
                                (int(ranges[0]) + int(ranges[1]))
                                - (int(s[1]) + int(s[2])),
                            ]
                        )
                    outputRanges.append([int(s[0]), int(s[2])])
                # covering whole range - works
                if (
                    int(s[1]) <= int(ranges[0])
                    and int(s[1]) + int(s[2]) - 1 >= int(ranges[0]) + int(ranges[1]) - 1
                ):
                    outputRanges.append(
                        [int(s[0]) + int(ranges[0]) - int(s[1]), int(ranges[1])]
                    )
                c += 1
            inputRanges = tmp.copy()
        ln += 1
        for ranges in tmp:
            outputRanges.append(ranges)
        if ln == 7:
            break
    minVal = float("inf")
    for ranges in outputRanges:
        if ranges[0] < minVal:
            minVal = ranges[0]
    return minVal


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
        performTests(2023, 5, [46], main)
    else:
        ans = getAnswer(2023, 5, main)
        print("The lowest location is: {0}".format(ans))
