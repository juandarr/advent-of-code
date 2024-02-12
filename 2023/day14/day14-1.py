from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    # Read lines and expand by rows
    for line in lines:
        m.append(list(line.strip()))
    return m


def moveRocks(m):
    i = 0
    net = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == "O":
                iTmp = i
                origin = [i, j]
                iTmp -= 1
                if iTmp < 0:
                    j += 1
                    net += len(m) - origin[0]
                    continue
                while m[iTmp][j] not in ["#", "O"]:
                    iTmp -= 1
                    if iTmp < 0:
                        break
                m[origin[0]][origin[1]] = "."
                m[iTmp + 1][j] = "O"
                net += len(m) - iTmp - 1
            j += 1
        i += 1
    return net


def main(filename):
    m = parseInformation(filename)
    net = moveRocks(m)
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
        performTests(2023, 14, [136], main)
    else:
        ans = getAnswer(2023, 14, main)
        print("The sum of possible arrangements is: {0}".format(ans))
