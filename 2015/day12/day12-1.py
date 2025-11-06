from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    return data.rstrip() 

def addNumbers(s):
    tmp = ''
    total = 0
    idx = 0
    while idx<len(s):
        while s[idx].isdigit() or s[idx]=='-':
            tmp += s[idx]
            idx+=1
        if tmp !='':
            total += int(tmp)  
            tmp = ''
        idx +=1
    return total

def main(filename):
    s = parseInformation(filename)
    print(s)
    net = addNumbers(s)
    return net

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 12, [12,6,0,0], main)
    else:
        iterations = getAnswer(2015, 12, main)
        print("Given current Santa's password next password is {0}".format(iterations))