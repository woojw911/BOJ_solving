import sys
n, k = map(int, sys.stdin.readline().split())
dp = [1] * (n+1)
for i in range(k-1):
    for j in range(n, 0, -1):
        dp[j] = sum(dp[0:j+1]) % 1000000000
print(dp[n])