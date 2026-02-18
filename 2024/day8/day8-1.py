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
    for freq in antenas:
        l = len(antenas[freq])
        for i in range(l):
            a = antenas[freq][i]
            for k in range(i+1,l):
                b = antenas[freq][k]
                dia = a[0]-b[0]
                dja = a[1]-b[1]
                nodes = [(a[0]+dia, a[1]+dja)]
                dib = b[0]-a[0]
                djb = b[1]-a[1]
                nodes.append((b[0]+dib, b[1]+djb))
                for node in nodes:
                    if node[0]>=0 and node[0]<iLimit and node[1]>=0 and node[1]<jLimit:
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
        performTests(2024, 8, [14,4],main)
    else:
        total = getAnswer(2024, 8, main)
        print("The number of unique antinode locations is: {0}".format(total))