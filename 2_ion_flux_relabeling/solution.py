#                    31
#        15                       30
#    7        14           22            29
#  3   6   10    13     18     21     25     28
# 1 2 4 5 8  9 11  12 16  17 19  20 23  24 26  27

def get_children(node, level, height):
    right = node - 1
    left = right - (2**(height - level) - 1)
    return (left, right)

def locate(height, target):
    node = 2**height - 1
    if node == target:
        return -1
    level = 1
    (left, right) = get_children(node, level, height)
    while left != target and right != target:
        if target < left:
            node = left
        else:
            node = right
        level+=1
        (left, right) = get_children(node, level, height)

    return node

def answer(h, q):
    p = []
    for node in q:
        p.append(locate(h, node))
    return p
