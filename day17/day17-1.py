from time import sleep, time
import heapq

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

def explore(starts, m, minM):
    toExpand = []
    for start in starts:
        heapq.heappush(toExpand, start)
    visited = set()
    while toExpand:
        curEnergy, curNode, curDir, steps = heapq.heappop(toExpand)
        if curNode==(len(m)-1, len(m[0])-1):
            return curEnergy
        if (curNode, curDir, steps) in visited:
            continue
        visited.add((curNode, curDir,steps))
        dir = (curDir, (curDir[1],curDir[0]),(-1*curDir[1], -1*curDir[0]))
        for d in dir:
            nextNode =(curNode[0]+d[0], curNode[1]+d[1])
            straight = 1
            if curDir==d:
                straight +=steps 
            if not(inLimits(nextNode[0],nextNode[1],m)) or straight>3: 
                continue    
            tmp = curEnergy+ int(m[nextNode[0]][nextNode[1]])
            if tmp<minM[nextNode[0]][nextNode[1]]:
                minM[nextNode[0]][nextNode[1]] = tmp
            heapq.heappush(toExpand,(tmp,nextNode,d, straight))

if __name__=='__main__': 
    test =False
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
    minM[0][0] = 0
    m[0][0]= 0
    minM[0][1]= int(m[0][1])
    minM[1][0]= int(m[1][0])
    t0 =time()
    s = explore(((int(m[0][1]),(0,1),(0,1),1),(int(m[1][0]),(1,0),(1,0),1)),m, minM)
    t =time()-t0
    print(minM)
    print(s)
    print('Total duration (secs): {0}'.format(t))