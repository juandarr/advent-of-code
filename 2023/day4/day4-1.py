from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    candidateList = []
    winnerList = []
    for line in lines:
        tmp = line.strip().split(":")
        numberSets = tmp[1].strip().split("|")
        winnerSet = set(numberSets[0].strip().split())
        candidates = numberSets[1].strip().split()
        candidateList.append(candidates)
        winnerList.append(winnerSet)
    return candidateList, winnerList


def score(candidateList, winnerList):
    score = 0
    for idx, candidates in enumerate(candidateList):
        matches = 0
        for candidate in candidates:
            if candidate in winnerList[idx]:
                matches += 1
        if matches > 0:
            score += 2 ** (matches - 1)
    return score


def main(filename):
    candidateList, winnerList = parseInformation(filename)
    net = score(candidateList, winnerList)
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
        performTests(2023, 4, [13], main)
    else:
        ans = getAnswer(2023, 4, main)
        print("The score is: {0}".format(ans))
