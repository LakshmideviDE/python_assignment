from collections import deque
def solve(integers):
    integers_list = [int(x) for x in integers.split(' ')]
    sorted_integers = sorted(integers_list)
    stack = deque(integers_list)
    pile = deque()
    while len(stack) >= 2:
        pile.appendleft(stack.popleft() if stack[0] >= stack[-1] else stack.pop())
    pile.appendleft(stack.pop())
    return 'Yes' if pile == deque(sorted_integers) else 'No'
