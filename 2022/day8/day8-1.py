def hiddenTrees(treeView):
    mainView = []
    for row in treeView:
        row = row.strip('\n')
        mainView.append(list(row))
    #Finding the blocking trees: [left-right, right-left,top-bottom,bottom-top]
    blockingHeight = []
    # Left to right
    for i in range(1,len(mainView)-1):
        tmp = []
        maxi = 0
        for j in range(1,len(mainView[0])-1):
            maxi = max(maxi,int(mainView[i][j-1]))
            tmp.append([maxi])
        blockingHeight.append(tmp)
    # Right to left
    for i in range(1,len(mainView)-1):
        maxi = 0
        for j in range(len(mainView[0])-1,1,-1):
            maxi = max(maxi,int(mainView[i][j]))
            blockingHeight[i-1][j-2].append(maxi) 
    # Top to bottom
    for j in range(1,len(mainView[0])-1):
        maxi = 0
        for i in range(1,len(mainView)-1):
            maxi = max(maxi,int(mainView[i-1][j]))
            blockingHeight[i-1][j-1].append(maxi) 
    # Bottom to top
    for j in range(1,len(mainView[0])-1):
        maxi = 0
        for i in range(len(mainView)-1,1,-1):
            maxi = max(maxi,int(mainView[i][j]))
            blockingHeight[i-2][j-1].append(maxi) 
    # Resolution
    visible = len(mainView)*2+(len(mainView[0])-2)*2 
    for i in range(1,len(mainView)-1):
        for j in range(1,len(mainView[0])-1):
            isBlocked = True
            for tmp in blockingHeight[i-1][j-1]:
                if tmp<int(mainView[i][j]):
                    isBlocked=False
                    break
            if not(isBlocked):
                visible += 1
    return visible 

def test_hiddenTrees():
    treeView="""30373
25512
65332
33549
35390"""
    treeView = treeView.split('\n')
    assert hiddenTrees(treeView)==21,'Number of visible trees don\'t  match'  
    print('Number of visible trees match, function works as expected')
    
if __name__ == '__main__':
    test_hiddenTrees()  
    fileTreeView = open('day8.txt','r')
    treeView= fileTreeView.readlines()
    # Part 1 
    visibleTrees = hiddenTrees(treeView)
    print("The number of visible trees is {0}".format(visibleTrees))
