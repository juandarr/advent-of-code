from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    actions = []
    for row in tmp:
        actions.append(list(row.split(" ")))
    return actions


def traverseBridge(actions, knots):
    positions = []
    for i in range(knots):
        positions.append([0, 0])
    visited = {(positions[knots - 1][0], positions[knots - 1][1]): 1}
    visitCounter = 1
    movements = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for action in actions:
        for i in range(int(action[1])):
            positions[0][0] += movements[action[0]][0]
            positions[0][1] += movements[action[0]][1]
            for k in range(1, knots):
                xH = positions[k - 1][0]
                xT = positions[k][0]
                yH = positions[k - 1][1]
                yT = positions[k][1]
                if (xH == xT) and abs(yH - yT) > 1:
                    positions[k][1] += int((yH - yT) / abs(yH - yT))
                elif (yH == yT) and abs(xH - xT) > 1:
                    positions[k][0] += int((xH - xT) / abs(xH - xT))
                elif abs(xH - xT) >= 1 and abs(yH - yT) > 1:
                    positions[k][1] += int((yH - yT) / abs(yH - yT))
                    positions[k][0] += int((xH - xT) / abs(xH - xT))
                elif abs(yH - yT) >= 1 and abs(xH - xT) > 1:
                    positions[k][1] += int((yH - yT) / abs(yH - yT))
                    positions[k][0] += int((xH - xT) / abs(xH - xT))
            if (positions[knots - 1][0], positions[knots - 1][1]) not in visited:
                visited[(positions[knots - 1][0], positions[knots - 1][1])] = 1
                visitCounter += 1
    return visitCounter


def main(filename):
    actions = parseInformation(filename)
    knots = 10
    visitCounter = traverseBridge(actions, knots)
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
        performTests(9, [1, 36], main)
    else:
        ans = getAnswer(9, main)
        print("The number of visited positions by tail is {0}".format(ans))
