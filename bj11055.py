n = int(input())
ary = list(map(int, input().strip().split()))

dp = [0] * n
for i in range(n):
    dp[i] = ary[i]
    for j in range(i):
        if ary[j] < ary[i] and dp[i] < dp[j] + ary[i]:
            dp[i] = dp[j] + ary[i]
print(max(dp))