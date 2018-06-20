""" Naive Solution
    Colutational comlextiy i O(N**3)

    Need to add memoization
"""

def is_divisible(x, y):
    """ checks if x is divisible by y"""
    result = float(x) / y == x // y
    if result:
        return True
    return False

def find_next(l, i, n):
    """iterate through remaining list to finde subsequent members triple"""
    if n == 3:
        return 1

    count = 0
    end = len(l) - (2 - n)
    for j in range(i+1, end):
        if is_divisible(l[j], l[i]):
            count += find_next(l, j, n+1)
    return count

def answer(l):
    count = 0
    l = sorted(l)
    for i in range(len(l) - 2):
        count += find_next(l, i, 1)
    return count

def test():
    l = [1, 2, 3, 4, 5, 6]
    s = answer(l)
    print "%s -> %d" % (str(l), s)
    assert s == 3

if __name__ == "__main__":
    test()
