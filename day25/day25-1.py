import heapq

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and extract every position and velocity for each hailstone
    nodes ={} 
    for line in lines:
        tmp = line.strip().split(':')
        nodes[tmp[0]] = list(tmp[1].strip().split())
    # From this list of nodes create graph
    new = {}
    for node in nodes:
        for i in nodes[node]:
            if i not in nodes:
                if i not in new:
                    new[i] = [node]
                else:
                    new[i].append(node)
            else:
                if node not in nodes[i]:
                    nodes[i].append(node)
    for node in new:
        nodes[node] = new[node]
    return nodes 

def findGroups(nodes):
    start = 'jqt'
    toExplore = [start]
    visited ={}
    while (toExplore):
        tmp = heapq.heappop(toExplore)
        level = tmp[0]
        curNode = tmp[1]
        print(tmp)
        visited[curNode] =level
        for node in nodes[curNode]:
            heapq.heappush(toExplore,(level+1,node))
    print(visited, len(visited))
    return

if __name__=='__main__': 
    test = True
    testNumber =1 
    '''
    Answers to tests
    1: 54 
    '''
    if test:
        filename = "day25-test{0}-input.txt".format(testNumber)
    else:
        filename = "day25-1-input.txt"
    lines = read_file(filename)
    nodes = parseInformation(lines)
    print(nodes)
    findGroups(nodes)