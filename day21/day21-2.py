from time import sleep, time
from copy import deepcopy
import heapq

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
    
# def stepsIn(steps,m,dir):
#     for s in range(2,steps+1):
#         for i in range(len(m)):
#             for j in range(len(m[0])):
#                 diag = []
#                 if m[i][j] in ['.', 'S']:
#                     tmp = 0
#                     for d in dir:
#                         i_tmp = i+dir[d][0]
#                         j_tmp = j+dir[d][1]
#                         if m[i_tmp%len(m)][j_tmp%len(m[0])] in ['.','S']:
#                             tmp += mem[((i_tmp%len(m), j_tmp%len(m[0])), s-1)]
#                             diag.append((i_tmp,j_tmp))
#                     for idx,p in enumerate(diag):
#                         l = idx+1
#                         while (l<len(diag)):
#                             if abs(diag[l][0]-p[0])+abs(diag[l][1]-p[1])==2:
#                                 tmp -=1
#                             l +=1
#                     mem[((i, j),s)] =tmp
#                     print(s, tmp )

if __name__=='__main__': 
    test =True
    testNumber = 1
    if test:
        filename = "day21-test{0}-input.txt".format(testNumber)
    else:
        filename = "day21-1-input.txt"
    lines = read_file(filename)
    m,start = parseInformation(lines)
    dir = {'n':(-1,0), 's':(1,0), 'e':(0,1), 'w': (0,-1)}
    for s in range(2,20):
        val = steps(start, 1,m,dir,s)
        print('\n',start,s, ': ',val, (s+1)**2)
        for d in dir:
            i = start[0]+dir[d][0]
            j = start[1]+dir[d][1]
            val2 = steps((i,j), 1,m,dir,s-1)
            print((i,j), s-1, ': ', val2)
    # mem ={}
    # for i in range(len(m)):
    #     for j in range(len(m[0])):
    #         diag = []
    #         if m[i][j] in ['.', 'S']:
    #             for d in dir:
    #                 i_tmp = i+dir[d][0]
    #                 j_tmp = j+dir[d][1]
    #                 if m[i_tmp%len(m)][j_tmp%len(m[0])] in ['.','S']:
    #                     diag.append((i_tmp,j_tmp))
    #             mem[((i, j),1)] = len(diag)
    # stepsIn(10**6,m,dir)
