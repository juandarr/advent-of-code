from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    steps = []
    for line in lines:
        if line.strip() != "":
            steps = list(line.strip().split(","))
    return steps


def hash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def focusingPower(steps):
    boxes = {}
    for step in steps:
        tmp = step.split("=")
        if len(tmp) == 2:
            inBox = False
            val = hash(tmp[0])
            if val in boxes:
                for idx, i in enumerate(boxes[val]):
                    if i[0] == tmp[0]:
                        inBox = True
                        boxes[val][idx][1] = tmp[1]
                        break
                if not (inBox):
                    boxes[val].append(tmp)
            else:
                boxes[val] = [tmp]
        else:
            tmp = tmp[0].split("-")
            val = hash(tmp[0])
            if val in boxes:
                for idx, i in enumerate(boxes[val]):
                    if i[0] == tmp[0]:
                        del boxes[val][idx]
                        if len(boxes[val]) == 0:
                            del boxes[val]
                        break
    net = 0
    for val in boxes:
        for idx, i in enumerate(boxes[val]):
            net += (1 + val) * (idx + 1) * int(i[1])
    return net


def main(filename):
    steps = parseInformation(filename)
    net = focusingPower(steps)
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
        performTests(2023, 15, [145], main)
    else:
        ans = getAnswer(2023, 15, main)
        print("The focusing power is: {0}".format(ans))
