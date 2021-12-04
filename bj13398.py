n = int(input())
ary = list(map(int, input().strip().split()))
if n == 1:
    print(ary[0])
    exit(0)
dp1 = [ary[0]] * n
dp2 = [0] * n
for i in range(1, n):
    dp1[i] = max(dp1[i-1] + ary[i], ary[i])
    dp2[i] = max(dp1[i-1], dp2[i-1] + ary[i])
print(max(*dp1, *dp2[1:]))