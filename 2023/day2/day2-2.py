from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def read_file(filename):
    return open(filename, "r")


def parseInformation(line):
    tmp = line.split(":")
    game = int(tmp[0].split(" ")[1])
    sets = tmp[1].strip().split(";")
    values = {"red": 0, "green": 0, "blue": 0}
    for s in sets:
        balls = s.strip().split(",")
        for ball in balls:
            tmp = ball.strip().split(" ")
            if values[tmp[1]] < int(tmp[0]):
                values[tmp[1]] = int(tmp[0])
    return values["red"] * values["blue"] * values["green"]


def sumOfPower(filename):
    lines = read_file(filename)
    power = 0
    for line in lines:
        powerLocal = parseInformation(line)
        power += powerLocal
    return power


def main(filename):
    net = sumOfPower(filename)
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
        performTests(2023, 2, [2286], main)
    else:
        biggest = getAnswer(2023, 2, main)
        print("The sum of powers is: {0}".format(biggest))
