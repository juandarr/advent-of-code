from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    patterns = []
    tmp = []
    # Read lines and expand by rows
    for line in lines:
        if line.strip() == "":
            patterns.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip())
    patterns.append(tmp)
    return patterns


def findMirror(pattern):
    i = 0
    mirrorFound = False
    mirrors = {}
    lines = []
    while i < len(pattern) - 1:
        e = len(pattern) - 1
        while e > i:
            if pattern[i] == pattern[e] and (i == 0 or e == len(pattern) - 1):
                iTmp = i
                eTmp = e
                while pattern[iTmp] == pattern[eTmp]:
                    if (eTmp - iTmp) == 1:
                        lines.append(iTmp)
                        mirrorFound = True
                        break
                    else:
                        lines.append(iTmp)
                    iTmp += 1
                    eTmp -= 1
            if mirrorFound:
                break
            e -= 1
        if mirrorFound:
            break
        i += 1
    if mirrorFound:
        mirrors["h"] = lines[-1] + 1
    j = 0
    mirrorFound = False
    cols = []
    while j < len(pattern[0]) - 1:
        e = len(pattern[0]) - 1
        while e > j:
            colJ = "".join([pattern[i][j] for i in range(len(pattern))])
            colE = "".join([pattern[i][e] for i in range(len(pattern))])
            if colJ == colE and (j == 0 or e == len(pattern[0]) - 1):
                jTmp = j
                eTmp = e
                while colJ == colE:
                    if (eTmp - jTmp) == 1:
                        cols.append(jTmp)
                        mirrorFound = True
                        break
                    else:
                        cols.append(jTmp)
                    jTmp += 1
                    eTmp -= 1
                    if jTmp - eTmp == 0:
                        break
                    colJ = "".join([pattern[i][jTmp] for i in range(len(pattern))])
                    colE = "".join([pattern[i][eTmp] for i in range(len(pattern))])
            if mirrorFound:
                break
            e -= 1
        if mirrorFound:
            break
        j += 1
    if mirrorFound:
        mirrors["v"] = cols[-1] + 1
    return mirrors


def summarizeNotes(patterns):
    net = 0
    for pattern in patterns:
        mirrors = findMirror(pattern)
        max = ["x", -float("inf")]
        for m in mirrors:
            if mirrors[m] > max[1]:
                max = [m, mirrors[m]]
        if max[0] == "v":
            net += max[1]
        else:
            net += 100 * max[1]
    return net


def main(filename):
    patterns = parseInformation(filename)
    net = summarizeNotes(patterns)
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
        performTests(2023, 13, [405], main)
    else:
        ans = getAnswer(2023, 13, main)
        print("The sum of possible arrangements is: {0}".format(ans))
