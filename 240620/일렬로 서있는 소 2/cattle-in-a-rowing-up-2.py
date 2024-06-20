n = int(input())
heights = list(map(int, input().split()))

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if heights[i] <= heights[j]:
            for k in range(j+1, n):
                if heights[j] <= heights[k]:
                    cnt += 1

print(cnt)