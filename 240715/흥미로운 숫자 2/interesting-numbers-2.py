x, y = tuple(map(int, input().split()))

cnt = 0
for i in range(x, y + 1):
    num_str = str(i)
    first = num_str[0]
    second = num_str[1]
    
    check = True
    num_cnt = 0
    for n in num_str:
        if n == first:
            num_cnt += 1
    
    if (num_cnt == 1 and num_str[1] == num_str[2]) or (len(num_str) - 1) == num_cnt:
        cnt += 1
    

print(cnt)