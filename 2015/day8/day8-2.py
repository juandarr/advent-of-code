from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    strs = data.rstrip().split('\n')
    return strs


def getDiff(strs):
    total = 0
    for idx,s in enumerate(strs): 
        total += 4
        tmp = s[1:-1]
        rawStrs = [r'\\\\',r'\\\"',r'\\x[0-9,a,b,c,d,e,f]{2}']
        for rule,rawStr in enumerate(rawStrs):
            positions = re.findall(rawStr,tmp)
            if rule==2:
                total += 1*len(positions)
            else:
                total +=2*len(positions)
    return total

def main(filename):
    strs = parseInformation(filename)
    dif = getDiff(strs)
    return dif

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 8, [19], main, test=["1"])
    else:
        dif = getAnswer(2015, 8, main)
        print("The difference between number of characters of code and characters in memory is {0}".format(dif))