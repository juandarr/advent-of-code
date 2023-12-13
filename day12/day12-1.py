def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m =[]
    # Read lines and expand by rows
    for line in lines:
        tmp = line.strip().split()
        m.append([list(tmp[0]),tmp[1].split(',') ])
    return m

if __name__=='__main__': 
    test =True
    if test:
        filename = "day12-test-input.txt"
    else:
        filename = "day12-1-input.txt"
    lines = read_file(filename)
    m= parseInformation(lines)
    print(m)
