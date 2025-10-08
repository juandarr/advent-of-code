from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    strs = data.rstrip().split('\n')
    print(strs)
    return strs


def getDiff(strs):
    totalR =0
    totalM = 0
    for s in strs: 
        totalR += len(s)
        totalM += len(s)-2
        tmp = s[1:-1]
        rawStrs = [r'\\\\',r'\\\"',r'(\\\\x[0-9,a,b,c,d,e,f]{2}|\w{1}\\x[0-9,a,b,c,d,e,f]{2}|^\\x[0-9,a,b,c,d,e,f]{2})']
        for rule,rawStr in enumerate(rawStrs):
            positions = re.findall(rawStr,tmp)
            print(tmp, positions)
            if rule==2:
                totalM -= 3*len(positions)
            else:
                totalM -=1*len(positions)
    return totalR-totalM

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
        performTests(2015, 8, [12], main, test=["1"])
    else:
        dif = getAnswer(2015, 8, main)
        print("The difference between number of characters of code and characters in memory is {0}".format(dif))

'''
Wrong: 1387, 1380, 1146, 1378, 1335, 1341
'''