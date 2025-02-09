from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    for idx,row in enumerate(rows):
        tmp = row.split(':')
        rows[idx] = (int(tmp[0]), list(map(lambda n: int(n), tmp[1][1:].split(' '))))
    print(rows)
    return rows

def checkOps(rows):
    return 0

def main(filename):
    rows = parseInformation(filename)
    sumValid = checkOps(rows)
    return sumValid


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 7, [3749], main)
    else:
        total = getAnswer(2024, 7, main)
        print("The total calibration result is: {0}".format(total))