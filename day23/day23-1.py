from time import sleep, time
import heapq
import sys

sys.setrecursionlimit(10000)

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m 

def createGraph(origin,m,graph):
    endPoints = {'>':(0,1),'<':(0,-1),'^':(-1,0), 'v':(1,0)}
    cur = origin
    cost = 0
    visited = {origin:1}
    while True:
        path = []
        for dir in endPoints:
            d = endPoints[dir]
            i = cur[0]+d[0]
            j = cur[1]+d[1]
            if m[i][j]=='#' or (i,j) in visited:
                continue
            elif m[i][j] in endPoints:
                if endPoints[m[i][j]]==(-1*d[0],-1*d[1]):
                    continue
            path.append((i,j))
        cost +=1
        if len(path)>1 or m[path[0][0]][path[0][1]] in endPoints:
            break
        cur = path[0]
        visited[cur]=1
        if cur[0]==len(m)-1:
            break
    if len(path)==1:
        cur = path[0]
        if cur[0]==len(m)-1:
            graph[origin]=[[cur,cost]]
            return 
        elif m[cur[0]][cur[1]] in endPoints:
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            cost+=1
            graph[origin]=[[(i,j),cost]]
            createGraph((i,j),m,graph)
    else:
        cost +=1
        for p in path:
            cur = p
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            if origin in graph:
                graph[origin].append([(i,j),cost])
            else:
                graph[origin]=[[(i,j),cost]]
            createGraph((i,j),m,graph)

def shortestPath(graph,origin):
    toExplore = []
    heapq.heappush(toExplore, (0,origin))
    visited = {}
    cost = {}
    for node in graph:
        cost[node] =float('inf')
    cost[origin] = 0
    cost[(22,21)] = float('inf')
    while toExplore:
        tmp = heapq.heappop(toExplore)
        curCost = tmp[0]
        curNode = tmp[1]
        if curNode==(22,21):
            break
        visited[curNode] = 1
        for pair in graph[curNode]: 
            node = pair[0]
            c = pair[1]
            newCost = curCost+c
            if cost[node]>newCost:
                cost[node] = newCost
            if node not in visited:
                heapq.heappush(toExplore,(newCost, node))
    return cost

if __name__=='__main__': 
    test =True
    testNumber =1 
    '''
    Answers to tests
    1: 94 
    '''
    if test:
        filename = "day23-test{0}-input.txt".format(testNumber)
    else:
        filename = "day23-1-input.txt"
    lines = read_file(filename)
    m = parseInformation(lines)
    print(m)
    origin = (0,1)
    graph= {}
    createGraph(origin,m,graph)
    # Graph is in format: source:[[dest1, cost1], [dest2, cost2],...]
    # print(len(graph))
    # endPoints = {'>':(0,1),'<':(0,-1),'^':(-1,0), 'v':(1,0)}
    # ed =set()
    # for i in range(len(m)):
    #     for j in range(len(m[0])):
    #         if m[i][j] in endPoints:
    #             ed.add((i+endPoints[m[i][j]][0], j+endPoints[m[i][j]][1]))
    p = shortestPath(graph,origin)
    print(p)
