from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    lines = open(filename, "r")
    return lines


def getScore(line):
    tmp = line.strip().split(":")
    numberSets = tmp[1].strip().split("|")
    winnerSet = set(numberSets[0].strip().split())
    candidates = numberSets[1].strip().split()
    matches = 0
    for candidate in candidates:
        if candidate in winnerSet:
            matches += 1
    return matches


def replicate(scores, copies, cards):
    for card in cards:
        base = card
        for _ in range(scores[card]):
            base += 1
            if base > len(scores):
                break
            cards[base] += copies[card]
            copies[base] += copies[card]
        copies[card] = 0


def copyAndScore(lines):
    c = 1
    scores = {}
    cards = {}
    copies = {}
    for line in lines:
        scores[c] = getScore(line)
        cards[c] = 1
        copies[c] = 1
        c += 1
    replicate(scores, copies, cards)
    net = 0
    for card in cards:
        net += cards[card]
    return net


def main(filename):
    lines = parseInformation(filename)
    net = copyAndScore(lines)
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
        performTests(2023, 4, [30], main)
    else:
        ans = getAnswer(2023, 4, main)
        print("The total scratchcards is: {0}".format(ans))
