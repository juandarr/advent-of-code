filePairs = open('day4.txt', 'r')
pairs = filePairs.readlines()

overlap = 0

for pair in pairs:
    pair = pair.strip('\n')
    elfs = pair.split(',')
    for idx, elf in enumerate(elfs):
        elf = elf.split('-')
        elfs[idx] = [int(elf[0]), int(elf[1])]
    if ((elfs[0][0] >= elfs[1][0] and elfs[0][1] <= elfs[1][1]) or
            (elfs[1][0] >= elfs[0][0] and elfs[1][1] <= elfs[0][1])):
        overlap += 1
print("The number of overlaps in work assignments is {0}".format(overlap))
