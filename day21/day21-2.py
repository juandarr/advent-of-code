from time import sleep, time
from copy import deepcopy
import numpy as np

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
    if m[s[0]][s[1]]=='#':
        return 0
    branches = set()
    branches.add(s)
    while step<=limit:
        tmp = set()
        for b in branches:
            for d in dir:
                i = b[0]+dir[d][0]
                j = b[1]+dir[d][1]
                if m[i%len(m)][j%len(m[0])] in ['.','S']:
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
    m,start = parseInformation(lines)
    dir = {'n':(-1,0), 's':(1,0), 'e':(0,1), 'w': (0,-1)}
    points = []
    for s in range(3):
        val = steps(start, 1,m,dir,s*131+65)
        points.append([s,val])
    A = np.zeros((3,3))
    B = np.zeros((3,1))
    for i in range(3):
        A[i,0]=(points[i][0])**2
        A[i,1]=points[i][0]
        A[i,2]=1
        B[i,0] = points[i][1]
    sol = np.linalg.solve(A,B)
    val = int(26501365/131)
    answer  = int(sol[0,0])*val*val + int(sol[1,0])*val + int(sol[2,0])
    print(answer)