from os.path import dirname, abspath
import sys
import re
import copy

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    connections = []
    for row in tmp:
        connections.append(row)
    return connections


def valveGraph(connections):
    """A function to read the valve
    graph"""
    graph = {}
    for connection in connections:
        valves = re.findall("[A-Z]{2}", connection)
        flow = re.findall("[0-9]+", connection)
        graph[valves[0]] = {
            "connectedTo": valves[1:],
            "flow": int(flow[0]),
            "open": (True if (flow[0] == "0") else False),
        }
    return graph


def shortestPath(graph, src):
    toExpand = [src]
    distances = {}
    for i in graph:
        distances[i] = float("inf")
    distances[src] = 0
    while toExpand:
        curNode = toExpand.pop()
        for i in graph[curNode]["connectedTo"]:
            if distances[i] > distances[curNode] + 1:
                distances[i] = distances[curNode] + 1
                toExpand.insert(0, i)
    return distances


def traverseGraph(graph):
    totalTime = 30
    initialState = {"graph": copy.deepcopy(graph)}
    initialState["time"] = 0
    initialState["release"] = 0
    toExpand = [["AA", initialState]]
    idx = 0
    highest = 0
    highestInTime = {}
    path = {}
    for i in range(30):
        highestInTime[i] = 0
    while idx < len(toExpand):
        tmp = toExpand[idx]
        currentNode = tmp[0]
        if currentNode not in path:
            path[currentNode] = shortestPath(graph, currentNode)
        currentState = tmp[1]
        highPressureNodes = sorted(
            [
                node
                for node in graph
                if (graph[node]["flow"] > 0 and not currentState["graph"][node]["open"])
            ],
            key=lambda node: graph[node]["flow"],
        )
        for node in highPressureNodes:
            # Reach node and open the valve
            tmpTime = currentState["time"] + path[currentNode][node] + 1
            if tmpTime > totalTime - 1:
                continue
            timeLeft = totalTime - tmpTime
            tmpHighest = timeLeft * graph[node]["flow"] + currentState["release"]
            if tmpHighest > highestInTime[tmpTime]:
                if tmpHighest > highest:
                    highest = tmpHighest
                highestInTime[tmpTime] = tmpHighest
                tmpState = copy.deepcopy(currentState)
                tmpState["release"] = tmpHighest
                tmpState["time"] = tmpTime
                tmpState["graph"][node]["open"] = True
                toExpand.append([node, tmpState])
        idx += 1
    return highest


def findMaximumRelease(connections):
    graph = valveGraph(connections)
    highestPressure = traverseGraph(graph)
    return highestPressure


def main(filename):
    connections = parseInformation(filename)
    releasedPressure = findMaximumRelease(connections)
    return releasedPressure


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 16, [1651], main)
    else:
        ans = getAnswer(2022, 16, main)
        print("The most pressure that can be released is {0}".format(ans))
