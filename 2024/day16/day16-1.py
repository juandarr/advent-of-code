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

    toExpand = [(0,start, (0,1))]
    distance = {(start, (0,1)): 0}

    mini = float('inf')
    while toExpand:
        curCost, curNode, curDir = heapq.heappop(toExpand)
        if curNode==target:
            return mini
        dirs = [curDir, (-curDir[1], -curDir[0]), (curDir[1], curDir[0])] 
        for idx,d in enumerate(dirs):
            newNode = (curNode[0]+d[0], curNode[1]+d[1])
            if  grid_map[newNode[0]][newNode[1]]=='#':
                continue
            cost = 1 if idx==0 else 1001
            newTotalCost= curCost+cost
            prevBest = distance.get((newNode,d), float('inf'))
            if  prevBest>newTotalCost:
                distance[(newNode,d)] = newTotalCost
                if newNode == target:
                    if mini>newTotalCost:
                        mini = newTotalCost
                heapq.heappush(toExpand,(newTotalCost,newNode,d)) 
    return mini

def main(filename):
    params = parseInformation(filename)
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
        performTests(2024, 16, [7036, 11048],main) 
    else:
        score = getAnswer(2024, 16, main)
        print("The lowest score in the map is: {0}".format(score))