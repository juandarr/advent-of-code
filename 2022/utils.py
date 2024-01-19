from os.path import join, dirname
from time import time


def performTests(day, answers, fn):
    dir = dirname(__file__)
    passed = 0
    for idx, ans in enumerate(answers):
        filename = "day{0}-test{1}-input.txt".format(day, idx + 1)
        filename = join(dir, "day{0}".format(day), filename)
        t0 = time()
        res = fn(filename)
        t = time() - t0
        if res == ans:
            passed += 1
            print("T.{0}: Correct answer, got {1}".format(idx + 1, res))
        else:
            print(
                "T.{0}: Wrong answer, should be {1}, got {2} instead".format(
                    idx + 1, ans, res
                )
            )
        print("    Running time: {0:7.6f} secs".format(t))
    print("Results: {0} of {1} tests PASSED".format(passed, len(answers)))


def getAnswer(day, fn):
    dir = dirname(__file__)
    filename = "day{0}-input.txt".format(day)
    filename = join(dir, "day{0}".format(day), filename)
    t0 = time()
    res = fn(filename)
    t = time() - t0
    print("    Running time: {0:7.6f} secs".format(t))
    return res
