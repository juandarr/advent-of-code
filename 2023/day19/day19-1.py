from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    wf = {}
    parts = []
    c = 0
    while lines[c] != "\n":
        tmp = lines[c].strip().split("{")
        name = tmp[0]
        tmp = tmp[1][:-1]
        tmp = tmp.split(",")
        tmpAr = []
        for i in tmp:
            tmpAr.append(tuple(i.split(":")))
        wf[name] = tmpAr
        c += 1
    c += 1
    for line in lines[c:]:
        tmp = line.strip()[1:-1].split(",")
        tmpAr = {}
        for i in tmp:
            tmp_i = i.split("=")
            tmpAr[tmp_i[0]] = int(tmp_i[1])
        parts.append(tmpAr)
    return wf, parts


def workflows(wf, parts):
    net = 0
    for part in parts:
        cur = "in"
        x = part["x"]
        m = part["m"]
        a = part["a"]
        s = part["s"]
        while cur not in ["A", "R"]:
            default = True
            for rule in wf[cur][:-1]:
                if eval(rule[0]):
                    cur = rule[1]
                    default = False
                    break
            if default:
                cur = wf[cur][-1][0]
        if cur == "A":
            for k in part:
                net += part[k]
    return net


def main(filename):
    wf, parts = parseInformation(filename)
    net = workflows(wf, parts)
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
        performTests(2023, 19, [19114], main)
    else:
        ans = getAnswer(2023, 19, main)
        print("The number of distinct combinations of ratings is: {0}".format(ans))
