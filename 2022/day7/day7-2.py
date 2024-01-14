from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer

def parseInformation(filename):
    file = open(filename, "r")
    tmp= file.read()
    tmp= tmp.rstrip().split('\n')
    return tmp

def folderTree(commandStream):
    currentDirectory = ''
    parent = ''
    tree = {}
    idx = 0 
    for command in commandStream:
        command = command.split(' ')
        if command[0]=='$':
            if command[1]=='cd':
                if command[2]=='..':
                    currentDirectory = parent
                    parent = tree[currentDirectory]['parent'] 
                else:
                    parent = currentDirectory
                    currentDirectory = (command[2],idx)
                    idx +=1
                    tree[currentDirectory]= {'parent':parent, 'size':0, 'children':[]}
                    if parent!='':
                        tree[parent]['children'].append(currentDirectory)
        else:
            if command[0]=='dir':
                continue
            else:
                tree[currentDirectory]['children'].append((command[1],int(command[0])))
                tree[currentDirectory]['size'] += int(command[0])
                tmp = tree[currentDirectory]['parent']
                while (tmp != ''):
                    tree[tmp]['size']+= int(command[0])
                    tmp = tree[tmp]['parent']
    return tree

def spaceFreed(tree):
    freeSpace=70000000-tree[('/',0)]['size']
    minValue = 70000000
    for k in tree:
        if (freeSpace+tree[k]['size']>30000000):
            if (tree[k]['size']<minValue):
                minValue = tree[k]['size']
    return minValue 

def main(filename):
    commands= parseInformation(filename)
    tree = folderTree(commands)
    minValue= spaceFreed(tree)
    return minValue

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(7,[24933642],main)
    else:
        ans = getAnswer(7,main)       
        print("A folder can be deleted  to get {0} of space, required to achieve at least 30M of free memory".format(ans))
