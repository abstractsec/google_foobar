import math

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    (a, b) = (a, b) if a < b else (b, a)
    while b > 0:
        a, b = b, a % b
    return a if a > 1 else 1


def get_next_pos_and_bearing(bearing, pos, dimensions):
    x = pos[0]
    y = pos[1]

    xd = bearing[0]
    yd = bearing[1]

    x_max = dimensions[0]
    y_max = dimensions[1]

    x_bounce = 0
    y_bounce = 0

    # get next y position
    x += xd
    while x<1 or x>x_max:
        x_bounce += 1
        if x<1:
            x = abs(x) + 1
        if x>x_max:
            x = x_max - (x - x_max)
    
    # get next y position
    y += yd
    while y<0 or y>y_max:
        y_bounce += 1
        if y<0:
            y = abs(y)
        if y>y_max:
            y = y_max - (y - y_max)

    # determine how the bearing hanged as the beam bounces around
    xv = bearing[0]
    yv = bearing[1]
    if x_bounce % 2:
        xv *= -1
    if y_bounce % 2:
        yv *= -1
    # return the new position and bearing
    return ((x, y), (xv, yv))


def eval_bearing(bearing, dimensions, your_position, guard_position, distance):
    segment_distance = math.sqrt(abs(bearing[0])**2 + abs(bearing[1])**2)
    dist_traveled = 0
    pos = (your_position[0], your_position[1])
    your_pos = (your_position[0], your_position[1])
    guard_pos = (guard_position[0], guard_position[1])

    # Follow the laser from position to position until the beam degrades
    while dist_traveled + segment_distance <= distance:
        (pos, bearing)  = get_next_pos_and_bearing(bearing, pos, dimensions)        
        dist_traveled += segment_distance

        if pos == your_pos:
            # If you will hit yourself, return false
            return False
        if pos == guard_pos:
            # If you will hit the guard, return true
            return True
    # If you won't hit anyone, return false
    return False


def answer(dimensions, your_position, guard_position, distance):
    bearings = {}
    kill_shots = 0

    # iterate over all possible bearings
    for x in range(-distance, distance+1):
        for y in range(-distance, distance+1):
            # check for bad bearings
            if x == 0 and y == 0:
                continue
            elif x == 0:
                v = (0, y / abs(y))
                if v in bearings:
                    # skip if already evaluated
                    continue
                
                if your_position[0] != guard_position[0]:
                    # skip if firing stright and not on same x-position
                    bearings[v] = False
                    continue
                elif y > 0 and your_position[1] > guard_position[1]:
                    # skip if firing stright and in the wrong direction
                    bearings[v] = False
                    continue
                elif y < 0 and your_position[1] < guard_position[1]:
                    # skip if firing stright and in the wrong direction
                    bearings[v] = False
                    continue

                bearings[v] = True
                kill_shots += 1
            elif y == 0:
                v = (x / abs(x), 0)
                if v in bearings:
                    # skip if already evaluated
                    continue

                if your_position[1] != guard_position[1]:
                    # skip if firing stright and not on same x-position
                    bearings[v] = False
                    continue
                if x > 0 and your_position[0] > guard_position[0]:
                    # skip if firing stright and in the wrong direction
                    bearings[v] = False
                    continue
                if x < 0 and your_position[0] < guard_position[0]:
                    # skip if firing stright and in the wrong direction
                    bearings[v] = False
                    continue

                bearings[v] = True
                kill_shots += 1
            else:
                # reduce bearing bearing using GCD 
                d = abs(gcd(x, y))
                x1 = x // d
                y1 = y // d
                v = (x1, y1)

                if v not in bearings:
                    # only evluate if this is the first time we've seen this bearing
                    bearings[v] = eval_bearing(v, dimensions, your_position, guard_position, distance)
                    if bearings[v]:
                        kill_shots += 1

    return kill_shots


def test(expect, dimensions, your_position, guard_position, distance):
    s = answer(dimensions, your_position, guard_position, distance)
    print "PASS\n----" if s == expect else "FAIL\n----"
    print """Dimensions: %s
Position:   %s
Guard Pos:  %s
Distance:   %d
  -> Ouput: %d (%d expected)\n""" % (
     dimensions, your_position,
     guard_position, distance, s, expect)


if __name__ == "__main__":
    test(7, [3, 2], [1, 1], [2, 1], 4)
    test(9, [300, 275], [150, 150], [185, 100], 500)
