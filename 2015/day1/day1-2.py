from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    data = values.rstrip()
    return data


def findPosition(data):
    counter = 0
    position = 1
    for dir in data:
        if dir=='(':
            counter += 1
        elif dir==')':
            counter -=1
            if counter == -1:
                return position
        position += 1
    return 0


def main(filename):
    l = parseInformation(filename)
    position = findPosition(l)
    return position


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 1, [0, 1, 1], main)
    else:
        position = getAnswer(2015, 1, main)
        print("The character position where Santa goes to basement is {0}".format(position))