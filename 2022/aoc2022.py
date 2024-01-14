import sys
from subprocess import Popen

if __name__=='__main__': 
    args = sys.argv[1:]    
    if len(args)>1:
        print('This script requires only one argument: the day (d) and the challenge (c) in format "d.c"') 
    else:
        tmp =  args[0].split('.')
        if len(tmp)!=2:
            print('This script requires format: "c.d", where d is the day and c the challenge') 
        else:
            day = int(tmp[0])    
            challenge = int(tmp[1])
            proc = Popen([sys.executable, "day{0}/day{0}-{1}.py".format(day, challenge)])
            return_value = proc.wait()  # this call blocks until the program has been finishedimport sys