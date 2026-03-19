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

def showValuesAndOps(values,ops,lims):
    i=0
    while True:
        key = 'z'+(str(i) if i>=10 else '0'+str(i))
        print(key)
        toVisit = [key]
        s=0
        while toVisit:
            tmp = []
            for k in toVisit:
                if k in ops:
                    if i>=lims[0]:
                        print(f'{k}: {ops[k]}')
                    s+=1
                    tmp.extend([ops[k][0], ops[k][2]])
                elif k in values:
                    s+=1
                    if i>lims[0]:
                        print(f'{k}: {values[k]}')
            toVisit = tmp
            if s>100:
                break
        i+=1
        print('')
        if i==lims[1]+1:
            break
    return

def increaseBinary(values, newValue, var):
    complete = False
    b = bin(newValue)
    for idx in range(45):
        if not complete:
            if b[-idx-1]=='b':
                complete=True
        if not complete:
            values[var+(str(idx) if idx>=10 else '0'+str(idx))]=int(b[-idx-1])
        else:
            values[var+(str(idx) if idx>=10 else '0'+str(idx))]=0
    return values

def getInteger(values, var):
    i = 1
    key = var+'00' 
    val = values[key]
    while key in values:
        key =  var+(str(i) if i>=10 else '0'+str(i))
        val +=  values[key]*(2**i)
        i+=1
        if i==45:
            break
    return val

def estimatedZ(values):
    i = 0
    zr = ''
    while True:
        keyZ = 'z'+(str(i) if i>=10 else '0'+str(i))
        if keyZ in values:
            zr = str(values[keyZ])+zr
        else:
            break
        i+=1
    return zr

def realZ(values):
    i = 0
    x = ''
    y = ''
    z = ''
    carry = 0
    while True:
        keyX = 'x'+(str(i) if i>=10 else '0'+str(i))
        keyY = 'y'+(str(i) if i>=10 else '0'+str(i))
        if keyY not in values:
            z += str(carry) 
            break
        x += str(values[keyX])
        y += str(values[keyY])
        if (carry,values[keyX], values[keyY])==(1,0,0) or (carry,values[keyX], values[keyY])==(0,0,1) or (carry,values[keyX], values[keyY])==(0,1,0):
            z+= '1'
            carry = 0
        elif (carry,values[keyX], values[keyY])==(1,0,1) or (carry,values[keyX], values[keyY])==(1,1,0) or (carry,values[keyX], values[keyY])==(0,1,1):
            z+= '0'
            carry = 1
        elif (carry,values[keyX], values[keyY])==(1,1,1):
            z+= '1'
            carry = 1
        else:
            z+= '0'
            carry = 0
        i+=1
    return z[::-1],x[::-1],y[::-1]
    
def retrieveSignals(values,ops):
    tmp = ops['z06']
    ops['z06'] = ops['jmq']
    ops['jmq']=tmp
    tmp = ops['z13']
    ops['z13'] = ops['gmh']
    ops['gmh']=tmp
    tmp = ops['z38']
    ops['z38'] = ops['qrh']
    ops['qrh']=tmp
    tmp = ops['rqf']
    ops['rqf'] = ops['cbd']
    ops['cbd']=tmp
    tmpValues = dict(values)
    tmpOps = dict(ops)

    ## This part gets the integer values from the binary numbers, the idea is to loop them
    ## and check whether the swaps work
    Xval= getInteger(values, 'x')
    Yval = getInteger(values, 'y')

    # Print values and operations registered per each bit output in z. Define limits to present between Zmin and Zmax
    #showValuesAndOps(values, tmpOps, [24,26])

    # Loop to verify viability of swaps
    for step in range(1,1000000000,100000):
        values = dict(tmpValues)
        # Increase Xval by step
        values = increaseBinary(values, Xval+step, 'x')
        # Increase Yval by step
        values = increaseBinary(values, Yval+step, 'y')
        # Start with a new copy of tmpOps (The one with swaped values)
        ops = dict(tmpOps)

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

        #Verify operations
        zEstimated =estimatedZ(values)
        zReal,x,y = realZ(values)
        print('\n '+x+f' -> X ({Xval+step})')
        print(' '+y+f' -> Y ({Yval+step})')
        print(zEstimated+' -> Expected')
        print(zReal+' -> Real')
        print(f'Same output? {zEstimated==zReal}')
        if zEstimated!=zReal:
            print(f'Number gave a different value! Increase: {step}')
            return
    return ','.join(sorted(['z06','jmq','z13','gmh','z38','qrh','rqf','cbd'])) 


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
        print("The swaped outputs that fix the addition calculator are {0}".format(val))