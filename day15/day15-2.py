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
    test = False
    if test:
        filename = "day15-test-input.txt"
    else:
        filename = "day15-1-input.txt"
    lines = read_file(filename)
    steps = parseInformation(lines)
    boxes = {}
    lenses = {}
    for step in steps:
        tmp = step.split('=')
        if len(tmp)==2:
            inBox = False
            val = hash(tmp[0])
            if val in boxes:
                for idx,l in enumerate(boxes[val]):
                    if l[0] == tmp[0]:
                        inBox = True
                        boxes[val][idx][1] = tmp[1]
                        break
                if not(inBox):
                    boxes[val].append(tmp)
            else:
                boxes[val] = [tmp]
        else:
            tmp = tmp[0].split('-')  
            val = hash(tmp[0])
            if val in boxes:
                for idx,l in enumerate(boxes[val]):
                    if l[0] == tmp[0]:
                        del boxes[val][idx]
                        if len(boxes[val])==0:
                            del boxes[val]
                        break
    net = 0
    for val in boxes:
        for idx,l in enumerate(boxes[val]):
            net += (1+val)*(idx+1)*int(l[1])
    print(net)