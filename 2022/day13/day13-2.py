import ast
from functools import cmp_to_key
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")

    packets = [[[2]], [[6]]]
    for packet in tmp:
        if packet == "":
            continue
        packets.append(ast.literal_eval(packet))
    return packets


# If pair in right order return 1, not conclusive 0, wrong order -1
def comparePair(left, right) -> int:
    i = 0
    out = 0
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
            out = comparePair(lt, rt)
            if out in [1, -1]:
                return out
        i += 1
    if i == len(left) and i < len(right):
        out = 1
    elif i == len(right) and i < len(left):
        out = -1
    return out


def decoderKeyExtractor(packets):
    packetList = sorted(packets, key=cmp_to_key(comparePair), reverse=True)  # noqa
    decoderKey = (packetList.index([[2]]) + 1) * (packetList.index([[6]]) + 1)
    return decoderKey


def main(filename):
    packets = parseInformation(filename)
    decoderKey = decoderKeyExtractor(packets)
    return decoderKey


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(13, [140], main)
    else:
        ans = getAnswer(13, main)
        print("The decoder key is {0}".format(ans))
