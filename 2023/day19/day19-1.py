from time import sleep, time
import heapq

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    wf = {}
    parts = []
    c= 0
    while lines[c]!='\n':
        tmp =lines[c].strip().split('{')
        name = tmp[0]
        tmp = tmp[1][:-1]
        tmp = tmp.split(',')
        tmpAr = []
        for i in tmp:
            tmpAr.append(tuple(i.split(':')))
        wf[name] = tmpAr
        c+=1
    c+=1
    for line in lines[c:]:
        tmp = line.strip()[1:-1].split(',')
        tmpAr = {}
        for i in tmp:
            tmp_i = i.split('=')
            tmpAr[tmp_i[0]]=int(tmp_i[1])
        parts.append(tmpAr)
    return  wf,parts

def workflows(wf,parts):
    net = 0
    for part in parts:
        cur = 'in'
        x =part['x']
        m = part['m']
        a = part['a']
        s = part['s']
        while cur not in ['A','R']:
            default = True
            for rule in wf[cur][:-1]:
                if eval(rule[0]):
                    cur = rule[1]
                    default=False
                    break
            if default:
                cur = wf[cur][-1][0]
        if cur=='A':
            for k in part:
                net += part[k]
    return net 

if __name__=='__main__': 
    test = False
    testNumber = 1
    if test:
        filename = "day19-test{0}-input.txt".format(testNumber)
    else:
        filename = "day19-1-input.txt"
    lines = read_file(filename)
    wf,parts = parseInformation(lines)
    net = workflows(wf,parts)

    print(net)