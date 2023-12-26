from time import sleep, time

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    bricks = []
    for line in lines:
        points = line.strip().split('~')
        p = []
        for point in points:
            x,y,z = point.split(',')
            p.append([int(x), int(y), int(z)])
        bricks.append(p)
    return  bricks

def exploreFall(bricks):
    pass

if __name__=='__main__': 
    test = True
    testNumber = 1
    if test:
        filename = "day22-test{0}-input.txt".format(testNumber)
    else:
        filename = "day22-1-input.txt"
    lines = read_file(filename)
    bricks = parseInformation(lines)
    print(bricks, len(bricks))