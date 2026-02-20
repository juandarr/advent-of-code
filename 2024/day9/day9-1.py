from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    storage_str = str.split('\n')
    return [int(d) for d in  list(storage_str[0])]

def checkSum(storage_dist):
    free = []
    files = []
    id = 0
    storage = [] 
    memory_idx = 0
    for idx,s in enumerate(storage_dist):
        if idx%2==0:
            for i in range(s):
                storage.append(id)
                files.append(memory_idx)
                memory_idx += 1
            id += 1
        else:
            for i in range(s):
                storage.append('.')
                free.append(memory_idx)
                memory_idx += 1
    idx_free = 0
    idx_file = len(files)-1
    while (idx_free < len(free)) and (idx_file>=0):
        storage[free[idx_free]] = storage[files[idx_file]]
        storage[files[idx_file]] = '.'
        idx_free += 1
        idx_file -= 1 
        if free[idx_free]> files[idx_file]:
            break
    cs = 0
    for idx, val in enumerate(storage):
        if val == '.':
            continue
        cs += val*idx
    return cs

def main(filename):
    storage= parseInformation(filename)
    total= checkSum(storage)
    return total

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 9, [60,1928],main)
    else:
        total = getAnswer(2024, 9, main)
        print("The checksum of the storage after compression is: {0}".format(total))