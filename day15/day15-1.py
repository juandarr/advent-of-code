def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    steps = []
    for line in lines:
        if line.strip()!='':
            steps = list(line.strip().split(','))
    return steps

def hash(str):
    val = 0
    for c in str:
        val += ord(c) 
        val *=17
        val %= 256
    return val

if __name__=='__main__': 
    test =False
    if test:
        filename = "day15-test-input.txt"
    else:
        filename = "day15-1-input.txt"
    lines = read_file(filename)
    steps = parseInformation(lines)
    net = 0
    for step in steps:
        net += hash(step)
    print(net)