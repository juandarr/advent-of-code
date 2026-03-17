from os.path import dirname, abspath
import sys
import heapq
import time

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    codes= []
    for row in rows:
        codes.append(''.join(list(row)))
    return codes

def combine(routes):
    paths = ['']
    for depth in range(len(routes)):
        newPaths = []
        for j in range(len(routes[depth])):
            for p in paths:
                newPaths.append(p+routes[depth][j])
        paths = newPaths
    return paths
            

def possiblePaths(start,target,isNumeric=False):
    global memo
    state_key=(start,target,isNumeric)
    if state_key in memo:
        return memo[state_key]
    if start==target:
        return ['A']
    dirs = {(0,1):'>',(0,-1):'<',(1,0):'v',(-1,0):'^'}
    bannedNode = (3,0) if isNumeric else (0,0)
    lims = (4,3) if isNumeric else (2,3)
    toExplore = [(-(abs(start[0]-target[0])+abs(start[1]-target[1])),start,'')]
    possiblePaths = []
    while toExplore:
        curCost, curNode, curPath = heapq.heappop(toExplore)
        curCost = -curCost
        for d in dirs:
            ni = curNode[0]+d[0]
            nj= curNode[1]+d[1]
            newNode = (ni,nj)
            newCost = abs(newNode[0]-target[0])+abs(newNode[1]-target[1])
            if newNode==bannedNode or ni<0 or ni>=lims[0] or nj<0 or nj>=lims[1]:
                continue 
            if newCost==0:
                possiblePaths.append(curPath+dirs[d]+'A')
            elif newCost < curCost:
                heapq.heappush(toExplore, (-newCost, newNode, curPath+dirs[d]))
    memo[state_key] = possiblePaths
    return possiblePaths

def simulation(codes):
    numPad = {'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0), '2':(2,1),'3':(2,2),'0':(3,1),'A':(3,2)}
    dirPad ={'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2)}

    stages = ['numeric','dirs','dirs']
    total = 0
    global memo
    memo = {}
    for code in codes:
        patterns = [code]
        mini = float('inf')
        for stage in stages: 
            newPatterns = []
            isNumeric = stage=='numeric'
            pad = numPad if isNumeric else dirPad
            cur= pad['A']
            for pattern in patterns:
                routes = []
                for c in pattern:
                    target = pad[c]
                    found = possiblePaths(cur,target,isNumeric)
                    routes.append(found)
                    cur = target
                paths = combine(routes)
                newPatterns.extend(paths)
            patterns = newPatterns
        for p in patterns:
            if len(p)<mini:
                mini = len(p)
        total += int(''.join(code[:-1]))*mini
    return total

def main(filename):
    codes = parseInformation(filename)
    p= simulation(codes)
    return p

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 21, [126384],main) 
    else:
        cx = getAnswer(2024, 21, main)
        print("The sum of complexities of the codes is {0}".format(cx))