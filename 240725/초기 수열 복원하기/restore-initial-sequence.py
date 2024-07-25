n = int(input())
arr = list(map(int, input().split()))

original = []
for i in range(1, n):
    original.append(i)
    for j in range(n - 1):
        new = arr[j] - original[j]
        if new <= n and new not in original:
            original.append(new)
        else:
            original.clear()
            break
    if len(original) == n:
        for elem in original:
            print(elem, end=' ')
        break