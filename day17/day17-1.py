from time import sleep, time

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

def inLimits(i,j,m):
    if i<0 or i>len(m)-1 or j<0 or j>len(m[0])-1:
        return False
    return True

def explore(m, minM):
    start = (0,0)
    next = []
    next.append((start,((0,1),1)))
    next.append((start,((1,0),1)))
    visited = set() 
    while next!=[]:
        location = next.pop()
        curNode = location[0]
        curDir = location[1][0]
        directions = (curDir,(curDir[1],curDir[0]),(-1*curDir[1], -1*curDir[0]))
        visited.add((curNode, (curDir, location[1][1])))
        for d in directions:
            nextNode =(curNode[0]+d[0], curNode[1]+d[1])
            sameDir = 1
            if d==curDir:
                sameDir += location[1][1]
            if not(inLimits(nextNode[0],nextNode[1],m)) or sameDir>3 or (nextNode,(d,sameDir)) in visited:
                continue
            tmp = minM[curNode[0]][curNode[1]]+int(m[nextNode[0]][nextNode[1]])
            if tmp<minM[nextNode[0]][nextNode[1]]:
                minM[nextNode[0]][nextNode[1]] = tmp
                next.append((nextNode,(d,sameDir)))
    print(minM)

if __name__=='__main__': 
    test = True
    testNumber = 1
    if test:
        filename = "day17-test{0}-input.txt".format(testNumber)
    else:
        filename = "day17-1-input.txt"
    file = read_file(filename)
    t0 = time()
    m = parseInformation(file)
    minM = []
    for i in range(len(m)):
        minM.append([])
        for j in range(len(m[0])):
            minM[i].append(float('inf'))
    minM[0][0] = int(0)
    print(m)
    explore(m,minM)
    t =time()-t0
    print('Total duration (secs): {0}'.format(t))