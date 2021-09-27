import sys
lines = sys.stdin.readlines()
print(*map(lambda x:' '.join(map(lambda y: y[::-1], x.split())),lines[1:]), sep='\n')