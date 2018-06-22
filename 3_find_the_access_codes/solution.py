""" Recursive Solution
    Compute: O(n**3)
    Memory: O(n)
    Fails due to timeout 
"""

# memoization cache
mem = {}

def is_divisible(x, y):
    """ checks if x is divisible by y"""
    return x >= y and float(x) / y == x // y


def find_next(l, i, n, state):
    """recurse through remaining list to finde subsequent members triple"""
    if n == 3:
        # print state
        return 1
    if i >= len(l):
        return 0

    count = 0
    end = len(l) - (2 - n)
    for j in range(i+1, end):
        # print state + " ? " + str(l[j])
        if is_divisible(l[j], l[i]):
            if (j, n+1) not in mem:
                mem[(j, n+1)] = find_next(l, j, n+1, state + ", %d" % l[j])
            count += mem[(j, n+1)]
            # count += find_next(l, j, n+1, state + ", %d" % l[j])
    return count


def answer(l):
    mem.clear()
    count = 0
    l = sorted(l)
    # print str(l)
    # iterate over each potential starting point
    for i in range(len(l) - 2):
        count += find_next(l, i, 1, str(l[i]))
    return count


def test(expect, l):
    s = answer(l)
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
    test(2, [1, 2, 7, 4, 5, 6])
    test(5, [1, 2, 4, 5, 6, 8])
    test(16, [4, 21, 7, 14, 56, 8, 56, 4, 42])
    test(10, [4, 21, 7, 14, 8, 56, 56, 42])
    test(4, [4, 7, 14, 8, 21, 56, 42])
