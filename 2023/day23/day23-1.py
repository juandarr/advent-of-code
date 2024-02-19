import heapq
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

sys.setrecursionlimit(10000)


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m


def createGraph(origin, m, graph):
    endPoints = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    cur = origin
    cost = 0
    visited = {origin: 1}
    while True:
        path = []
        for dir in endPoints:
            d = endPoints[dir]
            i = cur[0] + d[0]
            j = cur[1] + d[1]
            if m[i][j] == "#" or (i, j) in visited:
                continue
            elif m[i][j] in endPoints:
                if endPoints[m[i][j]] == (-1 * d[0], -1 * d[1]):
                    continue
            path.append((i, j))
        cost += 1
        if len(path) > 1 or m[path[0][0]][path[0][1]] in endPoints:
            break
        cur = path[0]
        visited[cur] = 1
        if cur[0] == len(m) - 1:
            break
    if len(path) == 1:
        cur = path[0]
        if cur[0] == len(m) - 1:
            if origin in graph:
                graph[origin][cur] = -cost
            else:
                graph[origin] = {cur: -cost}
            return
        elif m[cur[0]][cur[1]] in endPoints:
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            cost += 1
            if origin in graph:
                graph[origin][(i, j)] = -cost
            else:
                graph[origin] = {(i, j): -cost}
            createGraph((i, j), m, graph)
    else:
        cost += 1
        for p in path:
            cur = p
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            if origin in graph:
                graph[origin][(i, j)] = -cost
            else:
                graph[origin] = {(i, j): -cost}
            createGraph((i, j), m, graph)


def shortestPath(graph, m, origin):
    toExplore = []
    heapq.heappush(toExplore, (0, origin))
    visited = {}
    cost = {}
    for node in graph:
        cost[node] = float("inf")
    cost[origin] = 0
    cost[(len(m) - 1, len(m[0]) - 2)] = float("inf")
    while toExplore:
        tmp = heapq.heappop(toExplore)
        curCost = tmp[0]
        curNode = tmp[1]
        # if curNode==(len(m)-1,len(m[0])-2):
        #     break
        visited[curNode] = 1
        for node in graph[curNode]:
            c = graph[curNode][node]
            newCost = curCost + c
            if cost[node] > newCost:
                cost[node] = newCost
            if node != (len(m) - 1, len(m[0]) - 2):
                heapq.heappush(toExplore, (cost[node], node))
    return cost


def main(filename):
    m = parseInformation(filename)
    origin = (0, 1)
    end = (len(m) - 1, len(m[0]) - 2)
    graph = {}
    createGraph(origin, m, graph)
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
        performTests(2023, 23, [94], main)
    else:
        ans = getAnswer(2023, 23, main)
        print("The longest hike is: {0} steps long".format(ans))
