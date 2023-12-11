def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m =[]
    r= []
    # Read lines 
    row= 0
    expansion =1 
    for line in lines:
        tmp = line.strip()
        if tmp == '.'*len(tmp):
            r.append(row)
        m.append(list(tmp))
        row += 1
    galaxies = []
    c = []
    j = 0
    # Expand by columns and store location of galaxies
    while (j<len(m[0])):
        allDots = True
        for i in range(len(m)):
            if m[i][j]!='.':
                allDots = False
                break
        if allDots:
            c.append(j)
        else:
            for i in range(len(m)):
                if m[i][j]=='#':
                    galaxies.append((i+expansion*len([val for val in r if val<i]),j+expansion*len([val for val in c if val<j])))
        j += 1
    return m,galaxies

if __name__=='__main__': 
    test = True
    if test:
        filename = "day11-test-input.txt"
    else:
        filename = "day11-1-input.txt"
    lines = read_file(filename)
    m,galaxies= parseInformation(lines)
    net = 0
    for idx,galaxy in enumerate(galaxies):
        i = idx + 1
        while (i<len(galaxies)):
            galaxy2 = galaxies[i]
            d = abs(galaxy[0]-galaxy2[0]) + abs(galaxy[1] - galaxy2[1]) 
            net += d
            i += 1
    print(net)
