from time import sleep, time
from copy import deepcopy
import heapq

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    ops= {} 
    for line in lines:
        tmp = line.strip().split('->')
        input = tmp[0].strip()
        if input[0]=='b':
            node = input
        else:
            node = input[1:]
        type = input[0]
        output = tmp[1].strip().split(', ')
        ops[node] = {'type': type, 'output': output}
        
    # Calculate state
    state = {}
    for operation in ops:
        t = ops[operation]['type']
        node =  operation
        if t=='%':
            state[node]= {'type': '%', 'state':False}
        elif t=='&':
            state[node] = {'type':'&', 'state':True, 'input':[]}
        elif t=='b':
            state[node] = {'type': 'b', 'state': False, 'output': ops[operation]['output']}
    for node in state:
        if state[node]['type']=='&':
            for node2 in ops:
                if node in ops[node2]['output']:
                    state[node]['input'].append(node2)
    return ops, state 

def operations(ops, state):
    pushes = 1000
    startState = deepcopy(state)
    neg = 0
    pos = 0
    for i in range(pushes):
        print('Pulse: ',i+1)
        # print([[False,'broadcaster']])
        neg +=1
        cur = 'broadcaster'
        queue = []
        for e in ops[cur]['output']:
            queue.append([False, e])
        while queue!=[]:
            #print(queue)
            addToQueue = []
            for q in queue:
                if q[0]:
                    pos+=1
                else:
                    neg+=1
                curSignal = q[0]
                node = q[1]
                t = ops[node]['type']
                if t=='%': 
                    if curSignal==False:
                        state[node]['state'] = not(state[node]['state'])
                        for n in ops[node]['output']:
                            addToQueue.append([state[node]['state'],n])
                elif t=='&':
                    tmp = False
                    for n in state[node]['input']:
                        if state[n]['state']==False:
                            tmp = True
                            break
                    state[node]['state'] = tmp
                    for n in ops[node]['output']:
                        if n in state:
                            addToQueue.append([tmp,n])
                        else:
                            if tmp:
                                pos +=1
                            else:
                                neg+=1
            queue = []
            for op in addToQueue:
                queue.append(op)
            # print('Current state: ', state)
            # print('Starting state: ', startState)
        completed = True
        for node in state:
            if startState[node]['state']!=state[node]['state']:
                completed =False 
                break
        if completed:
            break
    print(state, pos, neg)
    m = 1000//(i+1)
    return (m*pos)*(m*neg)


if __name__=='__main__': 
    test = False
    testNumber = 1
    if test:
        filename = "day20-test{0}-input.txt".format(testNumber)
    else:
        filename = "day20-1-input.txt"
    lines = read_file(filename)
    ops,state = parseInformation(lines)
    print('Operations: ',ops)
    print('State: ', state)
    result = operations(ops, state)
    print(result)
# Too low: 849174300