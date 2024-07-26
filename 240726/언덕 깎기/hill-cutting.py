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
for i in range(1, (s + 1) // 2):
    for j, num in enumerate(arr):
        if num < i:
            moved[j] 
        elif num > i - num