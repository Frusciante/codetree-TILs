n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(1, 11):
    x = i
    for start, end in ranges:
        if start <= x * 2 and x * 2 <= end:
            x *= 2
        else:
            break
    else:
        answer = i
        break
print(answer)