""" Iterative solution
    Compute: O(n**2)
    Memory: O(n**2)
    Fails due to memory error
"""

def is_divisible(x, y):
    """ checks if x is divisible by y"""
    return x >= y and float(x) / y == x // y


def answer(l):
    l_size = len(l)

    # find all divisible pairs
    pairs = {}
    for i in range(l_size-1):
        for j in range(i+1, l_size):
            if is_divisible(l[j], l[i]):
                if i in pairs:
                    pairs[i].append((i, j))
                else:
                    pairs[i] = [(i, j)]

    #iterate over pairs to find triplets
    count = 0
    for k in sorted(pairs.keys()):
        for p in pairs[k]:
            j = p[1]
            if j in pairs:
                count += len(pairs[j])
    return count

def test(expect, l):
    s = answer(sorted(l))
    print "PASS " if s == expect else "FAIL ",
    print "%s -> %d" % (str(l), s)


if __name__ == "__main__":
    test(0, [1, 2])
    test(0, [1, 1])
    test(0, [2, 4])
    test(1, [1, 1, 1])
    test(1, [1, 2, 2])
    test(0, [1, 2, 3])
    test(1, [1, 2, 4])
    test(3, [1, 2, 3, 4, 5, 6])
    test(2, [1, 2, 4, 5, 6, 7])
    test(5, [1, 2, 4, 5, 6, 8])
    test(16, [4, 21, 7, 14, 56, 8, 56, 4, 42])
    test(10, [4, 21, 7, 14, 8, 56, 56, 42])
    test(4, [4, 7, 14, 8, 21, 56, 42])
