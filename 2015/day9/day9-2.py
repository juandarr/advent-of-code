from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    routesRaw = [row.split(' = ') for row in data.rstrip().split('\n')]
    routes = [(row[0].split(' to '), int(row[-1])) for row in routesRaw]
    return routes


def shortestDistance(routes):
    paths = {}
    nodes = set()
    d = -float('inf')
    for route in routes:
        if route[0][0] in paths:
            paths[route[0][0]].append((route[0][1], route[1]))
        else:
            paths[route[0][0]]= [(route[0][1], route[1])]
        if route[0][1] in paths:
            paths[route[0][1]].append((route[0][0], route[1]))
        else:
            paths[route[0][1]]= [(route[0][0], route[1])]
        nodes.add(route[0][0])
        nodes.add(route[0][1])
    for start in nodes:
        toExpand = [([start],{start:1}, 0)]
        while len(toExpand)>0:
            cur = toExpand.pop()
            if len(cur[0])==len(nodes):
                if d<cur[2]:
                    d = cur[2]
                continue
            if cur[0][-1] in paths:
                for p in paths[cur[0][-1]]:
                    if p[0] not in cur[1]:
                        s = cur[1].copy()
                        s[p[0]]=1
                        toExpand.append((cur[0]+[p[0]], s , cur[2]+p[1]))
                    else:
                        continue
            else:
                continue
    return d 

def main(filename):
    routes = parseInformation(filename)
    d = shortestDistance(routes)
    return d

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 9, [982], main, test=["1"])
    else:
        d = getAnswer(2015, 9, main)
        print("The longest travel distane visiting every node at least once is {0}".format(d))