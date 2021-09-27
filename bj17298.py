## 오등수 NGE(i)는 수열 A{n}의 A{i}에 대해, A{i}의 오른쪽에 있는 A{i}보다 큰 수 중,
## 가장 왼쪽에 있는 수이다. 그러한 수가 없다면 -1이라고 한다.
## 오른쪽은 i보다 큰 인덱스를 가지는 수를 말한다.
##
## 맨 오른쪽에 있는 수는 무조건 -1을 오등수로 가진다.
## 어떤 i에 대하여, A{i} < A{i+1} 이면 NGE(i) = A{i+1}이다.
## A{i} > A{i+1}라면, A{i}와 NGE(i+1)사이에 있는 모든 수는 A{i}보다 작다.
## 따라서 A{i} < NGE(i+1) 이면 NGE(i) = NGE(i+1)이고, 그렇지 않은 경우에는,
## 다시 NGE(i+1)의 오등수와 A{i}를 비교하면 된다.
## 재귀적으로 취하던 오등수가 -1이 된다면, NGE(i)는 -1이다.

import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
nge_index = [-1] * n
for i in range(n-2, -1, -1):
    t = i + 1
    while t != -1:
        if num_list[i] < num_list[t]:
            break
        t = nge_index[t]
    nge_index[i] = t
print(*map(lambda x: num_list[x] if x > -1 else -1, nge_index), sep=" ")