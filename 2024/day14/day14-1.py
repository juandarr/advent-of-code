from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    params = {'robots':[]}
    params['dims'] = [int(i) for i in rows[0].split(' ')]
    for row in rows[1:]:
        robot= []
        tmp = row.split(' ')
        pos = tmp[0].split('=')[1].split(',')
        vel = tmp[1].split('=')[1].split(',')
        robot.append([int(i) for i in pos])
        robot.append([int(i) for i in vel])
        params['robots'].append(robot)
    return params

def securityFactor(params, seconds):
    with open("trees.txt", "a") as f:
        f.write("Now the file has more content!")
    positions = {}
    for robot in params['robots']:
        pos = robot[0]
        vel = robot[1]
        newPos = ((pos[1]+vel[1]*seconds)%params['dims'][1], (pos[0]+vel[0]*seconds)%params['dims'][0])
        if newPos in positions:
            positions[newPos]+=1
        else:
            positions[newPos] = 1
    mid_i= params['dims'][1]//2
    mid_j = params['dims'][0]//2
    quadrants = [[[0,mid_i-1],[0,mid_j-1]],[[0,mid_i-1],[mid_j+1,params['dims'][0]-1]],
[[mid_i+1, params['dims'][1]-1],[0,mid_j-1]],[[mid_i+1, params['dims'][1]-1],[mid_j+1,params['dims'][0]-1]]]
    total = 1 
    for q in quadrants:
        factor = 0
        toDel = []
        for p in positions:
            if p[0]>=q[0][0] and p[0]<=q[0][1] and p[1]>=q[1][0] and p[1]<=q[1][1]:
                factor += positions[p]
                toDel.append(p) 
        total *= factor
        for d in toDel:
            del positions[d]
    return total

def main(filename):
    params = parseInformation(filename)
    seconds = 100 
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
        print("The security factor for the given configuration is: {0}".format(sf))