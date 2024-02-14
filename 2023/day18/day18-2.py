from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip().split()))
    return m


def shoelace(groundDug):
    i = len(groundDug) - 2
    total = 0
    while i >= 0:
        total += (
            groundDug[i][0] * groundDug[i - 1][1]
            - groundDug[i][1] * groundDug[i - 1][0]
        )
        i -= 1
        if i == 0:
            total += (
                groundDug[i][0] * groundDug[len(groundDug) - 2][1]
                - groundDug[i][1] * groundDug[len(groundDug) - 2][0]
            )
            break
    return total // 2


def dig(start, m, groundDug):
    # Find the ground edge based on intructions
    groundDug[0] = start
    i, j = start
    dir = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    vToDir = {"0": "R", "1": "D", "2": "L", "3": "U"}
    hexToDec = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    c = 1
    edge = 0
    for instruction in m:
        # Uncomment to solutions to challenge 1
        # d,value,color = instruction
        # d = dir[d]
        # value = int(value)

        # Start: part 2 specific
        _, _, hexValue = instruction
        d = dir[vToDir[hexValue[-2]]]
        hexValue = hexValue[2:-2]
        value = 0
        h = len(hexValue) - 1
        for idx in range(len(hexValue) - 1, -1, -1):
            if hexValue[idx] in hexToDec:
                value += hexToDec[hexValue[idx]] * (16 ** (h - idx))
            else:
                value += int(hexValue[idx]) * (16 ** (h - idx))
        # End: part 2 specific
        i += d[0] * value
        j += d[1] * value
        edge += value
        groundDug[c] = (i, j)
        c += 1
    count = 1
    for g in groundDug:
        if g + 1 in groundDug:
            if groundDug[g][0] == groundDug[g + 1][0]:
                if groundDug[g][1] > groundDug[g + 1][1]:
                    count += groundDug[g][1] - groundDug[g + 1][1]
            elif groundDug[g][1] == groundDug[g + 1][1]:
                if groundDug[g][0] < groundDug[g + 1][0]:
                    count += groundDug[g + 1][0] - groundDug[g][0]
    area = shoelace(groundDug)
    return area + count


def main(filename):
    m = parseInformation(filename)
    ans = dig((0, 0), m, {})
    return ans


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 18, [952408144115], main)
    else:
        ans = getAnswer(2023, 18, main)
        print("The volume of lava that can be held is: {0}".format(ans))
