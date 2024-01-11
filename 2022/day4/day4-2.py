filePairs = open('day4.txt','r')
pairs= filePairs.readlines()

overlap = 0 

for pair in pairs:
    pair = pair.strip('\n')
    elfs = pair.split(',')
    for idx,elf in enumerate(elfs):
        elf=elf.split('-')
        elfs[idx]=[int(elf[0]), int(elf[1])]
    if not((elfs[0][0]<elfs[1][0] and elfs[0][1]<elfs[1][0]) or (elfs[0][0]>elfs[1][1] and elfs[0][1]>elfs[1][1])):
        overlap += 1
        print(elfs)
print("The number of overlaps in work assignments is {0}".format(overlap))
