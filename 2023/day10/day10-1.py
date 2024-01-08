def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m =[]
    for line in lines:
        m.append(list(line.strip()))
        for index,v in enumerate(m[-1]):
            if 'S'==v:
                origin = (len(m)-1,index)
    return m, origin

if __name__=='__main__': 
    test = False
    testNumber= 2
    if test:
        filename = "day10-test{0}-input.txt".format(testNumber)
    else:
        filename = "day10-1-input.txt"
    lines = read_file(filename)
    m, origin= parseInformation(lines)
    shapes ={'|':[(-1,0),(1,0)],'-':[(0,-1),(0,1)],'L':[(-1,0),(0,1)], 'J':[(0,-1),(-1,0)],'7':[(0,-1),(1,0)],'F':[(1,0),(0,1)]}
    dirs = ((-1,0),(1,0),(0,-1),(0,1))
    cur = origin 
    candidates=[]
    for d in dirs:
        i = cur[0]+d[0]
        j = cur[1]+d[1]
        if m[i][j]!='.':
            if (-d[0],-d[1]) in shapes[m[i][j]]:
                idx  = shapes[m[i][j]].index((-d[0], -d[1]))
                candidates.append(((i,j), 
                shapes[m[i][j]][abs(idx- 1)]))
    visited={origin:1}
    complete = False
    while (candidates != [] and not(complete)):
        cur  = candidates.pop()
        curNode = cur[0]
        visited[curNode]=1
        complete = False
        d =cur[1]
        i = curNode[0]+d[0]
        j = curNode[1]+d[1]
        if m[i][j]=='S' and len(visited)>3:
            complete = True
            break
        if m[i][j] not in ['.','S'] and m[i][j] not in visited:
            if (-d[0],-d[1]) in shapes[m[i][j]]:
                idx  = shapes[m[i][j]].index((-d[0], -d[1]))
                candidates.append(((i,j),
            shapes[m[i][j]][abs(idx-1)]))
    print(len(visited)/2)