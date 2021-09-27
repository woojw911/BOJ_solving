import sys
n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().strip()
    s = 0
    for c in line:
        if c == '(':
            s += 1
        elif c == ')':
            if s:
                s -= 1
            else:
                s = 1
                break
    if s:
        print("NO")
    else:
        print("YES")