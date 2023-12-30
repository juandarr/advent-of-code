def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and extract every position and velocity for each hailstone
    hailstones = []
    for line in lines:
        tmp = line.strip().split('@')
        tmp = {'pos': [int(i) for i in  tmp[0].strip().split(',')], 'vel': [int(i) for i in  tmp[1].strip().split(',')]}
        hailstones.append(tmp)
    return hailstones

def findEstimate(hailstones):
    return

if __name__=='__main__': 
    test = True
    testNumber =1 
    '''
    Answers to tests
    1: 2 
    '''
    if test:
        filename = "day24-test{0}-input.txt".format(testNumber)
    else:
        filename = "day24-1-input.txt"
    lines = read_file(filename)
    hailstones = parseInformation(lines)
    print(hailstones)
