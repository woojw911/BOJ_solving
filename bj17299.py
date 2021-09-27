## 스택을 사용해서 구현
## rstrip을 해줘야 더 빠르다.

import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
f = [0] * 1000001
for num in num_list:
    f[num] += 1

stack = []
ngf = [-1] * n
for i in range(n):
    while stack and f[num_list[stack[-1]]] < f[num_list[i]]:
        ngf[stack.pop()] = num_list[i]
    stack.append(i)
print(*ngf, sep=' ')