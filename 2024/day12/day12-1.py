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
    dirs = [(0,1), (0,-1), (-1,0), (1,0)]
    regions = {}
    mapExplored = {}
    for i in range(len(map)):
        for j in range(len(map[0])):
            regionExplored = {}
            if (i,j) in mapExplored:
                continue
            t = map[i][j]
            area = 1
            perimeter = 0
            toExplore = {(i,j)}
            while toExplore:
                node = toExplore.pop()
                regionExplored[node]= 1
                mapExplored[node]=1
                for d in dirs:
                    new_i = node[0]+d[0]
                    new_j = node[1]+d[1]
                    if (new_i,new_j) in regionExplored or (new_i,new_j) in toExplore:
                        continue
                    if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]) or map[new_i][new_j]!=t:
                        perimeter += 1
                        continue
                    if map[new_i][new_j]==t:
                        area += 1
                        toExplore.add(((new_i, new_j)))
            if t in regions:
                regions[t].append((area,perimeter))
            else:
                regions[t] = [(area,perimeter)]
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
        performTests(2024, 12, [140,772,1930],main)
    else:
        price = getAnswer(2024, 12, main)
        print("The total price to fence the whole field is: {0}".format(price))