import math


def gcd(a,b):
    a = abs(a)
    b = abs(b)
    (a, b) = (a, b) if a < b else (b, a)
    while b > 0:
        a, b = b, a % b
    return a if a > 1 else 1


def get_next_pos_and_vector(vector, pos, dimensions):
    x = pos[0]
    y = pos[1]

    xd = vector[0]
    yd = vector[1]

    x_max = dimensions[0] - 1
    y_max = dimensions[1] - 1

    x_bounce = 0
    y_bounce = 0

    # get next y position
    x += xd
    while x<0 or x>x_max:
        x_bounce += 1
        if x<0:
            x = abs(x)
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

    # determine how the vector hanged as the beam bounces around
    xv = vector[0]
    yv = vector[1]
    if x_bounce % 2:
        xv *= -1
    if y_bounce % 2:
        yv *= -1

    return ((x, y), (xv, yv))


def eval_vector(vector, dimensions, your_position, guard_position, distance):
    segment_distance = math.sqrt(abs(vector[0])**2 + abs(vector[1])**2)
    dist_traveled = 0
    pos = (your_position[0], your_position[1])
    your_pos = (your_position[0], your_position[1])
    guard_pos = (guard_position[0], guard_position[1])
    # print str(vector) + " - > ",

    while dist_traveled + segment_distance < distance:
        (pos, vector)  = get_next_pos_and_vector(vector, pos, dimensions)        
        dist_traveled += segment_distance
        # print pos

        if pos == your_pos:
            # if you hit yourself return true
            # print "XXX"
            return False
        if pos == guard_pos:
            # print "!!!"
            # if you hit the guard return true
            return True
    # the beam died before hitting anyone
    # print "---"
    return False


def answer(dimensions, your_position, guard_position, distance):
    vectors = {}
    kill_shots = 0

    # iterate over all possible vectors
    for x in range(-distance, distance+1):
        for y in range(-distance, distance+1):
            # check for bad vectors
            if x == 0 and y == 0:
                continue
            elif x == 0:
                if your_position[0] != guard_position[0]:
                    continue
                if y > 0 and your_position[1] < guard_position[1]:
                    continue
                if y < 0 and your_position[1] > guard_position[1]:
                    continue
                y = y / abs(x)
            elif y == 0:
                if your_position[1] != guard_position[1]:
                    continue
                if x > 0 and your_position[0] < guard_position[0]:
                    continue
                if x < 0 and your_position[0] > guard_position[0]:
                    continue
                x = x / abs(x)
            else:
                d = gcd(x, y)
                x = x // d
                y = y // d
            v = (x, y)  
            if v not in vectors:
                vectors[v] = eval_vector(v, dimensions, your_position, guard_position, distance)
                if vectors[v]:
                    kill_shots += 1
            # elif vectors[v]:
            #     kill_shots += 1
    # print vectors

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
