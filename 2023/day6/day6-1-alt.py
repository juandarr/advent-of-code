from math import sqrt,ceil,floor
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
        x2 = (time + sqrt(time**2 - 4*distance))/2.0
        x1= (time - sqrt(time**2 - 4*distance))/2.0
        # If solution is integer increase the value
        if x1==int(x1):
            x1 = int(x1)+1
        # Else take the ceil of the float
        else:
            x1 = ceil(x1)
        # If solution is integer increase the value
        if x2==int(x2):
            x2 = int(x2)-1
        # Else take the ceil of the float
        else:
            x2 = floor(x2)
        net *= x2-x1+1
        c += 1
    print(net)