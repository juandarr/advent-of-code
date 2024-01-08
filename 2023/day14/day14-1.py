def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m = []
    # Read lines and expand by rows
    for line in lines:
        m.append(list(line.strip()))
    return m

def moveRocks(m):
    i = 0
    net = 0
    while (i<len(m)):
        j = 0
        while (j<len(m[i])):
            if m[i][j]=='O':
                iTmp = i
                origin = [i,j]
                iTmp -= 1
                if iTmp<0:
                    j += 1
                    net += len(m)-origin[0]
                    continue
                while m[iTmp][j] not in ['#', 'O']:
                    iTmp -=1
                    if iTmp<0:
                        break 
                m[origin[0]][origin[1]] ='.'
                m[iTmp+1][j] = 'O'
                net += len(m)-iTmp-1
            j+=1
        i += 1
    return net 

if __name__=='__main__': 
    test =False
    if test:
        filename = "day14-test-input.txt"
    else:
        filename = "day14-1-input.txt"
    lines = read_file(filename)
    m = parseInformation(lines)
    net = moveRocks(m)
    print(net)