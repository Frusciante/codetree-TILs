x, y = tuple(map(int, input().split()))

cnt = 0
for i in range(x, y + 1):
    num_str = str(i)
    len_str = len(num_str)
    first = num_str[0]

    another = -1
    for n in num_str:
        if n != first:
            another = n
            break
    
    f_cnt = 0
    a_cnt = 0
    for n in num_str:
        if n == first:
            f_cnt += 1
        elif n == another:
            a_cnt += 1
    
    if (a_cnt == 1 or f_cnt == 1) and (a_cnt + f_cnt == len_str):
        cnt += 1

print(cnt)