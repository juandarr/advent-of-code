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
        cost -=1
        if len(path)>1 or m[path[0][0]][path[0][1]] in endPoints:
            break
        cur = path[0]
        visited[cur]=1
        if cur[0]==len(m)-1:
            break
    if len(path)==1:
        cur = path[0]
        if cur[0]==len(m)-1:
            nodes[origin]=[[cur,cost]]
            return 
        elif m[cur[0]][cur[1]] in endPoints:
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            cost-=1
            nodes[origin]=[[(i,j),cost]]
            createGraph((i,j),m,graph)
    else:
        cost -=1
        for p in path:
            cur = p
            i = cur[0] + endPoints[m[cur[0]][cur[1]]][0]
            j = cur[1] + endPoints[m[cur[0]][cur[1]]][1]
            if origin in nodes:
                nodes[origin].append([(i,j),cost])
            else:
                nodes[origin]=[[(i,j),cost]]
            createGraph((i,j),m,graph)

def shortestPath(m,origin):
    toExplore = []
    heapq.heappush(toExplore, (0,origin))
    visited = {}
    cost = []
    dirs = {'n':(-1,0), 's':(1,0), 'w': (0,-1), 'e':(0,1)}
    pathAllowed = {'.':1, '>':(0,1),'<':(0,-1),'^':(-1,0), 'v':(1,0)}
    for i in range(len(m)):
        tmp = []
        for j in range(len(m[0])):
            tmp.append(float('inf'))
        cost.append(tmp)
    cost[0][1] = 0
    while toExplore:
        tmp = heapq.heappop(toExplore)
        curCost = tmp[0]
        curNode = tmp[1]
        visited[curNode] = 1
        if m[curNode[0]][curNode[1]] == '.':
            for dir in dirs:
                d = dirs[dir]
                i = curNode[0]+d[0]
                j = curNode[1]+d[1]
                if i<0 or i>len(m)-1:
                    continue
                if j<0 or j>len(m[0])-1:
                    continue
                if m[i][j] in pathAllowed:
                    c = curCost-1
                    if cost[i][j]>c:
                        cost[i][j] = c
                    if (i,j) not in visited:
                        heapq.heappush(toExplore,(cost[i][j], (i,j)))
        else:
            d = pathAllowed[m[curNode[0]][curNode[1]]]
            i = curNode[0]+d[0]
            j = curNode[1]+d[1]
            if i<0 or i>len(m)-1:
                continue
            if j<0 or j>len(m[0])-1:
                continue

            if m[i][j] in pathAllowed:
                c = curCost-1
                if cost[i][j]>c:
                    cost[i][j] = c
                if (i,j) not in visited:
                    heapq.heappush(toExplore,(cost[i][j], (i,j)))
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
    # p = shortestPath(m,(0,1))
    graph= {}
    createGraph((0,1),m,graph)
    # Graph is in format: source:[[dest1, cost1], [dest2, cost2],...]
    print(len(graph))
    endPoints = {'>':(0,1),'<':(0,-1),'^':(-1,0), 'v':(1,0)}
    ed =set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] in endPoints:
                ed.add((i+endPoints[m[i][j]][0], j+endPoints[m[i][j]][1]))
    print(len(ed)+1)
