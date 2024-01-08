import random
from copy import deepcopy

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and extract every position and velocity for each hailstone
    graph ={} 
    for line in lines:
        tmp = line.strip().split(':')
        graph[tmp[0]] = list(tmp[1].strip().split())
    # From this list of nodes create graph
    new = {}
    for node in graph:
        for i in graph[node]:
            if i not in graph:
                if i not in new:
                    new[i] = [node]
                else:
                    new[i].append(node)
            else:
                if node not in graph[i]:
                    graph[i].append(node)
    for node in new:
        graph[node] = new[node]

    return graph 

def getEdges(graph):
    edges = []
    for node in graph:
        for node2 in graph[node]:
            edges.append((node, node2))
    return edges

def contraction(graph, edge):
    newVertex = ''.join(edge)
    nodes = []
    # print('Before: ',graph, edge)
    for e in edge:
        for node in graph[e]:
            if node not in edge:
                nodes.append(node)
    for node in graph:
        if node not in edge:
            if edge[0] in graph[node]:
                indexes = [i for i,x in enumerate(graph[node]) if x==edge[0]]
                for idx in indexes:
                    graph[node][idx] = newVertex
            if edge[1] in graph[node]:
                indexes = [i for i,x in enumerate(graph[node]) if x==edge[1]]
                for idx in indexes:
                    graph[node][idx] = newVertex
    del graph[edge[0]]
    del graph[edge[1]]
    graph[newVertex] = nodes
    # print('After: ',graph, edge)

def kargerAlgorithm(graph):
    # print('Before: \n','Graph: ', graph, '\nEdges: ', edges)
    while len(graph)>2:
        edges = getEdges(graph)
        random_idx = random.choice(range(len(edges))) 
        edge  = edges[random_idx]
        # print(random_idx, edge)
        contraction(graph, edge)
        # print('After: \n','Graph: ', graph, '\nEdges: ', edges)
    edges = getEdges(graph)
    # print('After: \n','Graph: ', graph, '\nEdges: ', len(edges))
    print(len(edges))
    if len(edges)==6:
        net = 1
        for node in graph:
            net *= len(node)//3 
        print('Result!: ', net)

if __name__=='__main__': 
    test = False
    testNumber =1 
    '''
    Answers to tests
    1: 54 - minCut is 3 
    2: 3 - minCut is 2
    '''
    if test:
        filename = "day25-test{0}-input.txt".format(testNumber)
    else:
        filename = "day25-1-input.txt"
    lines = read_file(filename)
    graph = parseInformation(lines)
    for i in range(500):
        print(i)
        graph_cp = deepcopy(graph)
        kargerAlgorithm(graph_cp)