import sys
check = [0]*1000000
check[1] = 1
prime_number = []
for num in range(3, 1000000, 2):
    if not check[num]:
        prime_number.append(num)
        for p in range(num*3, 1000000, 2*num):
            check[p] = 1
input_lines = sys.stdin.readlines()[1:]
for line in input_lines:
    input_num = int(line)
    count = 0
    if input_num == 4:
        print(1)
        continue
    for p in prime_number:
        if p > input_num: 
            break
        q = input_num - p
        if not check[q]:
            if  p <= q:
                count += 1
            else:
                break
    print(count)