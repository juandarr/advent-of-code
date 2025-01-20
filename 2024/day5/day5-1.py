from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    data = [[],[]]
    idx = 0
    for row in rows:
        if row=='':
            idx+=1
            continue
        if idx==0:
            data[idx].append(list(map(int,row.split('|'))))
        else:
            data[idx].append(list(map(int, row.split(','))))
    return data

def checkUpdates(updates, rules):
    return 0


def main(filename):
    updates, rules = parseInformation(filename)
    print(updates, rules)
    total = checkUpdates(updates,rules)
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
        performTests(2024, 5, [143], main)
    else:
        total = getAnswer(2024, 5, main)
        print("The sum of middle values of correctly-ordered updates is: {0}".format(total))