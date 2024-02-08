from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

"""
In this problem we need to develop a sorting mechanism to classify a
given hand by its rank and value of its cards 
"""
cardValue = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def parseInformation(filename):
    lines = open(filename, "r")
    hands = []
    for line in lines:
        tmp = line.strip().split()
        hands.append(tmp)
    return hands


def compareHands(hand1, hand2):
    for index, h in enumerate(hand1):
        if cardValue[h] > cardValue[hand2[index]]:
            return 1
        elif cardValue[h] < cardValue[hand2[index]]:
            return 2
        else:
            continue


def sortHands(hands):
    c = 0
    while c < len(hands) - 1:
        cInc = 0
        while cInc < len(hands) - c - 1:
            comp = compareHands(hands[cInc][0], hands[cInc + 1][0])
            if comp == 1:
                tmp = hands[cInc]
                hands[cInc] = hands[cInc + 1]
                hands[cInc + 1] = tmp
            cInc += 1
        c += 1
    return hands


def totalWinnings(hands):
    groups = {"5K": [], "4K": [], "FH": [], "3K": [], "2P": [], "1P": [], "1K": []}
    for hand in hands:
        i = len(set(hand[0]))
        joker = 0
        for h in hand[0]:
            if h == "J":
                joker += 1
        if i == 1:
            groups["5K"].append(hand)
        elif i == 2:
            if joker > 0:
                groups["5K"].append(hand)
                continue
            fh = True
            for h in set(hand[0]):
                repetition = 0
                for tmp in hand[0]:
                    if h == tmp:
                        repetition += 1
                if repetition == 4:
                    fh = False
                    break
            if fh:
                groups["FH"].append(hand)
            else:
                groups["4K"].append(hand)
        elif i == 3:
            twoPairs = True
            for h in set(hand[0]):
                repetition = 0
                for tmp in hand[0]:
                    if h == tmp:
                        repetition += 1
                if repetition == 3:
                    twoPairs = False
                    break
            if twoPairs:
                if joker == 1:
                    groups["FH"].append(hand)
                elif joker == 2:
                    groups["4K"].append(hand)
                else:
                    groups["2P"].append(hand)
            else:
                if joker > 0:
                    groups["4K"].append(hand)
                else:
                    groups["3K"].append(hand)
        elif i == 4:
            if joker > 0:
                groups["3K"].append(hand)
            else:
                groups["1P"].append(hand)
        else:
            if joker == 1:
                groups["1P"].append(hand)
            else:
                groups["1K"].append(hand)
    rankHands = ["1K", "1P", "2P", "3K", "FH", "4K", "5K"]
    for rank in rankHands:
        hands = groups[rank]
        groups[rank] = sortHands(hands)
    c = 1
    net = 0
    for rank in rankHands:
        for hand in groups[rank]:
            net += c * int(hand[1])
            c += 1
    return net


def main(filename):
    hands = parseInformation(filename)
    winnings = totalWinnings(hands)
    return winnings


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 7, [5905], main)
    else:
        ans = getAnswer(2023, 7, main)
        print("The total winnings is: {0}".format(ans))
