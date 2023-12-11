def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m =[]
    expansion = 2 
    # Read lines and expand by rows
    for line in lines:
        tmp = line.strip()
        if tmp == '.'*len(tmp):
            for _ in range(expansion):
                m.append(list(tmp))
        else:
            m.append(list(tmp))
    expanded = []
    for _ in range(len(m)):
        expanded.append([])
    j = 0
    galaxies = []
    # Expand by columns and store location of galaxies
    while (j<len(m[0])):
        allDots = True
        for i in range(len(m)):
            if m[i][j]!='.':
                allDots = False
                break
        if allDots:
            for i in range(len(expanded)):
                for _ in range(expansion):
                    expanded[i].append('.')
        else:
            for i in range(len(expanded)):
                expanded[i].append(m[i][j])
                if expanded[i][-1]=='#':
                    galaxies.append((i,len(expanded[i])-1))
        j += 1
    return m,galaxies

if __name__=='__main__': 
    test = False
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
