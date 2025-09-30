from os.path import dirname, abspath
import sys
import hashlib

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    strs = data.rstrip().split('\n')
    return strs


def getNiceStrs(strs):
    niceNumber = 0
    for str in strs:
        idxStart = 0
        hasRepetition = False
        while (idxStart < len(str)-3):
            prev = str[idxStart:idxStart+2]
            idx = idxStart+2 
            while (idx < len(str)-1):
                if str[idx:idx+2]==prev:
                    hasRepetition = True
                    break
                idx+=1  
            if hasRepetition:
                break
            else:
                idxStart+=1
        if hasRepetition:
            pass
        else:
            continue
        hasPattern = False
        idx = 0
        while (idx < len(str)-2):
            reference = str[idx]
            if reference==str[idx+2]:
                hasPattern=True
                break
            idx +=1
        if hasPattern:
            niceNumber +=1
    return niceNumber

def main(filename):
    strs = parseInformation(filename)
    niceNumber = getNiceStrs(strs)
    return niceNumber

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 5, [2, 1], main, test=["2","3"])
    else:
        code = getAnswer(2015, 5, main)
        print("The number of nice strings is {0}".format(code))

