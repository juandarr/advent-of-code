'''
'''
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

if __name__=='__main__': 
    test = False
    testNumber= 1
    if test:
        filename = "day8-test-input{0}.txt".format(testNumber)
    else:
        filename = "day8-1-input.txt"
    dirsIndex= {'L':0,'R':1}
    lines = read_file(filename)
    nodes,directions = parseInformation(lines)
    startNode = 'AAA'
    endNode = 'ZZZ'
    curNode = startNode
    steps = 0
    while curNode != endNode:
        for d in directions:
            curNode = nodes[curNode][dirsIndex[d]]
            steps += 1
            if curNode == endNode:
                break
    print(steps)