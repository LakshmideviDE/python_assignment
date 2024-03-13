def find_runner_up_score(n, arr):
    scores = set(arr)
    scores.remove(max(arr))
    runner_up = max(scores)
    return runner_up
arr = list(map(int, input().split()))

