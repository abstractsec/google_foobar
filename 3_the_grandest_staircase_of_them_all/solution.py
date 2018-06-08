def answer(n):
    mem = []
    for level in range(n + 1):
        m = []
        for step in range(n):
            m.append(1 if level < 3 and step >= level else 0)
        mem.append(m)

    for level in range(3, n + 1):
        for step in range(2, n):
            mem[level][step] = mem[level][step - 1]
            if step <= level:
                mem[level][step] += mem[level - step][step - 1]

    return mem[n][n - 1]
