""" Iterative solution
"""

def answer(n):
    # start at desired state
    state = int(n)
    moves = 0

    while state > 1:
        # if even, divide
        if state % 2 == 0:
            state /= 2
        else:
            # determine number of times each border state can be divided
            sdown = state - 1
            sdown_div = 0
            while sdown % 2 == 0:
                sdown /= 2
                sdown_div += 1
                
            sup = state + 1
            sup_div = 0
            while sup % 2 == 0:
                sup /= 2
                sup_div += 1

            if sdown == 1 and sup != 1:
                state = 1
                moves += sdown_div
            elif sup == 1 and sdown != 1:
                state = 1
                moves += sup_div
            elif sup == 1 and sdown == 1 and sup_div < sdown_div:
                state = 1
                moves += sup_div
            elif sup == 1 and sdown == 1:
                state = 1
                moves += sdown_div
            elif sup_div > sdown_div:
                state += 1
            else:
                state -= 1
        moves += 1
    return moves


def test(expect, i):
    s = answer(i)
    print "PASS " if s == expect else "FAIL ",
    print "%s -> %d" % (i, s)


if __name__ == "__main__":
    test(0, "1")
    test(1, "2")
    test(2, "3")
    test(2, "4")
    test(5, "15")
    test(5, "20")
    test(6, "21")
