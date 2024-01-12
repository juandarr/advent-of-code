def parseInformation(filename):
    file = open(filename, "r")
    tmp= file.read()
    tmp= tmp.rstrip().split('\n')
    idx = 0
    while (tmp[idx][1] != '1'):
        idx +=1
    actionIdx = idx+2
    # Extract stacks
    stacks = []
    j=0
    while (1+4*j<len(tmp[idx])):
        stacks.append([])
        j += 1
    idx -= 1
    while idx>=0:
        j = 0
        while (1+4*j<len(tmp[idx])):
            if tmp[idx][1+4*j]!=' ':
                stacks[j].append(tmp[idx][1+4*j])
            j += 1
        idx -= 1
    actions = []
    # Extract actions
    for op in tmp[actionIdx:]:
        op = op.strip('move ').replace(' from ', ',').replace(' to ',',').split(',')
        op = [int(x) for x in op] 
        actions.append(op)
    return stacks,actions

def performActions(stacks, actions):
    for action in actions:
        tmp = []
        for i in range(action[0]):
            tmp.append(stacks[action[1]-1].pop())
        stacks[action[2]-1].extend(tmp)
    ans =''
    for idx in range(len(stacks)):
        ans += stacks[idx][-1]    
    return ans

if __name__=='__main__': 
    test = False
    if test:
        filename = "day5-test-input.txt"
    else:
        filename = "day5-input.txt"
    stacks, actions = parseInformation(filename)
    ans = performActions(stacks,actions)
    print("Here are the top crates in the every stack {0}".format(ans))


