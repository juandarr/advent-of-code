def read_file(filename):
    return open(filename, "r")

def parseInformation(lines):
    seeds = lines[0].strip().split(':')[1].strip().split()
    print(seeds)
    #for line in lines:

if __name__=='__main__': 
    lines = read_file("day4-1-input.txt")
    seeds, mapping= parseInformation(lines)