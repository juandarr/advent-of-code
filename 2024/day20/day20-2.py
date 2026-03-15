from os.path import dirname, abspath
import sys
import heapq

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    data = {}
    data['map']= []
    for row in rows:
        data['map'].append(list(row))
    gotS = False
    gotE = False
    data['start'] = []
    data['target'] = []
    for i in range(len(data['map'])):
        for j in range(len(data['map'][0])):
            if data['map'][i][j]=='S':
                data['start']=(i,j)
                gotS = True
                continue
            elif data['map'][i][j]=='E':
                data['target']=(i,j)
                gotE = True
                continue
        if gotS and gotE:
            break
    return data

def shortestPath(params):
    start = params['start']
    target = params['target']
    grid_map = params['map']

    dirs = [(1,0),(-1,0), (0,-1), (0,1)] 
    toExpand = [(0,start)]
    distance = {start: 0}
    mini = float('inf')
    while toExpand:
        curCost, curNode = heapq.heappop(toExpand)
        for d in dirs:
            newNode = (curNode[0]+d[0], curNode[1]+d[1])
            cost = 1
            if  grid_map[newNode[0]][newNode[1]]=='#':
                continue
            newTotalCost= curCost+cost
            prevBest = distance.get(newNode, float('inf'))
            if  prevBest>newTotalCost:
                distance[newNode] = newTotalCost
                if newNode == target:
                    if mini>newTotalCost:
                        mini = newTotalCost
                heapq.heappush(toExpand,(newTotalCost,newNode)) 
    total = 0
    visited = set()
    saves = {}
    for node1 in distance:
        visited.add(node1)
        for node2 in distance:
            if node2 not in visited:
                cheat = abs(node1[0]-node2[0])+abs(node1[1]-node2[1])
                if cheat<=20:
                    if distance[node1]<distance[node2]:
                        tmp = distance[node2]-distance[node1]-cheat
                        #tmp>=50 in test case
                        if tmp>=100:
                            total +=1
                        if tmp in saves:
                            saves[tmp] += 1
                        else:
                            saves[tmp]=1
    return total

def main(filename):
    params = parseInformation(filename)
    shortest= shortestPath(params)
    return shortest

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 20, [285],main) 
    else:
        score = getAnswer(2024, 20, main)
        print("The shortest path is: {0}".format(score))