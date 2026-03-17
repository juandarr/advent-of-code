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

    cheatSet = set()
    exploredCheats = 0
    dirs = [(1,0),(-1,0), (0,-1), (0,1)] 
    save = {}
    ans = 0
    while True:
        toExpand = [(0,start)]
        distance = {start: 0}
        availableCheat = 1
        mini = float('inf')
        tmp = exploredCheats
        tmpCheat = []
        while toExpand:
            curCost, curNode = heapq.heappop(toExpand)
            if curNode==target:
                break
            for d in dirs:
                newNode = (curNode[0]+d[0], curNode[1]+d[1])
                cost = 1
                if  grid_map[newNode[0]][newNode[1]]=='#':
                    if availableCheat==1:
                        cheatNode =(newNode[0]+d[0], newNode[1]+d[1]) 
                        if cheatNode[0]<0 or cheatNode[0]>=len(grid_map) or cheatNode[1]<0 or cheatNode[1]>=len(grid_map[0]): 
                            continue
                    else:
                        continue
                    if grid_map[cheatNode[0]][cheatNode[1]]=='#':
                        continue
                    else:
                        if (curNode, cheatNode) in cheatSet: 
                            continue
                        else:
                            tmpCheat.append((curNode, cheatNode))
                            exploredCheats += 1
                            newNode = cheatNode
                            availableCheat-=1
                            cheatSet.add((curNode, cheatNode))
                            cost = 2
                newTotalCost= curCost+cost
                prevBest = distance.get(newNode, float('inf'))
                if  prevBest>newTotalCost:
                    distance[newNode] = newTotalCost
                    if newNode == target:
                        if mini>newTotalCost:
                            mini = newTotalCost
                    heapq.heappush(toExpand,(newTotalCost,newNode)) 
        if exploredCheats==tmp:
            break
        else:
            val = 9464-mini
            if val!=0:
                if val in save:
                    save[val]+=1
                else:
                    save[val]=1
                if val>=100:
                    ans +=1      
                #print('Cheat taken!: ', tmpCheat[0], 84-mini)
            if len(save)%20==0:
                print(save)
    print(save)
    print(f'Answer!: {ans}')

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
        performTests(2024, 20, [84],main)#9464 
    else:
        score = getAnswer(2024, 20, main)
        print("The shortest path is: {0}".format(score))