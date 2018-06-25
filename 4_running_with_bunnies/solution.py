""" Rescue as many bunnies as possible

    This is a graph problem where you start at the initital node and want to visit the maximum
    number of unique inner nodes, while still reaching the final node before your timer expires.
    The cost of traveling from one node to another is asymmetric and may be negative (increasing
    your timer)

    Assumes you can only bring 1 bunny to the bulkhead at a time

    Passes 5/10 tests

    Issues:
    - If different combinations of the same number of bunnies can be rescued, this returns the
      combination that leaves the most time at the end, not the combination with the lowest set
      of IDs
"""

def get_shortest_paths(start, times):
    """ implementation of Djikstra's algorithm to get shortest path to all other positions
    """
    unvisited = range(len(times))

    # start at first node
    current = start
    distances = {current: 0}
    visited = [current]
    unvisited.remove(current)

    # find shortest path to destination
    while unvisited:
        next_n = None
        min_dist = 10000000
        for neighbor in range(len(times)):
            if neighbor in visited:
                continue

            dist = times[current][neighbor]
            if dist < min_dist:
                min_dist = dist
                next_n = neighbor

            new_dist = distances[current] + dist
            if neighbor not in distances or distances[neighbor] > new_dist:
                distances[neighbor] = new_dist

        current = next_n
        visited.append(current)
        unvisited.remove(current)

    return distances

def answer(times, time_limit):
    """ Determine which nodes you can use to visit the maximum number of unique in nodes
    """
    target = len(times) - 1

    # determine the shortest path from the start and bulkhead to each bunny
    cost_from_start = get_shortest_paths(0, times)
    cost_from_bulkhead = get_shortest_paths(target, times)

    start_to_bunny_cost = []
    bunny_to_bulkhead_cost = []
    bulkhead_to_bunny_cost = []
    cost_map = {}
    for bunny in range(target - 1):
        start_to_bunny_cost.append(cost_from_start[bunny+1])
        bulkhead_to_bunny_cost.append(cost_from_bulkhead[bunny+1])

        # determine the shortest path from each bunny to the bulkhead
        bunny_cost = get_shortest_paths(bunny+1, times)
        bunny_to_bulkhead_cost.append(bunny_cost[target])

        # determine the cost to rescue each bunny and return to the bulkhead
        cost = bulkhead_to_bunny_cost[bunny] + bunny_to_bulkhead_cost[bunny]
        if cost in cost_map:
            cost_map[cost].append(bunny)
        else:
            cost_map[cost] = [bunny]

    # determine the total cost 

    # determine the first bunny to rescue by finding the sortest path to the bulkhead via a bunny
    #  this path could be via the bulkhead
    ttl = time_limit
    rescued = []
    rescue_cost = 1000
    bunny = -1
    for b in range(len(start_to_bunny_cost)):
        c = start_to_bunny_cost[b] + bunny_to_bulkhead_cost[b]
        if c <= ttl and c < rescue_cost:
            bunny = b
            rescue_cost = c
    if bunny == -1:
        return []

    rescued.append(bunny)
    ttl -= rescue_cost

    # Rescue as many more bunnies as you can
    for c in sorted(cost_map.keys()):
        for b in cost_map[c]:
            r = None
            if b not in rescued and ttl - c >= 0:
                ttl -= c
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

    test([0], [
        [0, 2, 2, -1],
        [9, 0, 8, 1],
        [9, 8, 0, 1],
        [9, 1, 1, 0]
        ], 1)
