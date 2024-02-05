from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    return list(tmp[0])


def checkMarkerLocation(stream, uniqueStream):
    distinctCharacters = uniqueStream
    idx = 0
    currentStarter = {}
    # Store fist nCharacters in hash map
    while idx < distinctCharacters:
        k = stream[idx]
        if k in currentStarter:
            currentStarter[k] += 1
        else:
            currentStarter[k] = 1
        idx += 1
    # While unique consecutive characters is different from distinctCharacters
    while len(currentStarter) < distinctCharacters:
        # Remove last character in sequence to count the next one
        k = stream[idx - distinctCharacters]
        if currentStarter[k] > 1:
            currentStarter[k] -= 1
        else:
            currentStarter.pop(k)
        # Count next character
        k = stream[idx]
        if k in currentStarter:
            currentStarter[k] += 1
        else:
            currentStarter[k] = 1
        idx += 1
    return idx


def main(filename):
    s = parseInformation(filename)
    uniqueStream = 4
    location = checkMarkerLocation(s, uniqueStream)
    return location


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 6, [7, 5, 6, 10, 11], main)
    else:
        ans = getAnswer(2022, 6, main)
        print(
            "The character location at which the first 4-character long starter marker is detected is {0}".format(
                ans
            )
        )
