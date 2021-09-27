## 스택을 사용해서 구현

import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

stack = []
nge = [-1] * n
for i, num in enumerate(num_list):
    while stack:
        if num_list[stack[-1]] < num:
            top = stack.pop()
            nge[top] = num
        else:
            break
    stack.append(i)
print(*nge, sep=' ')