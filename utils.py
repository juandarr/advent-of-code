from os.path import join, dirname
from time import time


def performTests(year, day, answers, fn, *args, test=None):
    """
    This function perform tests for every `dayx-testy-input.txt` file defined. When test is None it will run and try to match
    every answer defined from the first possible test, `1`. If test is defined the tests as a list of tests (values as strings), the same number
    of answers is expected in a list.
    *args is used when more than the typical arguments are expected in the main function.
    """
    dir = dirname(__file__)
    passed = 0
    for idx, ans in enumerate(answers):
        fileIdx = ""
        if test is None:
            fileIdx = str(idx + 1)
        else:
            fileIdx = test[idx]
        filename = "day{0}-test{1}-input.txt".format(day, fileIdx)
        filename = join(dir, "{0}/day{1}".format(year, day), filename)
        t0 = time()
        res = fn(filename, *args)
        t = time() - t0
        if res == ans:
            passed += 1
            print("T.{0}: Correct answer, got {1}".format(fileIdx, res))
        else:
            print(
                "T.{0}: Wrong answer, should be {1}, got {2} instead".format(
                    fileIdx, ans, res
                )
            )
        print("    Running time: {0:7.6f} secs".format(t))
    print("Results: {0} of {1} tests PASSED".format(passed, len(answers)))


def getAnswer(year, day, fn, *args):
    dir = dirname(__file__)
    filename = "day{0}-input.txt".format(day)
    filename = join(dir, "{0}/day{1}".format(year, day), filename)
    t0 = time()
    res = fn(filename, *args)
    t = time() - t0
    print("    Running time: {0:7.6f} secs".format(t))
    return res
