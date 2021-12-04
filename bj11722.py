n = int(input())
ary = list(map(int, input().strip().split()))

dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if ary[j] > ary[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))