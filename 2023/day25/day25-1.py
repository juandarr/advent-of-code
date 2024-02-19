import random
from copy import deepcopy
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and extract every position and velocity for each hailstone
    graph = {}
    for line in lines:
        tmp = line.strip().split(":")
        graph[tmp[0]] = list(tmp[1].strip().split())
    # From this list of nodes create graph
    new = {}
    for node in graph:
        for i in graph[node]:
            if i not in graph:
                if i not in new:
                    new[i] = [node]
                else:
                    new[i].append(node)
            else:
                if node not in graph[i]:
                    graph[i].append(node)
    for node in new:
        graph[node] = new[node]

    return graph


def getEdges(graph):
    edges = []
    for node in graph:
        for node2 in graph[node]:
            edges.append((node, node2))
    return edges


def contraction(graph, edge):
    newVertex = "".join(edge)
    nodes = []
    # print('Before: ',graph, edge)
    for e in edge:
        for node in graph[e]:
            if node not in edge:
                nodes.append(node)
    for node in graph:
        if node not in edge:
            if edge[0] in graph[node]:
                indexes = [i for i, x in enumerate(graph[node]) if x == edge[0]]
                for idx in indexes:
                    graph[node][idx] = newVertex
            if edge[1] in graph[node]:
                indexes = [i for i, x in enumerate(graph[node]) if x == edge[1]]
                for idx in indexes:
                    graph[node][idx] = newVertex
    del graph[edge[0]]
    del graph[edge[1]]
    graph[newVertex] = nodes
    # print('After: ',graph, edge)


def kargerAlgorithm(graph):
    # print('Before: \n','Graph: ', graph, '\nEdges: ', edges)
    while len(graph) > 2:
        edges = getEdges(graph)
        random_idx = random.choice(range(len(edges)))
        edge = edges[random_idx]
        # print(random_idx, edge)
        contraction(graph, edge)
        # print('After: \n','Graph: ', graph, '\nEdges: ', edges)
    edges = getEdges(graph)
    # print('After: \n','Graph: ', graph, '\nEdges: ', len(edges))
    if len(edges) == 6:
        net = 1
        for node in graph:
            net *= len(node) // 3
        return net
    return 0


def main(filename):
    graph = parseInformation(filename)
    for i in range(500):
        graph_cp = deepcopy(graph)
        c = kargerAlgorithm(graph_cp)
        if c != 0:
            return c
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 25, [54], main)
    else:
        ans = getAnswer(2023, 25, main)
        print("The product of sizes of the two group division is: {0}".format(ans))
