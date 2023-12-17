def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m

def runBeam(m):
    return 0

if __name__=='__main__': 
    test = True
    if test:
        filename = "day16-test-input.txt"
    else:
        filename = "day16-1-input.txt"
    lines = read_file(filename)
    m = parseInformation(lines)
    print(m)