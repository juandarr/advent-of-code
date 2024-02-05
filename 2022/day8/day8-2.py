from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    mainView = []
    for row in tmp:
        mainView.append(list(row))
    return mainView


def hiddenTrees(mainView):
    # scores
    maxScore = 0
    for i in range(1, len(mainView) - 1):
        for j in range(1, len(mainView[0]) - 1):
            score = 1
            height = int(mainView[i][j])
            # left
            d = 0
            for k in range(j - 1, -1, -1):
                d += 1
                if height <= int(mainView[i][k]):
                    break
            score *= d
            # right
            d = 0
            for k in range(j + 1, len(mainView[0])):
                d += 1
                if height <= int(mainView[i][k]):
                    break
            score *= d
            # up
            d = 0
            for k in range(i - 1, -1, -1):
                d += 1
                if height <= int(mainView[k][j]):
                    break
            score *= d
            # down
            d = 0
            for k in range(i + 1, len(mainView)):
                d += 1
                if height <= int(mainView[k][j]):
                    break
            score *= d
            maxScore = max(maxScore, score)
    return maxScore


def main(filename):
    mainView = parseInformation(filename)
    score = hiddenTrees(mainView)
    return score


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 8, [8], main)
    else:
        ans = getAnswer(2022, 8, main)
        print("The highest scenic score is {0}".format(ans))
