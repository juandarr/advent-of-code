def read_file(filename):
    return open(filename, "r")

def parseInformation(line):
    tmp = line.split(':')
    game =  int(tmp[0].split(' ')[1])
    sets = tmp[1].strip().split(';') 
    values = {'red': 0,'green': 0, 'blue':0}
    for s in sets:
        balls = s.strip().split(',')
        for ball in balls:
            tmp = ball.strip().split(' ')
            if values[tmp[1]]<int(tmp[0]):
                values[tmp[1]] = int(tmp[0])
    return values['red']*values['blue']*values['green']


if __name__=='__main__': 
    lines = read_file("day2-1-input.txt")
    #linesTest = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red','Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    power = 0
    for line in lines:
        powerLocal = parseInformation(line)
        power += powerLocal
    print(power)