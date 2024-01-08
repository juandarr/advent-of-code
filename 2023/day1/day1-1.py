
def read_file(filename):
    return open(filename, "r")

if __name__=='__main__': 
    lines = read_file("day1-1-input.txt")
    digits = set([0,1,2,3,4,5,6,7,8,9])
    net = 0
    for line in lines:
        values = []
        for s in line:
            try:
                if int(s) in digits: 
                    values.append(int(s))
            except: 
                continue
        print(values)
        val = int('{0}{1}'.format(values[0], values[-1]))
        net  += val 
        print(val)
    print(net)