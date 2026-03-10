from os.path import dirname, abspath
import sys
import time
import heapq

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    data: dict[str, list | tuple ] = {'map':[], 'start':[], 'target':[]}
    for row in rows:
        data['map'].append(list(row))
    gotS = False
    gotE = False
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

def printMap(map):
    for row in map:
        print(''.join(row))
    print('\n')

def shortestPath(params):
    start = params['start']
    target:tuple[int] = params['target']
    map = params['map']
    Possibledirs = [(-1,0),(1,0), (0,1), (0,-1)]
    expanded: dict[tuple[int,int], int] = {start:0}
    for d in Possibledirs:
        newPos = (start[0]+d[0], start[1]+d[1])
        if map[newPos[0]][newPos[1]]!='#':
            toExpand: list[tuple[int, tuple[int, int],tuple[int, int], list[tuple[int,int]]]] = [(1,newPos,d,[start,newPos])]
            expanded[newPos] = 1
    mini  = float('inf')
    while True:
        curNode:tuple[int, tuple[int,int],tuple[int,int], list[tuple[int,int]]] = heapq.heappop(toExpand)
        if curNode[1]==target:
            break
        #print(curNode)
        time.sleep(1)
        dirs = [curNode[2], (-1*curNode[2][1], -1*curNode[2][0]), (curNode[2][1], curNode[2][0])] 
        for idx,d in enumerate(dirs):
            newNode = (curNode[1][0]+d[0], curNode[1][1]+d[1])
            if  map[newNode[0]][newNode[1]]=='#' or newNode in curNode[3]:
                continue
            if idx==0:
                cost = 1
            else:
                cost = 1001 
            newPath = list(curNode[3])+[(newNode)]
            print(newPath)
            if newNode in expanded:
                if expanded[newNode]>curNode[0]+cost:
                    expanded[newNode ] = curNode[0]+cost
                    print(expanded)
                    toExpand.append((expanded[newNode],newNode,d,newPath)) 
            else:
                expanded[newNode] = curNode[0]+cost
                toExpand.append((expanded[newNode],newNode,d,newPath)) 
        heapq.heapify(toExpand)
        if target in expanded:
            if mini > expanded[target]:
                print(expanded[target])
                mini = expanded[target]
                time.sleep(1)
        print('toexpand: ',toExpand)
        if len(toExpand)==0:
            break
    print(expanded)
    return expanded[target]

def main(filename):
    params = parseInformation(filename)
    printMap(params['map'])
    lowestScore= shortestPath(params)
    return lowestScore

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 16, [7036],main)#10092 
    else:
        score = getAnswer(2024, 16, main)
        print("The lowest score in the map is: {0}".format(score))