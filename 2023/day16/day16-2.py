# import sys
# sys.setrecursionlimit(10**5)
from time import sleep,time

def read_file(filename):
    file = open(filename,'r')
    return file.read()

def parseInformation(file):
    # Read lines and expand by rows
    lines = file.split('\n')
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m

def inLimits(i,j):
    if i<0 or i>len(m)-1 or j<0 or j>len(m[0])-1:
        return False
    return True

def changeDir(d, mirror):
    tmp = []
    if mirror=='\\':
        tmp = (d[1],d[0])
    elif mirror=='/':
        tmp = (-1*d[1], -1*d[0])
    return tuple(tmp)


def runBeam(m, start, dir, visited):
    i = start[0] 
    j = start[1]
    curDir = dir
    while inLimits(i,j) and ((i,j),curDir) not in visited:
        visited.add(((i,j),curDir))
        if m[i][j]!='.':
            if m[i][j] in ['|','-']:
                if m[i][j]=='|' and curDir in [(0,1),(0,-1)]:
                    visited.union(runBeam(m,[i-1,j],(-1,0),visited))
                    visited.union(runBeam(m,[i+1,j],(1,0),visited))
                    break
                if m[i][j]=='-' and curDir in [(1,0),(-1,0)]:
                    visited.union(runBeam(m,[i,j+1],(0,1),visited))
                    visited.union(runBeam(m,[i,j-1],(0,-1),visited))
                    break
            else:
                curDir = changeDir(curDir, m[i][j])
        i += curDir[0]
        j += curDir[1]
    return visited 

if __name__=='__main__': 
    test =False
    testNumber = 1
    if test:
        filename = "day16-test{0}-input.txt".format(testNumber)
    else:
        filename = "day16-1-input.txt"
    file = read_file(filename)
    m = parseInformation(file)
    t0 = time()
    netMax = -float('inf')
    for j in range(len(m[0])):
        start=[0,j]
        startDir = (1,0)
        visited = set()
        visited = runBeam(m,start,startDir,visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final)>netMax:
            netMax = len(final)
    for j in range(len(m[0])):
        start=[len(m)-1,j]
        startDir = (-1,0)
        visited = set()
        visited = runBeam(m,start,startDir,visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final)>netMax:
            netMax = len(final)
    for i in range(len(m)):
        start=[i,0]
        startDir = (0,1)
        visited = set()
        visited = runBeam(m,start,startDir,visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final)>netMax:
            netMax = len(final)
    for i in range(len(m)):
        start=[i,len(m[0])-1]
        startDir = (0,-1)
        visited = set()
        visited = runBeam(m,start,startDir,visited)
        final = set()
        for i in visited:
            final.add(i[0])
        if len(final)>netMax:
            netMax = len(final)
    print(netMax)
    t =time() - t0
    print('Total duration (secs): {0}'.format(t))