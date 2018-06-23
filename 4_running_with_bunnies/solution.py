def answer(times, time_limit):
    # your code here
    return []

def test(expect, m, time_limit):
    s = answer(m, time_limit)
    print "PASS " if s == expect else "FAIL ",
    print "%d / %s -> %d" % (time_limit, str(m), s)


if __name__ == "__main__":
    test([1, 2], [
            [0, 2, 2, 2, -1],
            [9, 0, 2, 2, -1],
            [9, 3, 0, 2, -1],
            [9, 3, 2, 0, -1],
            [9, 3, 2, 2,  0],
        ], 1)
