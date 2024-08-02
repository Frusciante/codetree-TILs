n = int(input())
mov = [2] * 11

cnt = 0
for i in range(n):
    p, loc = tuple(map(int, input().split()))
    if mov[p] != loc and mov[p] != 2:
        cnt += 1
        mov[p] = loc
    elif mov[p] == 2:
        mov[p] = loc

print(cnt)