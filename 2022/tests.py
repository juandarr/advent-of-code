from os.path import join

def performTests(dir, day, answers, fn, args): 
    passed= 0
    for idx,ans in enumerate(answers):
        filename = "day{0}-test{1}-input.txt".format(day,idx+1)
        filename = join(dir,filename)
        
        res = fn(filename,*args) 
        if res==ans:
            passed += 1
        else:
            print('T.{0}: Wrong answer, should be {1}, got {2} instead'.format(idx+1,ans,res))
    print('{0} of {1} tests PASSED'.format(passed, len(answers)))