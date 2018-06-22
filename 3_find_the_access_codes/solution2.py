""" Iterative Solution
    Compute: O(n**3)
    Memory: O(1)
    Fails due timeout
"""

def is_divisible(x, y):
    """ checks if x is divisible by y"""
    return x >= y and float(x) / y == x // y


def is_triplet(x, y, z):
    return is_divisible(z, y) and is_divisible(y, x)


def answer(l):
    l_size = len(l)
    count = 0
    for i in range(l_size - 2):
        for j in range(i+1, l_size - 1):
            for k in range(j+1, l_size):
                if is_triplet(l[i], l[j], l[k]):
                    count += 1
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
