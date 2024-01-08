def read_file(filename):
    return open(filename, "r")

def parseInformation(lines):
    c = 0
    for line in lines:
        if c==0:
            time = line.strip().split(':')[1].strip().split()
            c += 1
        else:
            distance = line.strip().split(':')[1].strip().split()
    return time,distance

if __name__=='__main__': 
    test =False 
    if test:
        filename = "day6-test-input.txt"
    else:
        filename = "day6-1-input.txt"
    lines = read_file(filename)
    times,distances = parseInformation(lines)
    c = 0
    net = 1
    while (c<len(times)):
        time = int(times[c])
        distance =int(distances[c])
        ways = 0
        for t in range(1,time):
            if (t*(time-t)>distance):
                ways += 1
        net *= ways
        c += 1
    print(net)