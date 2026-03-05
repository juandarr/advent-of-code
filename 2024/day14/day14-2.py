from os.path import dirname, abspath
import sys
import time

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    params = {'robots':[]}
    params['dims'] = [int(i) for i in rows[0].split(' ')][::-1]
    for row in rows[1:]:
        robot={} 
        tmp = row.split(' ')
        pos = tmp[0].split('=')[1].split(',')
        vel = tmp[1].split('=')[1].split(',')
        robot['pos']=tuple([int(i) for i in pos][::-1])
        robot['vel'] = tuple([int(i) for i in vel][::-1])
        params['robots'].append(robot)
    return params

def printMap(pos,dims,s):
    map = str(s)+' sec\n'
    #print(f'{s} sec')
    tree =False
    prev = False
    for i in range(dims[0]):
        c = 0
        row = ''
        for j in range(dims[1]):
            if (i,j) in pos:
                row+= str(pos[(i,j)])
                if prev==True:
                    c+=1
                prev=True
            else:
                row+=' '
                prev=False
        map += row+'\n'
        #print(row)
        if c>20:
            tree= True    
    map+='\n\n'
    #print(f'\n\n')
    if tree==True:
        print(map)
        return 1
    return 0

def securityFactor(params, seconds):
    base = 0
    for idx,robot in enumerate(params['robots']):
        pos = robot['pos']
        vel = robot['vel']
        new_pos =tuple([(pos[0]+vel[0]*base)%params['dims'][0], (pos[1]+vel[1]*base)%params['dims'][1]])
        params['robots'][idx] = {'pos' :new_pos, 'vel': vel} 
    tree_second = None
    for s in range(1,seconds+1):
        positions = {}
        for idx,robot in enumerate(params['robots']):
            pos = robot['pos']
            vel = robot['vel']
            new_pos =tuple([(pos[0]+vel[0])%params['dims'][0], (pos[1]+vel[1])%params['dims'][1]])
            params['robots'][idx] = {'pos' :new_pos, 'vel': vel} 
            if new_pos in positions:
                positions[new_pos]+=1
            else:
                positions[new_pos]=1
        out = printMap(positions, params['dims'],s)
        if out==1:
            tree_second = s
            break
        #time.sleep(0.01)
    return tree_second

def main(filename):
    params = parseInformation(filename)
    seconds = 20000
    sf = securityFactor(params,seconds)
    return sf

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 14, [12],main)
    else:
        sf= getAnswer(2024, 14, main)
        print("The second at which the easter egg appears is: {0}".format(sf))