def hiddenTrees(treeView):
    mainView = []
    for row in treeView:
        row = row.strip('\n')
        mainView.append(list(row))
    # scores
    maxScore = 0 
    for i in range(1,len(mainView)-1):
        for j in range(1,len(mainView[0])-1):
            score = 1
            height = int(mainView[i][j])    
            #left
            d = 0 
            for k in range(j-1,-1,-1):
                d +=1
                if height<=int(mainView[i][k]):
                    break
            score *= d
            #right
            d = 0 
            for k in range(j+1,len(mainView[0])):
                d +=1
                if height<=int(mainView[i][k]):
                    break
            score *= d
            #up
            d = 0 
            for k in range(i-1,-1,-1):
                d +=1
                if height<=int(mainView[k][j]):
                    break
            score *= d
            #down
            d = 0 
            for k in range(i+1,len(mainView)):
                d +=1
                if height<=int(mainView[k][j]):
                    break
            score *= d
            maxScore = max(maxScore, score)
    return maxScore 

def test_hiddenTrees():
    treeView="""30373
25512
65332
33549
35390"""
    treeView = treeView.split('\n')
    assert hiddenTrees(treeView)==8,'Highest scenic score don\'t  match'  
    print('Highest scenic scores match, test PASSED')
    
if __name__ == '__main__':
    test_hiddenTrees() 
    fileTreeView = open('day8.txt','r')
    treeView= fileTreeView.readlines()
    # Part 2 
    score = hiddenTrees(treeView)
    print("The highest scenic score is {0}".format(score))
