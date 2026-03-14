from os.path import dirname, abspath
import sys
import time 

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    data = {}
    data['designs']= []
    data['patterns']=set()
    r = 0
    for row in rows:
        if row=='':
            r +=1
            continue
        if r>=1:
            data['designs'].append(row)
            r += 1
        else:
            tmp = row.split(', ')
            for p in tmp:
                data['patterns'].add(p)
    return (data['designs'], data['patterns'])

def explorePatterns(idx, maxSpan, design, patterns, memo):
    if idx==len(design):
        return True
    if idx in memo:
        return memo[idx]
    out = False
    for iSpan in range(idx+1,idx+maxSpan+1): 
        if iSpan>len(design):
            break
        if design[idx:iSpan] in patterns:
            out = out or explorePatterns(iSpan, maxSpan, design, patterns,memo)
            if out:
                break
    memo[idx]=out
    return out

def possibleDesigns(data):
    designs, patterns = data
    possibles = 0
    maxSpan = 0
    for p in patterns:
        if maxSpan < len(p):
            maxSpan = len(p)
    for d in designs:
        memo = {}
        if explorePatterns(0,maxSpan, d, patterns,memo):
            possibles+=1
    return possibles

def main(filename):
    data = parseInformation(filename)
    out = possibleDesigns(data)
    return out

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 19, [6],main) 
    else:
        out = getAnswer(2024, 19, main)
        print("The number of possible designs is: {0}".format(out))