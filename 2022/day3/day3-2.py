fileSacks = open('day3.txt', 'r')
ruckSacks = fileSacks.readlines()

priorities = {}
p = 1
for i in range(97, 97+26):
    priorities[chr(i)] = p
    p += 1
for i in range(65, 65+26):
    priorities[chr(i)] = p
    p += 1

netPriorities = 0
items = []
for ruckSack in ruckSacks:
    ruckSack = ruckSack.strip('\n')
    items.append(set(ruckSack))
    if len(items) == 3:
        for a in items[0]:
            if a in items[1] and a in items[2]:
                netPriorities += priorities[a]
                break
        items = []

print("Addition of priorities is {0}".format(netPriorities))
