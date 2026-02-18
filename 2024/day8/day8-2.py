from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    m = []
    for row in rows:
        m.append(list(row))
    antenas = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!='.':
                if m[i][j] in antenas:
                    antenas[m[i][j]].append((i,j))
                else:
                    antenas[m[i][j]] = [(i,j)]
    return m, antenas

def checkMap(m, antenas):
    antinodes = {}
    iLimit = len(m)
    jLimit = len(m[0])
    total = 0
    for freq in antenas:
        l = len(antenas[freq])
        if l>1:
            total += l
        for i in range(l):
            a = antenas[freq][i]
            if a not in antinodes:
                antinodes[a] = 1
            for k in range(i+1,l):
                b = antenas[freq][k]
                nodes = []
                dia = a[0]-b[0]
                dja = a[1]-b[1]
                c = 1
                node = (a[0]+dia, a[1]+dja)
                while node[0]>=0 and node[0]<iLimit and node[1]>=0 and node[1]<jLimit:
                    nodes.append(node)
                    c += 1
                    node = (a[0]+c*dia, a[1]+c*dja)
                dib = b[0]-a[0]
                djb = b[1]-a[1]
                c = 1
                node = (b[0]+dib, b[1]+djb)
                while node[0]>=0 and node[0]<iLimit and node[1]>=0 and node[1]<jLimit:
                    nodes.append(node)
                    c += 1
                    node = (b[0]+c*dib, b[1]+c*djb)
                for node in nodes:
                    if node not in antinodes:
                        antinodes[node] = 1
    return len(antinodes)

def main(filename):
    m,antenas= parseInformation(filename)
    locations= checkMap(m,antenas)
    return locations


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 8, [34,9],main, test=["1", "3"])
    else:
        total = getAnswer(2024, 8, main)
        print("The number of unique antinode locations is: {0}".format(total))