def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    directions = lines[0].strip() 
    nodes ={}
    for line in lines[2:]:
        tmp = line.strip().split('=')
        key = tmp[0].strip()
        value = tmp[1].strip().split(',')
        nodes[key] = [value[0].strip()[1:], value[1].strip()[:-1]]
    return nodes, directions

def primeDecomposition(number):
    primes = {}    
    tmp = number
    c = 0
    while (tmp%2==0):
        tmp /= 2
        c += 1
    if c>0:
        primes[2] = c
    div = 3
    while (tmp>1):
        c = 0
        while(tmp%div==0):
            tmp /= div
            c += 1
        if c>0:
            primes[div] = c
        div += 2
    return primes

if __name__=='__main__': 
    test = False
    if test:
        filename = "day8-test2-input1.txt"
    else:
        filename = "day8-1-input.txt"
    dirsIndex= {'L':0,'R':1}
    lines = read_file(filename)
    nodes,directions = parseInformation(lines)
    endChar = 'Z'
    curNodes = []
    endSteps= []
    completed = []
    for node in nodes:
        if node[-1]=='A':
            curNodes.append(node)
            endSteps.append(0)
            completed.append('f')
    steps = 0
    end = False
    while not(end):
        for d in directions:
            end = True
            for (index, node) in enumerate(curNodes):
                curNodes[index] = nodes[node][dirsIndex[d]]
                if curNodes[index][-1]!=endChar:
                    end = False
                else:
                    if endSteps[index] == 0:
                        endSteps[index] = steps+1
                        completed[index]='t'
                    if ''.join(completed) == 't'*len(endSteps):
                        end = True
                        break
            steps += 1
            if end ==True:
                if ''.join(completed) == 't'*len(endSteps):
                    for (index,step) in enumerate(endSteps):
                        endSteps[index] = primeDecomposition(step)
                    commonMultiple = {} 
                    for stepDict in endSteps:
                        for key in stepDict:
                            if key in commonMultiple:
                                if (commonMultiple[key]<stepDict[key]):
                                    commonMultiple[key] = stepDict[key]
                            else:
                                commonMultiple[key] =stepDict[key]
                    net = 1
                    for key in commonMultiple:
                        net *= key**commonMultiple[key]
                    print('Answer!: ',net)
                    break
                else:
                    print(steps)
                    break