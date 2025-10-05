from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    wirings = [s.split(' ') for s in data.rstrip().split('\n')]
    return wirings

def computeWirings(wirings):
    d = {}
    idx = len(wirings)-1
    while (idx >= 0):
        w = wirings[idx]
        if len(w)==3:
            if w[0].isdigit():
                if w[2]=='b':
                    d[w[2]] = 3176
                wirings.pop(idx)
        idx -=1
    while len(wirings)>0:
        print(wirings)
        idx = len(wirings)-1
        while (idx >= 0):
            w = wirings[idx]
            if len(w)==3:
                if w[0] in d:
                    d[w[2]] = int(d[w[0]])
                    wirings.pop(idx) 
            elif len(w)==4:
                if w[1] in d:
                    v = ~d[w[1]]
                    d[w[3]] = 65536+v
                    wirings.pop(idx) 
            else:
                if w[0] in d or w[0].isdigit():
                    if w[1]=='RSHIFT':
                        d[w[4]] = d[w[0]] >>  int(w[2])
                        wirings.pop(idx) 
                    elif w[1]=='LSHIFT':
                        d[w[4]] = d[w[0]] << int(w[2])
                        wirings.pop(idx) 
                    else:
                        if w[2] in d:
                            if w[1]=='AND':
                                if w[0].isdigit():
                                    d[w[4]] = int(w[0]) & d[w[2]]
                                else:
                                    d[w[4]] = d[w[0]] & d[w[2]]
                            elif w[1]=='OR':
                                if w[0].isdigit():
                                    d[w[4]] = int(w[0]) | d[w[2]]
                                else:
                                    d[w[4]] = d[w[0]] | d[w[2]]
                            wirings.pop(idx) 
            idx -=1
    return d['a']


def main(filename):
    wirings = parseInformation(filename)
    signal = computeWirings(wirings)
    return signal

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 7, [65079], main)
    else:
        signal = getAnswer(2015, 7, main)
        print("The signal for wire a is {0}".format(signal))

