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

def passwordValidity(password):
    passRule1 = False
    i = 0
    while (i<len(password)-2):
        if password[i+1]-password[i]==1 and password[i+2]-password[i+1]==1:
            passRule1= True
            break 
        i += 1
    if not(passRule1):
        return False

    passRule2 = True
    bannedLetters = [ord('i'),ord('o'),ord('l')]
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
    while (i<len(password)-1):
        if password[i]==password[i+1]:
            pairs += 1
            if pairs == 2:
                passRule3= True
                break 
            i += 2
        else:
            i += 1
    if not(passRule3):
        return False
    return True

def incrementPassword(p):
    i = len(p)-1
    carry = 1
    while(carry==1 and i>=0):
        p[i]+= 1
        if p[i]==123:
            p[i]=97
            carry = 1
        else:
            carry = 0
        i-=1

def passwordSequence(data):
    # Starting value a=97, end value z=122
    s = [ord(i) for i in data[0]]
    while not(passwordValidity(s)):
        incrementPassword(s)
    key = [chr(i) for i in s]
    key = ''.join(key)
    return key 

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
        performTests(2015, 11, ['abcdffaa','ghjaabcc'], main)
    else:
        iterations = getAnswer(2015, 11, main)
        print("Given current Santa's password next password is {0}".format(iterations))