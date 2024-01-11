def parseInformation(filename):
    file = open(filename, "r")
    games = file.read()
    games = games.rstrip().split('\n')
    return games

def checkGames(games):
    # Score added according the choice
    scoreChoice = {'A':1, 'B':2, 'C':3}
    # Encodes winning results: 0 means draw, 1 means player 1 wins, 2 player 2 wins. Second
    # Value of the tuple is the score added for such result
    possibleResults = {'AA':(0,3),'AB':(2,6),'AC':(1,6),'BA':(1,6),'BB':(0,3),'BC':(2,6),'CA':(2,6),'CB':(1,6),'CC':(0,3)}
    decryption = {'X':{'A':'C','B':'A','C':'B'},'Y':{'A':'A','B':'B','C':'C'},'Z':{'A':'B','B':'C','C':'A'}}

    playerScore = [0,0] 
    for game in games:
        singleHand = game.split(' ')
        singleHand[1]=decryption[singleHand[1]][singleHand[0]]
        hands = ''.join(singleHand)
        # If draw add value to both players
        if possibleResults[hands][0]==0:
            for idx in range(len(playerScore)):
                playerScore[idx] += possibleResults[hands][1]
        # Else add value to the winner
        else:
            playerScore[possibleResults[hands][0]-1] += possibleResults[hands][1]
        # Add value according to the player's choice 
        for idx in range(len(playerScore)):
            playerScore[idx] += scoreChoice[singleHand[idx]]
    return playerScore

if __name__=='__main__': 
    test = False
    if test:
        filename = "day2-test-input.txt"
    else:
        filename = "day2-input.txt"
    games = parseInformation(filename)
    playerScore = checkGames(games)
    print("Score of player 1 {0}, Score of player 2 {1}".format(playerScore[0], playerScore[1]))