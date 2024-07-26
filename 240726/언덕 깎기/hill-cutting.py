import sys

n = int(input())
arr = [int(input()) for _ in range(n)]
moved = [0] * n
mini = 100
maxi = 0
for item in arr:
    if item <= mini:
        mini = item
    if item >= maxi:
        maxi = item
s = maxi + mini

smallest = sys.maxsize
for i in range(1, maxi):
    for j, num in enumerate(arr):
        if num < i:
            moved[j] = i - num
        elif num > i + 17:
            moved[j] = num - i - 17
    ans = 0
    for mov in moved:
        ans += mov ** 2
    smallest = min(smallest, ans)
    
    for k in range(n):
        moved[k] = 0

print(smallest)