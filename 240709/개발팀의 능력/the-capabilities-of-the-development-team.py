arr = list(map(int, input().split()))
s = sum(arr)

import sys
min_val = sys.maxsize

for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if j == k or k == i:
                continue
            team1 = arr[i] + arr[j]
            team2 = arr[k]
            team3 = s - team1 - team2
            if team1 == team2 or team1 == team3 or team2 == team3:
                continue
            min_val = min(max(team1, team2, team3) - min(team1, team2, team3), min_val)

if min_val == sys.maxsize:
    min_val = -1

print(min_val)