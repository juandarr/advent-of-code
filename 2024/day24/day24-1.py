from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    values = {}
    ops = {}
    i = 0
    for row in rows:
        if row=='':
            i+=1
            continue
        if i==0:
            tmp = row.split(': ')
            values[tmp[0]] = int(tmp[1])
        else:
            tmp = row.split(' ')
            ops[tmp[-1]]=[tmp[0],tmp[1],tmp[2]]
    return values,ops 

def retrieveSignals(values,ops):
    while ops:
        toDel = []
        for op in ops:
            l = ops[op]
            if l[0] in values and l[2] in values:
                tmp = None
                if l[1]=='AND':
                    tmp = values[l[0]] and values[l[2]]
                elif l[1]=='OR':
                    tmp = values[l[0]] or values[l[2]]
                elif l[1]=='XOR':
                    tmp = values[l[0]] ^ values[l[2]]
                values[op]= tmp
                toDel.append(op)
        for op in toDel:
            del ops[op]
    i = 0
    decimal = 0
    while True:
        key = 'z'+(str(i) if i>=10 else '0'+str(i))
        if key in values:
            decimal += (2**i)*values[key]
        else:
            break
        i+=1
    return decimal 


def main(filename):
    values,ops = parseInformation(filename)
    out= retrieveSignals(values,ops)
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
        performTests(2024, 24, [2024],main) 
    else:
        val = getAnswer(2024, 24, main)
        print("The decimal number retrieves from the values of z bits is {0}".format(val))