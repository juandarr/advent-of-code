from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

class Node():
    def __init__(self,value):
        self.value = value
        self.next:Node | None = None
    def __repr__(self):
        return f"Node({self.value})"

class LinkedList():
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
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
        newNode = Node(value)
        if self.head == None or self.tail == None:
            self.head: Node | None = newNode
            self.tail: Node | None = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    row = str.split('\n')
    data = row[0].split(',')
    return data[1].split(' '),int(data[0])

def calculateMultiplicity(value, horizon):
    ll = LinkedList()
    ll.append(value)
    valuesprod = {}
    valuesdiv = {}
    values = {}
    for i in range(1,horizon+1):
        node = ll.head
        while node is not None:
            if node.value == 0:
                node.value = 1
                if i==horizon:
                    if 1 in values:
                        values[1]+=1
                    else:
                        values[1]=1
            elif len(str(node.value))%2==0:
                if node.value in valuesdiv:
                    val1,val2 = valuesdiv[node.value]
                else:
                    s = str(node.value)
                    size = len(s)
                    val1 = int(s[0:size//2])
                    val2 = int(s[size//2:size])
                    valuesdiv[node.value] = (val1,val2)
                if i==horizon:
                    if val1 in values:
                        values[val1]+=1
                    else:
                        values[val1]=1
                    if val2 in values:
                        values[val2]+=1
                    else:
                        values[val2]=1
                next = node.next
                node.value = val1
                newnode = Node(val2)
                node.next = newnode
                newnode.next = next
                node = newnode
                ll.length += 1
                if next==None:
                    ll.tail=newnode
            else:
                if node.value in valuesprod:
                    node.value = valuesprod[node.value]
                else:
                    tmp = node.value 
                    node.value *= 2024
                    valuesprod[tmp]= node.value
                if i==horizon:
                    if node.value in values:
                        values[node.value]+=1
                    else:
                        values[node.value]=1
            node = node.next
    return (values, ll.length)

def traverseList(l):
    newSeries = {}
    for str_v in l:
        v = int(str_v)
        if v in newSeries:
            newSeries[v]+=1
        else:
            newSeries[v] = 1
    counter = 0
    history = {}
    for i in range(25):
        series = dict(newSeries)
        newSeries = {}
        tmp = 0
        for s in series:
            tmp += series[s]
        counter = 0
        for v in series:
            if v in history:
                values, length = history[v]
            else:
                values, length = calculateMultiplicity(v, 3)
                history[v]=(values, length)
            counter += length*series[v]
            for k in values:
                if k in newSeries:
                    newSeries[k] += values[k]*series[v]
                else:
                    newSeries[k] = values[k]*series[v]
    return counter

def main(filename):
    l, _ = parseInformation(filename)
    score= traverseList(l)
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