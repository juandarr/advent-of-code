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
    data['bytes']= []
    data['dim']=None
    r = 0
    for row in rows:
        if row=='':
            r +=1
            continue
        tmp = row.split(',')
        if r>=1:
            data['dim']=int(tmp[0])
            data['steps']=int(tmp[1])
            r += 1
        else:
            data['bytes'].append([int(i) for i in tmp])
    return data['bytes'], data['dim'], data['steps']

def printMap(dim,m):
    for i in range(dim):
        row = ''
        for j in range(dim):
            if (i,j) in m:
                row+='#'
            else:
                row+='.'
        print(row)

def isOutside(newNode,dim):
    i = newNode[0]
    j = newNode[1]
    return (i<0 or i>= dim) or (j<0 or j>= dim)

def shortestPath(b,dim,steps):
    m = {}
    for idx in range(steps):
        i = b[idx][1]
        j = b[idx][0]
        m[(i,j)]= 1
    
    start = (0,0)
    target  = (dim-1, dim-1)

    distances:dict[tuple[int,int],int] = {start:0}
    toExpand: list[tuple[int, tuple[int,int]]] = [(0,start)]

    dirs = [(-1,0),(1,0),(0,-1), (0,1)]

    mini = float('inf')
    while toExpand:
        curCost, curNode = heapq.heappop(toExpand)
        if curNode==target:
            break
        for d in dirs:
            newNode = (curNode[0]+d[0], curNode[1]+d[1])
            if newNode in m or isOutside(newNode,dim):
                continue
            newCost = curCost+1
            prevCost = distances.get(newNode, float('inf'))
            if prevCost>newCost:
                distances[newNode] = newCost
                heapq.heappush(toExpand,(newCost, newNode))
                if newNode ==target:
                    if mini>newCost:
                        mini = newCost
    return mini

def main(filename):
    b,dim,steps = parseInformation(filename)
    out= shortestPath(b,dim,steps)
    return out

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 18, [22],main) 
    else:
        out = getAnswer(2024, 18, main)
        print("The shortest path after simulation is: {0}".format(out))