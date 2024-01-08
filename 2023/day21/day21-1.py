from time import sleep, time
from copy import deepcopy

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    m = []
    c = 0
    for line in lines:
        tmp = list(line.strip())
        for idx,val in enumerate(tmp):
            if val=='S':
                start = (c,idx)
        c +=1
        m.append(tmp)
    return m,start 

def steps(s,step, m, dir, limit):
    counter = 0
    branches = set()
    branches.add(s)
    while step<=limit:
        tmp = set()
        for b in branches:
            for d in dir:
                i = b[0]+dir[d][0]
                j = b[1]+dir[d][1]
                if i<0 or i>len(m)-1:
                    continue
                if j<0 or j>len(m[0])-1:
                    continue
                if m[i][j] in ['.','S']:
                    tmp.add((i,j)) 
        counter += len(tmp)
        branches = tmp
        step +=1
    return len(tmp) 

if __name__=='__main__': 
    test = False
    testNumber = 1
    if test:
        filename = "day21-test{0}-input.txt".format(testNumber)
    else:
        filename = "day21-1-input.txt"
    lines = read_file(filename)
    limit = 64 
    m,start = parseInformation(lines)
    dir = {'n':(-1,0), 's':(1,0), 'e':(0,1), 'w': (0,-1)}
    # print(m,start)
    steps = steps(start,1,m,dir,limit)
    print(steps)