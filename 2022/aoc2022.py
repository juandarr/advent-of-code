import sys
from subprocess import Popen

if __name__=='__main__': 
    args = sys.argv[1:]    
    if len(args)>2:
        print('This script requires two arguments: the day (d) and the challenge (c) in format "d.c" and whether to call "test" or "main" input files') 
    else:
        tmp =  args[0].split('.')
        if len(tmp)!=2:
            print('This script requires format: "c.d", where d is the day and c the challenge') 
        else:
            day = int(tmp[0])    
            challenge = int(tmp[1])
            proc = Popen([sys.executable, "day{0}/day{0}-{1}.py".format(day, challenge), args[1]])
            return_value = proc.wait()  # this call blocks until the program has been finished