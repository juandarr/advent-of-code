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
        tmp = [-1*d[1],-1*d[0]]
    elif mirror=='/':
        tmp = [d[1], d[0]]
    return d


def runBeam(m, start, dir):
    i = start[0] 
    j = start[1]
    curDir = dir
    visited = {}
    net = 0
    while inLimits(i,j) and (i,j) not in visited:
        visited[(i,j)] = 1
        i += curDir[0]
        j += curDir[1]
        if m[i][j]!='.':
            if m[i][j] in ['|','-']:
                pass
                # Ramification
            else:
                curDir = changeDir(curDir, m[i][j])
        pass
    return net+len(visited) 

if __name__=='__main__': 
    test = True
    if test:
        filename = "day16-test-input.txt"
    else:
        filename = "day16-1-input.txt"
    file = read_file(filename)
    m = parseInformation(file)
    startDir = [1,0]
    start=[0,0]
    runBeam(m,start,dir)
    print(m)