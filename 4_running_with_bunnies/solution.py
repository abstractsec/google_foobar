""" Rescue as many bunnies as possible

    This is a graph problem where you start at the initital node and want to visit the maximum
    number of unique inner nodes, while still reaching the final node before your timer expires.
    The cost of traveling from one node to another is asymmetric and may be negative (increasing
    your timer)

    Passes 5/10 tests

    Issues:
    - Does not account for non-direct shortest paths
    - If different combinations of the same number of bunnies can be rescued, this returns the
      combination that leaves the most time at the end, not the combination with the lowest set
      of IDs
"""

def answer(times, time_limit):
    """ Determine which nodes you can use to visit the maximum number of unique in nodes
    """
    target = len(times) - 1
    cost = []
    cost_map = {}

    # determine the shortest path from the start to each bunny for the first move
    start_to_bunny_cost = []

    # determine the shortest path from each bunny to the bulkhead
    bunny_to_bulkhead_cost = []

    # determinethe shortest path from the bulkhead to each bunny
    bulkhead_to_bunny_cost = []

    # determine the minimum amount of time you need to get from the bulkhead to each bunny and back
    #  this fails if the fastest route from the bulhead to the bunny of vice versus is not a direct
    #  route. You need to reduce the times to get the actual shortest paths between nodes
    for b in range(1, target):
        c = times[target][b] + times[b][target]
        cost.append(c)
        if c in cost_map:
            cost_map[c].append(b-1)
        else:
            cost_map[c] = [b-1]
    print "Cost: Bulkhead -> Bunny N\n%s" % cost_map

    timer = time_limit
    pos = 0
    rescued = []
    # go to bulkhead
    timer -= times[pos][target]
    pos = target
    print "Went to bulkhead... (timer=%d)" % timer

    for c in sorted(cost_map.keys()):
        for b in cost_map[c]:
            if timer - c >= 0:
                print "Rescued Bunny %d... (timer=%d)" % (b, timer)
                timer -= c
                rescued.append(b)

    return sorted(rescued)

def test(expect, m, time_limit):
    expect = sorted(expect)
    s = answer(m, time_limit)
    print "PASS " if s == expect else "FAIL ",
    print "%d @ %s -> %s" % (time_limit, m, s)


if __name__ == "__main__":
    test([1, 2], [
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]
        ], 1)
