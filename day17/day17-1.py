# import sys
# sys.setrecursionlimit(10**5)
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

def inLimits(i,j):
    if i<0 or i>len(m)-1 or j<0 or j>len(m[0])-1:
        return False
    return True

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
    print(m)
    start=[0,0]
    t =time()-t0
    print('Total duration (secs): {0}'.format(t))