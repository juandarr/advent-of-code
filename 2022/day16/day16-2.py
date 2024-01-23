from os.path import dirname, abspath
import sys
import re
import copy

sys.path.insert(0, dirname(dirname(abspath(__file__))))
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
    graph = {}
    for connection in connections:
        connection = connection.strip()
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
    totalTime = 26
    initialState = {"graph": copy.deepcopy(graph)}
    initialState["release"] = 0
    toExpand = [[("AA", 0, "AA", 0), initialState]]
    idx = 0
    highest = 0
    highestInTime = {}
    path = {}
    while idx < len(toExpand):
        (currentNode1, time1, currentNode2, time2), currentState = toExpand[idx]
        if currentNode1 not in path:
            path[currentNode1] = shortestPath(graph, currentNode1)
        if currentNode2 not in path:
            path[currentNode2] = shortestPath(graph, currentNode2)
        highPressureNodes = sorted(
            [
                node
                for node in graph
                if (graph[node]["flow"] > 0 and not currentState["graph"][node]["open"])
            ],
            key=lambda node: graph[node]["flow"],
            reverse=True,
        )
        visited = {}
        for node1 in highPressureNodes:
            # Reach node and open the valve
            tmpTime1 = time1 + path[currentNode1][node1] + 1
            if tmpTime1 > totalTime - 1:
                node1 = currentNode1
                tmpTime1 = time1
                release1 = 0
                visitedNode1 = ""
            else:
                visitedNode1 = node1
                timeLeft1 = totalTime - tmpTime1
                release1 = timeLeft1 * graph[node1]["flow"]
            for node2 in highPressureNodes:
                if node1 == node2:
                    continue
                tmpTime2 = time2 + path[currentNode2][node2] + 1
                if tmpTime2 > totalTime - 1:
                    node2 = currentNode2
                    tmpTime2 = time2
                    release2 = 0
                    visitedNode2 = ""
                else:
                    timeLeft2 = totalTime - tmpTime2
                    release2 = timeLeft2 * graph[node2]["flow"]
                    visitedNode2 = node2
                if (visitedNode1, visitedNode2) in visited:
                    continue
                tmpHighest = release1 + release2 + currentState["release"]
                if tmpHighest > highest:
                    highest = tmpHighest
                visited[(visitedNode1, visitedNode2)] = 1
                if (
                    node1,
                    tmpTime1,
                    node2,
                    tmpTime2,
                ) not in highestInTime or tmpHighest > highestInTime[
                    (node1, tmpTime1, node2, tmpTime2)
                ]:
                    highestInTime[(node1, tmpTime1, node2, tmpTime2)] = tmpHighest
                    tmpState = copy.deepcopy(currentState)
                    tmpState["release"] = tmpHighest
                    if node1 != currentNode1:
                        tmpState["graph"][node1]["open"] = True
                    if node2 != currentNode2:
                        tmpState["graph"][node2]["open"] = True
                    toExpand.append([(node1, tmpTime1, node2, tmpTime2), tmpState])
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
        performTests(16, [1707], main)
    else:
        ans = getAnswer(16, main)
        print("The most pressure that can be released is {0}".format(ans))
