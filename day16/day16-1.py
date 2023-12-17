# import sys
# sys.setrecursionlimit(10**5)
from time import sleep

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

visited = set()

def runBeam(m, start, dir):
    i = start[0] 
    j = start[1]
    curDir = dir
    while inLimits(i,j) and ((i,j),curDir) not in visited:
        if m[i][j]!='.':
            if m[i][j] in ['|','-']:
                if m[i][j]=='|' and curDir in [(0,1),(0,-1)]:
                    visited.union(runBeam(m,[i,j],(-1,0)))
                    visited.union(runBeam(m,[i,j],(1,0)))
                    break
                if m[i][j]=='-' and curDir in [(1,0),(-1,0)]:
                    visited.union(runBeam(m,[i,j],(0,1)))
                    visited.union(runBeam(m,[i,j],(0,-1)))
                    break
            else:
                curDir = changeDir(curDir, m[i][j])
        visited.add(((i,j),curDir))
        i += curDir[0]
        j += curDir[1]
        print((i,j))
    return visited 

if __name__=='__main__': 
    test = False
    testNumber = 2
    if test:
        filename = "day16-test{0}-input.txt".format(testNumber)
    else:
        filename = "day16-1-input.txt"
    file = read_file(filename)
    m = parseInformation(file)
    startDir = (0,1)
    start=[0,0]
    visited = runBeam(m,start,startDir)
    final = set()
    for i in visited:
        final.add(i[0])
    print(final,len(final))
# Too low: 5990
# Too low: 6005