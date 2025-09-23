from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    data = values.rstrip()
    return data


def countFloors(data):
    counter = 0
    for dir in data:
        if dir=='(':
            counter += 1
        elif dir==')':
            counter -=1
    return counter


def main(filename):
    l = parseInformation(filename)
    count = countFloors(l)
    return count


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 1, [3, -3, -1], main)
    else:
        total = getAnswer(2015, 1, main)
        print("Santa is in floor {0} after following the instructions".format(total))