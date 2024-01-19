from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
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
    # Finding the blocking trees: [left-right, right-left,top-bottom,bottom-top]
    blockingHeight = []
    # Left to right
    for i in range(1, len(mainView) - 1):
        tmp = []
        maxi = 0
        for j in range(1, len(mainView[0]) - 1):
            maxi = max(maxi, int(mainView[i][j - 1]))
            tmp.append([maxi])
        blockingHeight.append(tmp)
    # Right to left
    for i in range(1, len(mainView) - 1):
        maxi = 0
        for j in range(len(mainView[0]) - 1, 1, -1):
            maxi = max(maxi, int(mainView[i][j]))
            blockingHeight[i - 1][j - 2].append(maxi)
    # Top to bottom
    for j in range(1, len(mainView[0]) - 1):
        maxi = 0
        for i in range(1, len(mainView) - 1):
            maxi = max(maxi, int(mainView[i - 1][j]))
            blockingHeight[i - 1][j - 1].append(maxi)
    # Bottom to top
    for j in range(1, len(mainView[0]) - 1):
        maxi = 0
        for i in range(len(mainView) - 1, 1, -1):
            maxi = max(maxi, int(mainView[i][j]))
            blockingHeight[i - 2][j - 1].append(maxi)
    # Resolution
    visible = len(mainView) * 2 + (len(mainView[0]) - 2) * 2
    for i in range(1, len(mainView) - 1):
        for j in range(1, len(mainView[0]) - 1):
            isBlocked = True
            for tmp in blockingHeight[i - 1][j - 1]:
                if tmp < int(mainView[i][j]):
                    isBlocked = False
                    break
            if not (isBlocked):
                visible += 1
    return visible


def main(filename):
    mainView = parseInformation(filename)
    visible = hiddenTrees(mainView)
    return visible


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(8, [21], main)
    else:
        ans = getAnswer(8, main)
        print("The number of visible trees is {0}".format(ans))
