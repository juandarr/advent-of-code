from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

digits = {
    "0": True,
    "1": True,
    "2": True,
    "3": True,
    "4": True,
    "5": True,
    "6": True,
    "7": True,
    "8": True,
    "9": True,
}


def parseInformation(filename):
    return open(filename, "r")


def checkItem(matrix, i, j):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dir in dirs:
        iTmp = i + dir[1]
        if iTmp < 0 or iTmp >= len(matrix):
            continue
        jTmp = j + dir[0]
        if jTmp < 0 or jTmp >= len(matrix[iTmp]):
            continue
        if matrix[iTmp][jTmp] not in digits and matrix[iTmp][jTmp] != ".":
            return True
    return False


def sumPartNumbers(lines):
    m = []
    for line in lines:
        m.append(list(line.strip()))
    i = 0
    j = 0
    net = 0
    while i < len(m):
        tmp = ""
        isItem = False
        j = 0
        while j < len(m[i]):
            if m[i][j] in digits:
                tmp += m[i][j]
                if not (isItem):
                    isItem = checkItem(m, i, j)
                if j == len(m[i]) - 1:
                    if tmp != "" and isItem:
                        net += int(tmp)
            else:
                if tmp != "" and isItem:
                    net += int(tmp)
                tmp = ""
                isItem = False
            j += 1
        i += 1
    return net


def main(filename):
    lines = parseInformation(filename)
    net = sumPartNumbers(lines)
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
        performTests(2023, 3, [4361], main)
    else:
        ans = getAnswer(2023, 3, main)
        print("The sum of all part numbers is: {0}".format(ans))
