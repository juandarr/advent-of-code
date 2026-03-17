from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    graph = {}
    for row in rows:
        tmp = row.split('-')
        for idx,node in enumerate(tmp):
            if node in graph:
                graph[node].add(tmp[abs(idx-1)])
            else:
                graph[node] = {tmp[abs(idx-1)]}
    return graph

def checkNetwork(graph):
    totalSets = set()
    for node1 in graph:
        for node2 in graph[node1]:
            for node3 in graph[node2]:
                if not (node1[0]=='t' or node2[0]=='t' or node3[0]=='t'):
                    continue
                if node1 in graph[node3]:
                    tmp = tuple(sorted([node1,node2,node3]))
                    if  tmp not in totalSets:
                        totalSets.add(tmp)
    return len(totalSets)


def main(filename):
    graph = parseInformation(filename)
    triads= checkNetwork(graph)
    return triads

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 23, [7],main) 
    else:
        n = getAnswer(2024, 23, main)
        print("The number of sets of 3 interconnected computers including a node start with t is {0}".format(n))