def answer(banana_list):
    guards = len(banana_list)
    # find combinations that have an odd difference
    paired = []
    for i in range(len(banana_list)):
        if i in paired:
            continue
        x = banana_list[i]
        for j in range(i+1, len(banana_list)):
            y = banana_list[j]
            if (y-x) > 0 and (y-x) % 2 == 0:
                paired += [x, y]
                is_paired = True
                break
    
    # calculate the number of unpaired guards
    return guards - len(paired)


def test(expect, l):
    s = answer(l)
    print "PASS " if s == expect else "FAIL ",
    print "%s -> %d" % (str(l), s)


if __name__ == "__main__":
    test(2, [1, 1])
    test(0, [1, 7, 3, 21, 13, 19])
