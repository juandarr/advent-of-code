import heapq
from copy import deepcopy
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

sys.setrecursionlimit(100000)


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m


def isNode(node, m):
    endPoints = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    i = node[0]
    j = node[1]
    isNode = True
    for d in endPoints:
        newI = i + endPoints[d][0]
        newJ = j + endPoints[d][1]
        if newI < 0 or newI >= len(m) or newJ < 0 or newJ >= len(m[0]):
            continue
        if m[newI][newJ] == ".":
            isNode = False
            break
    return isNode


def createGraph(origin, aim, m, graph):
    endPoints = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    cur = (origin[0] + endPoints[aim][0], origin[1] + endPoints[aim][1])
    cost = 1
    visited = {origin: 1, cur: 1}
    while True:
        path = []
        if cur == (0, 1):
            return
        for dir in endPoints:
            d = endPoints[dir]
            i = cur[0] + d[0]
            j = cur[1] + d[1]
            if m[i][j] == "#" or (i, j) in visited:
                continue
            path.append((i, j))
        cost += 1
        cur = path[0]
        visited[cur] = 1
        if cur[0] == len(m) - 1 or isNode(cur, m):
            break
    cur = path[0]
    if origin in graph:
        if cur in graph[origin]:
            return
        else:
            graph[origin][cur] = -cost
    else:
        graph[origin] = {cur: -cost}
    if cur[0] == len(m) - 1:
        return
    else:
        path = []
        for dir in endPoints:
            d = endPoints[dir]
            i = cur[0] + d[0]
            j = cur[1] + d[1]
            if m[i][j] == "#" or (i, j) in visited:
                continue
            path.append((cur, dir))
        for p in path:
            createGraph(p[0], p[1], m, graph)


def shortestPath(graph, m, origin):
    toExplore = []
    heapq.heappush(toExplore, (0, origin, {}))
    cost = {}
    for node in graph:
        cost[node] = float("inf")
    cost[origin] = 0
    cost[(len(m) - 1, len(m[0]) - 2)] = float("inf")
    while toExplore:
        tmp = heapq.heappop(toExplore)
        curCost = tmp[0]
        curNode = tmp[1]
        visited = deepcopy(tmp[2])
        visited[curNode] = 1
        for node in graph[curNode]:
            c = graph[curNode][node]
            if node in visited:
                continue
            newCost = curCost + c
            if cost[node] > newCost:
                cost[node] = newCost
            if node != (len(m) - 1, len(m[0]) - 2):
                heapq.heappush(toExplore, (newCost, node, visited))
    return cost


def main(filename):
    m = parseInformation(filename)
    origin = (0, 1)
    end = (len(m) - 1, len(m[0]) - 2)
    graph = {}
    createGraph(origin, "v", m, graph)
    p = shortestPath(graph, m, origin)
    return p[end] * -1


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 23, [154], main)
    else:
        ans = getAnswer(2023, 23, main)
        print("The longest hike is: {0} steps long".format(ans))
