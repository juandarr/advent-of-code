from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests import performTests

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

def main(filename):
    games = parseInformation(filename)
    playerScore = checkGames(games)
    return playerScore[1]

if __name__=='__main__': 
    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2,[12],main,[])
    else:
        dir = dirname(__file__)
        filename = join(dir,'day2-input.txt')
        playerScore = main(filename)
        print("Score of player 2 {0}".format(playerScore))