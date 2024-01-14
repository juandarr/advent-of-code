from os.path import join,dirname

def performTests( day, answers, fn, args): 
    dir = dirname(__file__)
    passed= 0
    for idx,ans in enumerate(answers):
        filename = "day{0}-test{1}-input.txt".format(day,idx+1)
        filename = join(dir,'day{0}'.format(day),filename)
        res = fn(filename,*args) 
        if res==ans:
            passed += 1
            print('T.{0}: Correct answer, got {1}'.format(idx+1,res))
        else:
            print('T.{0}: Wrong answer, should be {1}, got {2} instead'.format(idx+1,ans,res))
    print('{0} of {1} tests PASSED'.format(passed, len(answers)))