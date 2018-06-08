from fractions import Fraction as frac

def subtract_matricies(m, n):
    """
        1 2     1 0     0 2
        3 4  -  1 2  =  2 2
        5 6     4 2     1 4
    """
    row_count = len(m)
    return [[m[row][col] - n[row][col] for col in range(row_count)] for row in range(row_count)]


def multiply_matricies(m, n):
    """
        1 2     1 2 3 4     11 14 17 20
        3 4  X  5 6 7 8  =  23 30 37 44
    """
    n = zip(*n)
    return [[sum(a * b for a, b in zip(row_m, col_n)) for col_n in n] for row_m in m]


def multiply_rows(r, q):
    """
        [1, 2, 3] * [4, 5, 6] = 1*4 + 2*5 + 3*6
    """
    result = 0
    for i in range(len(r)):
        result += r[i] * q[i]
    return result


def get_identity_matrix(m):
    return [[1 if r == c else 0 for c in range(len(m))] for r in range(len(m))]


def get_matrix_minor(m, r, c):
    return [row[:c] + row[c+1:] for row in (m[:r]+m[r+1:])]


def get_matrix_deternminant(m):
    # 2x2 matrix-specific
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += (-1**c) * m[0][c] * get_matrix_deternminant(get_matrix_minor(m, 0, c))
    return d


def invert_matrix(m):
    determinant = get_matrix_deternminant(m)
    # 2x2 matrix-specific
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactorRow)

    cofactors = map(list,zip(*cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def get_denominators(m):
    """
    Get the denominator for each state
    """
    denominators = []
    for s in m:
        d = 0
        for n in s:
            d += n
        denominators.append(d)
    return denominators


def get_int_array_for_fractions(r):
    denom = 1
    for f in r:
        denom = lcm(denom, f.denominator)
    result = [f.numerator * (denom / f.denominator) for f in r] + [denom]
    return result 


def lcm(a, b):
    a1 = 0
    b1 = 0
    if a < b:
        a1 = a
        b1 = b
    else:
        a1 = b
        b1 = a
    multiples = [b1]
    next_mult = a1
    i = 1
    while next_mult not in multiples:
        i += 1
        multiples.append(b1 * i)
        next_mult = a1 * i
    return next_mult


def answer(m):
    denominators = get_denominators(m)
    
    absorbing_states = []
    non_absorbing_states = []
    for state in range(len(denominators)):
        if denominators[state] == 0:
            absorbing_states.append(state)
        else:
            non_absorbing_states.append(state)

    # handle 1x1 nad 2x2 matricies
    if len(denominators) <= 2:
        return [1, 1]
    
    # handle absorbing state 0
    if 0 in absorbing_states:
        return [1 if s == 0 else 0 for s in range(len(m))] + [1]

    # setup standard for matricies
    q_matrix = [[frac(m[n][q], denominators[n]) for q in non_absorbing_states] for n in non_absorbing_states]
    i_matrix = get_identity_matrix(q_matrix)
    
    r_matrix = [[frac(m[n][a], denominators[n]) for a in absorbing_states] for n in non_absorbing_states]

    # calculate 
    iq_matrix = subtract_matricies(i_matrix, q_matrix)
    f_matrix = invert_matrix(subtract_matricies(i_matrix, q_matrix))
    result_matrix = multiply_matricies(f_matrix, r_matrix)

    # get probabilities from s0
    return get_int_array_for_fractions(result_matrix[0])


if __name__ == "__main__":
    a1 = answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    print a1
    assert a1 == [7, 6, 8, 21]

    a2 = answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    print a2
    assert a2 == [0, 3, 2, 9, 14]

    a3 = answer([[1, 1, 1], [1, 0, 0], [0, 0, 0]])
    print a3
    assert a3 == [1, 1]

    a4 = answer([[0, 1], [0, 0]])
    print a4
    assert a4 == [1, 1]

    a5 = answer([[0, 0, 0], [1, 0, 1], [0, 1, 1]])
    print a5
    assert a5 == [1, 0, 0, 1]
