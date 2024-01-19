from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    actions = []
    for row in tmp:
        actions.append(list(row.split(" ")))
    return actions


def traverseBridge(actions):
    xT = 0
    yT = 0
    xH = 0
    yH = 0
    visited: dict = {(xT, yT): 1}
    visitCounter = 1
    movements = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
    for action in actions:
        for _ in range(int(action[1])):
            xH += movements[action[0]][0]
            yH += movements[action[0]][1]
            if xH == xT:
                if abs(yH - yT) > 1:
                    yT += int((yH - yT) / abs(yH - yT))
            elif yH == yT:
                if abs(xH - xT) > 1:
                    xT += int((xH - xT) / abs(xH - xT))
            elif abs(xH - xT) == 1:
                if abs(yH - yT) > 1:
                    yT += int((yH - yT) / abs(yH - yT))
                    xT += xH - xT
            elif abs(yH - yT) == 1:
                if abs(xH - xT) > 1:
                    yT += yH - yT
                    xT += int((xH - xT) / abs(xH - xT))
            key = (xT, yT)
            if key not in visited:
                visited[key] = 1
                visitCounter += 1
    return visitCounter


def main(filename):
    actions = parseInformation(filename)
    visitCounter = traverseBridge(actions)
    return visitCounter


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(9, [13, 88], main)
    else:
        ans = getAnswer(9, main)
        print("The number of visited positions by tail is {0}".format(ans))
