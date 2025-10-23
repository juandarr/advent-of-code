from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    rows = [row.split(' ') for row in data.rstrip().split('\n')]
    return rows[0] 

def passwordValidity(seqRev, password):
    passRule1 = False
    i = 0
    while (i<len(password)-3):
        if seqRev[password[i]]-seqRev[password[i+1]]==1 and seqRev[password[i+1]]-seqRev[password[i+2]]==1:
            passRule1= True
            break 
        i += 1
    if not(passRule1):
        return False

    passRule2 = True
    bannedLetters = ['i','o','l']
    t = set(password)
    for c in t:
        if c in bannedLetters:
            passRule2 = False
            break
    if not(passRule2):
        return False


    passRule3 = False
    pairs = 0
    i = 0
    while (i<len(password)-2):
        if seqRev[password[i]]==seqRev[password[i+1]]:
            pairs += 1
            if pairs == 2:
                passRule1= True
                break 
            i += 2
        else:
            i += 1
    if not(passRule3):
        return False
    return True



def passwordSequence(data):
    seq = {}
    seqRev = {}
    for i in range(97,150):
        c = chr(i)
        seq[i-97]=c
        seqRev[c]=i-97
        if c=='z':
            break
    print(seq)
    p1 = 'abcdffaa'
    val = passwordValidity(seqRev,p1)
    p2 = 'ghjaabcc'
    val2 = passwordValidity(seqRev, p2)
    print(p1,val,p2,val2)
    return 0

def main(filename):
    data = parseInformation(filename)
    password = passwordSequence(data)
    return password

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 11, ['abcdffaa','ghjaabcc'], main, test=[])
    else:
        iterations = getAnswer(2015, 11, main)
        print("Given current Santa's password next password is {0}".format(iterations))