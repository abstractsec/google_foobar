def is_infinite(x, y):
    """ Determind is the pair will play indefinitly
    """
    # sort x and y such that x < y
    (x, y) = (x, y) if x < y else (y, x)
    while x != y:
        # x wins while x < y
        y -= x
        x *= 2

        # if the numbers x becomes larger than y, we will keep playing indefitely
        if x > y:
            return True
    return False

def answer(banana_list):
    """ With the given banana counts, determine how many guards will not be paired off indefinitly
    """
    guards = len(banana_list)
    # find combinations that will play infinitley
    paired = ()
    for i in range(guards-1):
        if i in paired:
            continue
        x = int(banana_list[i])
        for j in range(i+1, guards):
            if j in paired:
                continue
            y = int(banana_list[j])
            if is_infinite(x, y):
                paired += (i, j)
                break

    # calculate the number of unpaired guards
    return guards - len(paired)


def test(expect, l):
    s = answer(l)
    print "PASS " if s == expect else "FAIL ",
    print "%s -> %d" % (str(l), s)


if __name__ == "__main__":
    test(1, [1])
    test(2, [1, 1])
    test(0, [1, 7, 3, 21, 13, 19])
    test(1, [3, 3, 2, 6, 6])
    test(0, [1, 2, 1, 7, 3, 21, 13, 19])
