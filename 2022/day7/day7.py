from deepdiff import DeepDiff

def folderTree(commandStream):
    currentDirectory = ''
    parent = ''
    tree = {}
    idx = 0 
    for command in commandStream:
        command = command.strip('\n').split(' ')
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


def test_folderTree():
    commands="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    commands = commands.split('\n')
    ans = {('/',0):{'parent':'', 'size':4060174+8033020+5626152+7214296+584+29116+2557+62596+14848514+8504156,'children':[('b.txt',14848514),('c.dat',8504156),('a',1),('d',3)]}, ('d',3):{'parent':('/',0), 'size':4060174+8033020+5626152+7214296,'children':[('j',4060174),('d.log',8033020),('d.ext',5626152),('k',7214296)]},('a',1):{'parent':('/',0), 'size':584+29116+2557+62596,'children':[('f',29116),('g',2557),('h.lst',62596),('e',2)]},('e',2):{'parent':('a',1), 'size':584,'children':[('i',584)]}}
    dif = DeepDiff(folderTree(commands),ans)
    assert dif=={},'Trees don\'t match: {0}'.format(dif)  
    print('Trees match, function works as expected')
    
if __name__ == '__main__':
    test_folderTree() 
    fileMessage = open('day7.txt','r')
    commands= fileMessage.readlines()
    tree = folderTree(commands)
    # Part 1 
    totalSize = 0
    limit = 100000
    for k in tree:
        if tree[k]['size']<=limit:
            totalSize += tree[k]['size']
     
    print("The sum of the total sizes of directories below {0} is {1}".format(limit,totalSize)) 
    # Part  2
    freeSpace=70000000-tree[('/',0)]['size']
    minValue = 70000000
    folder = ''
    for k in tree:
        if (freeSpace+tree[k]['size']>30000000):
            if (tree[k]['size']<minValue):
                minValue = tree[k]['size']
                folder = k
    print("The folder {0} can be deleted  to get {1} of space, required to achieve at least 30M of free memory".format(folder,minValue))
