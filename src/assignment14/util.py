def cal_hap(n, m, array, set_a, set_b):
    happiness = 0

    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    return happiness

