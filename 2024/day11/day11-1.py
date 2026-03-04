from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

class Node():
    def __init__(self,value):
        self.value = value
        self.next: Node | None = None
    def __repr__(self):
        return f"Node({self.value})"

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    def append(self, value):
        node = Node(value)
        if self.head == None or self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    row = str.split('\n')
    data = row[0].split(',')
    return data[1].split(' '),int(data[0])

def traverseList(l, rep):
    ll = LinkedList()
    for v in l:
        ll.append(int(v))
    valuesProd = {}
    valuesDiv = {}
    for i in range(1,rep+1):
        node = ll.head
        while node is not None:
            if node.value == 0:
                node.value = 1
            elif len(str(node.value))%2==0:
                if node.value in valuesDiv:
                    val1,val2 = valuesDiv[node.value]
                else:
                    s = str(node.value)
                    size = len(s)
                    val1 = int(s[0:size//2])
                    val2 = int(s[size//2:size])
                    valuesDiv[node.value] = (val1,val2)
                next = node.next
                node.value = val1
                newNode = Node(val2)
                node.next = newNode
                newNode.next = next
                node = newNode
                ll.length += 1
                if next==None:
                    ll.tail = newNode 
            else:
                if node.value in valuesProd:
                    node.value = valuesProd[node.value]
                else:
                    tmp = node.value 
                    node.value *= 2024
                    valuesProd[tmp]= node.value
            node = node.next
    return ll.length

def main(filename):
    l, rep = parseInformation(filename)
    score= traverseList(l, rep)
    return score

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 11, [22,55312,7],main) 
    else:
        totalStones = getAnswer(2024, 11, main)
        print("The number of stones after bliking n times is: {0}".format(totalStones))