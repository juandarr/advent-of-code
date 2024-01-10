def parseInformation(filename):
    file = open(filename, "r")
    games = file.read()
    games = games.rstrip().split('\n')
    return games

def checkGames(games):
    scoreChoice = {'X':1,'Y':2,'Z':3, 'A':1, 'B':2, 'C':3}
    # Encodes winning results: 0 means draw, 1 means player 1 wins, 2 player 2 wins. Second
    # Value of the tuple is the score added for such result
    possibleResults = {'A X':(0,3),'A Y':(2,6),'A Z':(1,6),'B X':(1,6),'B Y':(0,3),'B Z':(2,6),'C X':(2,6),'C Y':(1,6),'C Z':(0,3)}

    playerScore = [0,0] 
    print(games)
    for game in games:
        # If draw add value to both players
        if possibleResults[game][0]==0:
            for idx in range(len(playerScore)):
                playerScore[idx] += possibleResults[game][1]
        # Else add value to the winner
        else:
            playerScore[possibleResults[game][0]-1] += possibleResults[game][1]
        singleHand= game.split(' ')
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