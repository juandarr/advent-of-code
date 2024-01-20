import ast
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    pairs = []
    pair = []
    for row in tmp:
        if row == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(ast.literal_eval(row))
    pairs.append(pair)
    return pairs


# If pair in right order return 1, not conclusive 0, wrong order -1
def comparePair(pair):
    left = pair[0]
    right = pair[1]
    i = 0
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(right, list) and isinstance(left, int):
        left = [left]
    while i < len(left) and i < len(right):
        lt = left[i]
        rt = right[i]
        if isinstance(lt, int) and isinstance(rt, int):
            if lt < rt:
                return 1
            elif lt > rt:
                return -1
        else:
            if isinstance(lt, list) and isinstance(rt, int):
                rt = [rt]
            elif isinstance(rt, list) and isinstance(lt, int):
                lt = [lt]
            out = comparePair([lt, rt])
            if out in [1, -1]:
                return out
        i += 1
    if i == len(left) and i < len(right):
        return 1
    elif i == len(right) and i < len(left):
        return -1


def rightOrderChecker(pairs):
    rightOrder = 0
    for idx, pair in enumerate(pairs):
        out = comparePair(pair)
        if out == 1:
            rightOrder += idx + 1
    return rightOrder


def main(filename):
    pairs = parseInformation(filename)
    packets = rightOrderChecker(pairs)
    return packets


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(13, [13], main)
    else:
        ans = getAnswer(13, main)
        print("The sum of indices of packets in the right order is {0}".format(ans))
