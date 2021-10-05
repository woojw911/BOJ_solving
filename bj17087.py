import sys
n, s = map(int, sys.stdin.readline().split())
gcd = None
a0, *a_list =  map(lambda x: abs(int(x) - s), sys.stdin.readline().split())
gcd = a0
for a in a_list:
    if gcd != a:
        x, y = max(a, gcd), min(a, gcd)
        while y:
            x, y = y, x % y
        gcd = x

        if gcd == 1:
            break
print(gcd)