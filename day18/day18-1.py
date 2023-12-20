from time import sleep, time
import heapq

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip().split()))
    return m

'''
Finds when a given edge location/region is the entry/exit point to the interior
'''
def isWallPresent(i,j,ground):
    arc = [0,0]
    if i+1< len(ground):
        if ground[i+1][j]=='#':
            arc[1]=1
    if i-1 >=0:
        if ground[i-1][j]=='#':
            arc[0]=1
    while (ground[i][j]=='#'):
        j+=1
        if (j>=len(ground[0])):
            break
    j -=1
    if i+1< len(ground):
        if ground[i+1][j]=='#':
            arc[1]=1
    if i-1 >=0:
        if ground[i-1][j]=='#':
            arc[0]=1
    if arc==[1,1]:
        return True,j
    return False,j

def dig(start,m, groundDug):
    # Find the ground edge based on intructions
    groundDug.add(start)
    i,j = start
    lim_i =[0,0] 
    lim_j =[0,0]
    dir = {'R':(0,1),'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
    for instruction in m:
        direction, value, color = instruction
        d = dir[direction]
        value = int(value)
        for _ in range(value):
            i += d[0]
            j += d[1]
            groundDug.add((i,j))
            if (i<lim_i[0]):
                lim_i[0] = i
            elif (i>lim_i[1]):
                lim_i[1] = i
            if (j<lim_j[0]):
                lim_j[0] = j
            elif (j>lim_j[1]):
                lim_j[1] = j
    # Create the ground edge in a matrix form
    ground = []
    i_calibration = -lim_i[0]
    j_calibration = -lim_j[0]
    for i in range(lim_i[0]+i_calibration,lim_i[1]+1+i_calibration):
        ground.append([])
        for j in range(lim_j[0]+j_calibration, lim_j[1]+1+j_calibration):
            ground[-1].append('.')
    for s in groundDug:
        ground[s[0]+i_calibration][s[1]+j_calibration] = '#'
    # Fill the ground
    i = 0 
    count = 0
    while (i<len(ground)):
        j = 0
        open = False
        tmp = 0
        while (j<len(ground[0])):
            if open:
                if ground[i][j]=='.':
                    tmp +=1
                if ground[i][j]=='#':
                    wallPresent, j = isWallPresent(i,j,ground)
                    if wallPresent:
                        open = False
                        count += tmp
            else:
                if ground[i][j]=='#':
                    wallPresent, j = isWallPresent(i,j,ground)
                    if wallPresent:
                        open = True
                        tmp = 0
            j+=1
        i+= 1
    return count+len(groundDug)

if __name__=='__main__': 
    test = False
    testNumber = 1
    if test:
        filename = "day18-test{0}-input.txt".format(testNumber)
    else:
        filename = "day18-1-input.txt"
    lines = read_file(filename)
    m = parseInformation(lines)
    groundDug = set()
    area = dig((0,0), m, groundDug)
    print(area)