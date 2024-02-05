from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def read_file(filename):
    return open(filename, "r")


def parseInformation(line, limit):
    tmp = line.split(":")
    game = int(tmp[0].split(" ")[1])
    sets = tmp[1].strip().split(";")
    valid = True
    for s in sets:
        balls = s.strip().split(",")
        for ball in balls:
            tmp = ball.strip().split(" ")
            if limit[tmp[1]] < int(tmp[0]):
                valid = False
                return (valid, game)
    return (valid, game)


def IDsum(filename):
    lines = read_file(filename)
    limit = {"red": 12, "green": 13, "blue": 14}
    net = 0
    for line in lines:
        (validGroup, game) = parseInformation(line, limit)
        if validGroup:
            net += game
    return net


def main(filename):
    net = IDsum(filename)
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
        performTests(2023, 2, [8], main)
    else:
        biggest = getAnswer(2023, 2, main)
        print("The sum of values is: {0}".format(biggest))
