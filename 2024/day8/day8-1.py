from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    m = []
    for row in rows:
        m.append(list(row))
    print(m)
    return m

def checkRow():
   pass

def main(filename):
    m= parseInformation(filename)
    points= checkRow()
    return points


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 8, [0],main)
    else:
        total = getAnswer(2024, 8, main)
        print("The result is: {0}".format(total))