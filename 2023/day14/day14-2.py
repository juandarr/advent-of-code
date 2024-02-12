from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    m = []
    # Read lines and expand by rows
    for line in lines:
        m.append(list(line.strip()))
    return m


def limit(i, iLim):
    if iLim == 0:
        return i >= iLim
    else:
        return i < iLim


def moveRocks(m, d):
    net = 0
    dirs = {"n": [-1, 0], "s": [1, 0], "e": [0, 1], "w": [0, -1]}
    dir = dirs[d]
    if d in ["n", "s"]:
        if d == "n":
            i = 0
            iLim = len(m)
        else:
            i = len(m) - 1
            iLim = 0
        inc = -1 * dir[0]
        while limit(i, iLim):
            j = 0
            while j < len(m[i]):
                if m[i][j] == "O":
                    iTmp = i
                    origin = [i, j]
                    iTmp += dir[0]
                    if iTmp < 0 or iTmp > len(m) - 1:
                        j += 1
                        net += len(m) - origin[0]
                        continue
                    while m[iTmp][j] not in ["#", "O"]:
                        iTmp += dir[0]
                        if iTmp < 0 or iTmp > len(m) - 1:
                            break
                    m[origin[0]][origin[1]] = "."
                    m[iTmp + inc][j] = "O"
                    net += len(m) - iTmp - inc
                j += 1
            i += inc
    elif d in ["w", "e"]:
        if d == "w":
            j = 0
            jLim = len(m[j])
        else:
            j = len(m) - 1
            jLim = 0
        inc = -1 * dir[1]
        while limit(j, jLim):
            i = 0
            while i < len(m):
                if m[i][j] == "O":
                    jTmp = j
                    origin = [i, j]
                    jTmp += dir[1]
                    if jTmp < 0 or jTmp > len(m[0]) - 1:
                        i += 1
                        net += len(m[0]) - origin[0]
                        continue
                    while m[i][jTmp] not in ["#", "O"]:
                        jTmp += dir[1]
                        if jTmp < 0 or jTmp > len(m[0]) - 1:
                            break
                    m[origin[0]][origin[1]] = "."
                    m[i][jTmp + inc] = "O"
                    net += len(m[0]) - i
                i += 1
            j += inc
    return net, m


def totalLoad(m):
    cycles = 1000000000
    mem = {}
    net = 0
    for idx, line in enumerate(m):
        for jdx, e in enumerate(line):
            if e == "O":
                net += len(m) - idx
    s = ""
    for i in m:
        s += "".join(i)
    mem[s] = [0, net]
    loop = 0
    cycle = 0
    for cycle in range(cycles):
        moves = ["n", "w", "s", "e"]
        for d in moves:
            net, m = moveRocks(m, d)
        s = ""
        for i in m:
            s += "".join(i)
        if s in mem:
            loop = mem[s][0]
            break
        else:
            mem[s] = [cycle + 1, net]
    cycles -= loop
    loop = cycle + 1 - loop
    for s in range(cycles % loop):
        moves = ["n", "w", "s", "e"]
        for d in moves:
            net, m = moveRocks(m, d)
    return net


def main(filename):
    m = parseInformation(filename)
    net = totalLoad(m)
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
        performTests(2023, 14, [64], main)
    else:
        ans = getAnswer(2023, 14, main)
        print("The sum of possible arrangements is: {0}".format(ans))
