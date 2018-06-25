""" Rescue as many bunnies as possible

    This is a graph problem where you start at the initital node and want to visit the maximum
    number of unique inner nodes, while still reaching the final node before your timer expires.
    The cost of traveling from one node to another is asymmetric and may be negative (increasing
    your timer)

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
    bunny_to_bunny_cost = {}
    
    cost_map = {}
    for bunny in range(target - 1):
        start_to_bunny_cost.append(cost_from_start[bunny+1])

        # determine the shortest path from each bunny to the bulkhead
        bunny_cost = get_shortest_paths(bunny+1, times)
        bunny_to_bulkhead_cost.append(bunny_cost[target])

        # determine the cost from bunny to bunny
        bunny_to_bunny_cost[bunny] = {}
        for (pos, cost) in get_shortest_paths(bunny+1, times).items():
            if pos > 0 and pos < target and pos-1 != bunny:
                bunny_to_bunny_cost[bunny][pos-1] = cost


    # determine the first bunny to rescue by finding the sortest path to the bulkhead via a bunny
    ttl = time_limit
    rescued = []
    last_rescued = None

    rescue_cost = 10000000
    for bunny in range(target - 1):
        c = start_to_bunny_cost[bunny] + bunny_to_bulkhead_cost[bunny]
        if c <= ttl and c < rescue_cost:
            last_rescued = bunny
            rescue_cost = c
    if last_rescued is None:
        return []
    else:
        rescued.append(last_rescued)
        ttl -= start_to_bunny_cost[bunny]

    # rescue as many more bunnies as you can
    while True:
        # find next bunny to rescue
        next_bunny = None
        rescue_cost = 10000000
        for bunny in range(target - 1):
            if bunny in rescued:
                continue
            
            c = bunny_to_bunny_cost[last_rescued][bunny]
            if c < rescue_cost and c+bunny_to_bulkhead_cost[bunny] <= ttl :
                rescue_cost = c
                next_bunny = bunny
        if next_bunny is None:
            break
        else:
            rescued.append(next_bunny)
            ttl -= bunny_to_bunny_cost[last_rescued][next_bunny]
            last_rescued = next_bunny

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
