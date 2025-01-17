from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    rows = values.rstrip().split("\n")
    a = []
    b = []
    for row in rows:
        tmp = row.split("   ")
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    return [a,b]


def sumScores(l):
    total = 0
    a = sorted(l[0])
    b = sorted(l[1])
    score = {}
    for aVal in a:
        if aVal in score:
            total+= score[aVal]
            continue
        try:
            idx  = b.index(aVal)
        except:
            score[aVal] = 0
            continue
        count = 0
        for i in range(idx, len(b)):
            if (b[i]==aVal):
                count += 1
            else:
                break
        score[aVal] = aVal*count
        total += score[aVal]
    return total


def main(filename):
    l = parseInformation(filename)
    total = sumScores(l)
    return total


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 1, [31], main)
    else:
        total = getAnswer(2024, 1, main)
        print("The sum of scores for the vales on the left list is: {0}".format(total))