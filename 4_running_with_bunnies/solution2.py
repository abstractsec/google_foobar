""" Rescue as many bunnies as possible

    This is a graph problem where you start at the initital node and want to visit the maximum
    number of unique inner nodes, while still reaching the final node before your timer expires.
    The cost of traveling from one node to another is asymmetric and may be negative (increasing
    your timer)

    This solution is less efficient that the previous one, becuase it evaluates all permutations
    of a given 

    Passing 9/10 tests
"""
import itertools

def validate_path(times, path, ttl):
    """validate that the given path between stages can be visited in the given ttl
    """
    full_path = [p for p in path] + [len(times)-1]

    prev = 0
    path_cost = 0
    for s in full_path:
        path_cost += times[prev][s]
        prev = s

    return ttl >= path_cost

def optimize_graph(times):
    """ implementation of floyd-warshall to find shortest path from node to node
    """
    dist = times
    verticies = len(times)
    for k in range(verticies):
        for i in range(verticies):
            for j in range(verticies):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def answer(times, time_limit):
    """ Determine which nodes you can use to visit the maximum number of unique in nodes
    """
    target = len(times) - 1
    optimal_times = optimize_graph(times)
    ttl = time_limit

    # visit as manny inner nodes as possible before timer expires
    path = []
    bunnies = range(1, target)
    for cnt in bunnies:
        this_path = None
        for p in itertools.permutations(bunnies, cnt):
            p_sorted = [x-1 for x in sorted(p)]
            if (not this_path or this_path > p_sorted) and validate_path(optimal_times, p, ttl):
                this_path = p_sorted
        if this_path:
            path = this_path

    return path


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

    test([0], [
        [0, 2, 2, -1],
        [9, 0, 8, 1],
        [9, 8, 0, 1],
        [9, 1, 1, 0]
        ], 1)
