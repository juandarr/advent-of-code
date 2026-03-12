from os.path import dirname, abspath
import sys
import heapq

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

def runComputer(params):
    regs = params['registers']
    ins = params['instructions']
    ptr = 0
    labels = ['A','B','C']
    out = ''
    while ptr<len(ins):
        i = ins[ptr]
        op = ins[ptr+1]
        combOp = op if op<=3 else regs[labels[op-4]]
        jump = False
        match i:
            case 0:
                regs['A'] = regs['A']//(2**combOp)
            case 1:
                regs['B'] = regs['B']^op
            case 2:
                regs['B']= combOp%8
            case 3:
                if regs['A']==0:
                    pass
                else:
                    ptr = op
                    jump = True
            case 4:
                regs['B'] = regs['B']^regs['C']
            case 5:
                tmp = combOp%8
                if out!='':
                    out+=','
                out+=str(tmp)
            case 6:
                regs['B'] = regs['A']//(2**combOp)
            case 7:
                regs['C'] = regs['A']//(2**combOp)
        if not(jump):
            ptr += 2
    return out

def main(filename):
    params = parseInformation(filename)
    out= runComputer(params)
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
        performTests(2024, 17, ['4,6,3,5,6,3,5,2,1,0'],main) 
    else:
        out = getAnswer(2024, 17, main)
        print("The output after running the instructions is: {0}".format(out))