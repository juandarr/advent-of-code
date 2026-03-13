from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    data = {}
    data['registers']= {}
    data['instructions']=[]
    keys = ['A','B','C']
    r = 0
    for row in rows:
        if row=='':
            continue
        tmp = row.split(': ')
        if r<=2:
            data['registers'][keys[r]] = int(tmp[1])
            r += 1
        else:
            tmp = tmp[1].split(',')
            data['instructions']=[int(i) for i in tmp]
    return data

def runComputer():
    targetValues = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]

    def expansion(index, curA)-> int | None:
        if index < 0:
            return curA
        for offset in range(8):
            a = (curA << 3) | offset
            if a==0:
                continue 
            b = a%8
            b = b^1
            c = a>>b
            b = b^c
            b = b^6
            out = b%8

            if out==targetValues[index]:
                result = expansion(index-1, a)
                if result is not None:
                    return result
        return None
    return expansion(len(targetValues)-1, 0)


def main(filename):
    params = parseInformation(filename)
    out= runComputer()
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
        performTests(2024, 17, [117440],main, test=["2"]) 
    else:
        out = getAnswer(2024, 17, main)
        print("The output after running the instructions is: {0}".format(out))