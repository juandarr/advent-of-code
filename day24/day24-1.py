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

def findEstimate(hailstones, limits):
    i = 0
    c= 0
    while i<len(hailstones)-1:
        p1 = hailstones[i]
        j = i+1
        while j<len(hailstones):
            p2 = hailstones[j]
            m = -1*p2['vel'][1]/p2['vel'][0]
            num = m*(p2['pos'][0]-p1['pos'][0])+p2['pos'][1]-p1['pos'][1]
            den = p1['vel'][1]+m*p1['vel'][0]
            if den!=0: 
                t1 = num/den
                num = p1['vel'][1]*t1-p2['pos'][1]+p1['pos'][1]
                den = p2['vel'][1]
                if den!=0:
                    t2 = num/den
                    if (t1>0 and t2>0):
                        x = p1['vel'][0]*t1+p1['pos'][0]
                        y = p1['vel'][1]*t1+p1['pos'][1]
                        if x>=limits[0] and x<=limits[1] and y>=limits[0] and y<=limits[1]:
                            c+=1
            j +=1
        i+=1
    return c

if __name__=='__main__': 
    test = False
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
    # Test
    # limits = [7,27]
    limits= [200000000000000, 400000000000000]
    c= findEstimate(hailstones,limits)
    print('Estimate: ', c)
