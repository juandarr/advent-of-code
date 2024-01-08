from time import sleep, time
from math import factorial as f
import heapq

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    wf = {}
    c= 0
    while lines[c]!='\n':
        tmp =lines[c].strip().split('{')
        name = tmp[0]
        tmp = tmp[1][:-1]
        tmp = tmp.split(',')
        tmpAr = []
        for i in tmp[:-1]:
            iTmp = i.split(':')
            node = iTmp[0][0]
            if (len(iTmp[0].split('>'))>1):
                r = [int(iTmp[0].split('>')[1])+1, 4000]
            elif (len(iTmp[0].split('<'))>1):
                r = [1,int(iTmp[0].split('<')[1])-1]
            tmpAr.append(((node, r), iTmp[1]))
        tmpAr.append((tmp[-1],))
        wf[name] = tmpAr
        c+=1
    return  wf

def exploreWorkflows(wfs, wf, ranges, nodes):
    if wf in ['R','A']:
        if wf=='A':
            c = 1
            for r in ranges:
                c *= (r[1]-r[0]+1)
            return c
        return 0
    rules = wfs[wf]
    net = 0
    for rule in rules:
        if len(rule)>1:
            node = nodes[rule[0][0]]
            r = rule[0][1] 
            n = rule[1]
            include = ranges[node].copy()
            exclude = ranges[node].copy()
            if r[0]>ranges[node][0]:
                include[0] = r[0]
                exclude[1] =r[0]-1 
            if r[1]<ranges[node][1]:
                include[1] = r[1]
                exclude[0] = r[1]+1
            ranges[node] = include
            net += exploreWorkflows(wfs,n, ranges.copy(),nodes)
            ranges[node] = exclude
        else:
            n = rule[0]
            net += exploreWorkflows(wfs,n, ranges.copy(),nodes)
    return net 

if __name__=='__main__': 
    test = False
    testNumber = 1
    if test:
        filename = "day19-test{0}-input.txt".format(testNumber)
    else:
        filename = "day19-1-input.txt"
    lines = read_file(filename)
    nodes = {'x':0,'m':1 , 'a':2, 's':3}
    wfs = parseInformation(lines)
    possibilities = exploreWorkflows(wfs, 'in',[[1,4000],[1,4000],[1,4000],[1,4000]], nodes)
    print(possibilities)