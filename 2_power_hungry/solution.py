def answer(xs):
    neg = []
    max_pos = 0
    has_zero = False

    # combine positive panels and not negative ones
    for p in xs:
        if p > 0:
            if max_pos == 0:
                max_pos = 1
            max_pos *= p
        elif p < 0:
            neg.append(p)
        else:
            has_zero = True

    # sort negative panels and try to get an even number
    neg.sort()
    neg_panels = len(neg)
    if neg_panels > 1 and neg_panels % 2 != 0:
        neg_panels -= 1

    # combine negative panels where you can to produce positive output
    max_neg = 1 if neg_panels > 0 else 0
    for i in range(neg_panels):
        max_neg *= neg[i]
    
    # return the total max power from positive and flipped negative panels
    max_power = 0
    if max_pos == 0 and not has_zero:
        max_power = max_neg
    elif max_neg == 0:
        max_power = max_pos
    else:
        max_power = max_pos * max_neg
        
    return str(max_power)
