from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    operations = []
    for row in tmp:
        operations.append(list(row.split(" ")))
    return operations


def registerAndClock(instructions):
    register = 1
    cycle = 0
    sumStrenghts = 0
    for instruction in instructions:
        if len(instruction) == 2:
            for _ in range(2):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    sumStrenghts += cycle * register
            register += int(instruction[1])
        elif len(instruction) == 1:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                sumStrenghts += cycle * register
    print(sumStrenghts)
    return sumStrenghts


def main(filename):
    operations = parseInformation(filename)
    sum = registerAndClock(operations)
    return sum


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(10, [13140], main)
    else:
        ans = getAnswer(10, main)
        print("The signal strenght is {0}".format(ans))
