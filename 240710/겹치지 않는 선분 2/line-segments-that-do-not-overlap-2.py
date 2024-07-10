n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
n_bitmap = [0] * n

for i in range(n - 1):
    x1, x2 = arr[i]
    for j in range(i + 1, n):
        x3, x4 = arr[j]
        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            n_bitmap[i] = n_bitmap[j] = 1            
print(n_bitmap.count(0))