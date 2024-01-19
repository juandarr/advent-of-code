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
    sprite = range(register - 1, register + 2)
    cycle = 0
    display = list("." * 240)
    for instruction in instructions:
        if len(instruction) == 2:
            for _ in range(2):
                cycle += 1

                crt = (cycle - 1) % 40
                pixel = (cycle - 1) % 240
                if crt in sprite:
                    display[pixel] = "#"
                else:
                    display[pixel] = "."
            register += int(instruction[1])
            sprite = range(register - 1, register + 2)
        elif len(instruction) == 1:
            cycle += 1

            crt = (cycle - 1) % 40
            pixel = (cycle - 1) % 240
            if crt in sprite:
                display[pixel] = "#"
            else:
                display[pixel] = "."
    output = []
    for i in range(6):
        tmp = ""
        for j in range(40):
            tmp += display[40 * i + j]
        output.append(tmp)
    out = "\n".join(output)
    return out


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
        performTests(
            10,
            [
                """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
            ],
            main,
        )
    else:
        ans = getAnswer(10, main)
        print(ans)
