'''
In this problem we need to develop a sorting mechanism to classify a
given hand by its rank and value of its cards 
'''
cardValue = {'2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, 'T':10,'J':11, 'Q':12, 'K':13,'A':14}

def read_file(filename):
    return open(filename, "r")

def parseInformation(lines):
    hands = []
    for line in lines:
        tmp = line.strip().split()
        hands.append(tmp)
    return hands

def compareHands(hand1, hand2):
    for (index,h) in enumerate(hand1):
        if cardValue[h]>cardValue[hand2[index]]:
            return 1
        elif cardValue[h]<cardValue[hand2[index]]:
            return 2
        else: continue

def sortHands(hands):
    c = 0
    while (c<len(hands)-1):
        cInc = 0
        while (cInc < len(hands)-c-1):
            comp = compareHands(hands[cInc][0],hands[cInc+1][0])
            if comp==1:
                tmp = hands[cInc]
                hands[cInc] = hands[cInc+1]
                hands[cInc+1] = tmp
            cInc += 1
        c += 1
    return hands

if __name__=='__main__': 
    test = True
    if test:
        filename = "day7-test-input.txt"
    else:
        filename = "day7-1-input.txt"
    lines = read_file(filename)
    hands = parseInformation(lines)
    groups = {'5K':[], '4K':[], 'FH':[],'3K':[], '2P':[],'1P':[],'1K':[]}
    for hand in hands:
        l = len(set(hand[0]))
        if l==1:
            groups['5K'].append(hand)
        elif l==2:
            fh =True 
            for h in set(hand[0]):
                repetition = 0
                for tmp in hand[0]:
                    if h==tmp:
                        repetition += 1
                if repetition == 4:
                    fh = False 
                    break
            if fh:
                groups['FH'].append(hand)
            else:
                groups['4K'].append(hand)
        elif l==3:
            pair =True 
            for h in set(hand[0]):
                pairCounter = 0
                for tmp in hand[0]:
                    if h==tmp:
                        pairCounter += 1
                if pairCounter == 3:
                    pair = False 
                    break
            if pair:
                groups['2P'].append(hand)
            else:
                groups['3K'].append(hand)
        elif l==4:
            groups['1P'].append(hand)
        else:
            groups['1K'].append(hand)
    rankHands =['1K','1P','2P','3K','FH','4K','5K']
    for rank in rankHands:
        hands = groups[rank]
        groups[rank] = sortHands(hands)  
    c = 1
    net =0
    for rank in rankHands:
        for hand in groups[rank]:
            net += c * int(hand[1])
            c += 1
    print(net)