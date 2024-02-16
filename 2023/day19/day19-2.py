from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    wf = {}
    c = 0
    while lines[c] != "\n":
        tmp = lines[c].strip().split("{")
        name = tmp[0]
        tmp = tmp[1][:-1]
        tmp = tmp.split(",")
        tmpAr = []
        r = []
        for i in tmp[:-1]:
            iTmp = i.split(":")
            node = iTmp[0][0]
            if len(iTmp[0].split(">")) > 1:
                r = [int(iTmp[0].split(">")[1]) + 1, 4000]
            elif len(iTmp[0].split("<")) > 1:
                r = [1, int(iTmp[0].split("<")[1]) - 1]
            tmpAr.append(((node, r), iTmp[1]))
        tmpAr.append((tmp[-1],))
        wf[name] = tmpAr
        c += 1
    return wf


def exploreWorkflows(wfs, wf, ranges, nodes):
    if wf in ["R", "A"]:
        if wf == "A":
            c = 1
            for r in ranges:
                c *= r[1] - r[0] + 1
            return c
        return 0
    rules = wfs[wf]
    net = 0
    for rule in rules:
        if len(rule) > 1:
            node = nodes[rule[0][0]]
            r = rule[0][1]
            n = rule[1]
            include = ranges[node].copy()
            exclude = ranges[node].copy()
            if r[0] > ranges[node][0]:
                include[0] = r[0]
                exclude[1] = r[0] - 1
            if r[1] < ranges[node][1]:
                include[1] = r[1]
                exclude[0] = r[1] + 1
            ranges[node] = include
            net += exploreWorkflows(wfs, n, ranges.copy(), nodes)
            ranges[node] = exclude
        else:
            n = rule[0]
            net += exploreWorkflows(wfs, n, ranges.copy(), nodes)
    return net


def main(filename):
    wfs = parseInformation(filename)
    nodes = {"x": 0, "m": 1, "a": 2, "s": 3}
    possibilities = exploreWorkflows(
        wfs, "in", [[1, 4000], [1, 4000], [1, 4000], [1, 4000]], nodes
    )
    return possibilities


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 19, [167409079868000], main)
    else:
        ans = getAnswer(2023, 19, main)
        print("The number of distinct combinations of ratings is: {0}".format(ans))
