from itertools import combinations

def pro_letter(n, letters, k):
    total_combinations = list(combinations(range(n), k))
    favorable_combinations = [comb for comb in total_combinations if any(letters[i] == 'a' for i in comb)]

    probability = len(favorable_combinations) / len(total_combinations)
    return round(probability, 4)
