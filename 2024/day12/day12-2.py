from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    return [list(row) for row in rows]

def calculatePrice(map):
    dirs = {'vr':(0,1), 'vl':(0,-1), 'hu':(-1,0), 'hd':(1,0)}
    regions = {}
    mapExplored = {}
    for i in range(len(map)):
        for j in range(len(map[0])):
            regionExplored = {}
            if (i,j) in mapExplored:
                continue
            t = map[i][j]
            area = 1
            toExplore = {(i,j)}
            points = {} 
            while toExplore:
                node = toExplore.pop()
                regionExplored[node]= 1
                mapExplored[node]=1
                for d in dirs:
                    new_i = node[0]+dirs[d][0]
                    new_j = node[1]+dirs[d][1]
                    if (new_i,new_j) in regionExplored or (new_i,new_j) in toExplore:
                        continue
                    if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]) or map[new_i][new_j]!=t:
                        if d in points:
                            points[d].append(node)
                        else:
                            points[d] = [node]
                        continue
                    if map[new_i][new_j]==t:
                        area += 1
                        toExplore.add(((new_i, new_j)))
            sides = 0
            for side in points:
                dims = {'vl':[(-1,0),(1,0)],'vr':[(-1,0),(1,0)],'hu':[(0,-1),(0,1)],'hd':[(0,-1),(0,1)]}
                points_set = set(points[side])
                while points_set:
                    start = points_set.pop()
                    toExpand = [start]
                    while toExpand:
                        point = toExpand.pop()
                        points_set.discard(point)
                        for dim in dims[side]:
                            newPoint = (point[0]+dim[0], point[1]+dim[1])
                            if newPoint in points_set:
                                toExpand.append(newPoint)
                    sides += 1
            if t in regions:
                regions[t].append((area,sides))
            else:
                regions[t] = [(area,sides)]
    total = 0
    for region in regions:
        for d in regions[region]:
            total += d[0]*d[1]
    return total

def main(filename):
    map = parseInformation(filename)
    price = calculatePrice(map)
    return price 

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 12, [80,436,1206,236,368],main) 
    else:
        price = getAnswer(2024, 12, main)
        print("The total price to fence the whole field is: {0}".format(price))