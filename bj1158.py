import sys
n, m = map(int, sys.stdin.readline().split())
a = list(range(1, n+1))
b = 0
c = []
for i in range(n):
    b = (b + m - 1) % (n - i)
    c.append(a.pop(b))
print('<', end='')
print(*c, sep=', ', end=">")
