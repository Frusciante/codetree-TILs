arr = list(map(int, input().split()))
s = sum(arr)

import sys
min_val = sys.maxsize

for i in range(6):
    for j in range(6):
        if i == j:
            continue
        for k in range(6):
            if j == k or k == i:
                continue
            for l in range(6):
                if l == k or l == j or l == i:
                    continue
                team1 = arr[i] + arr[j]
                team2 = arr[k] + arr[l]
                team3 = s - team1 - team2
                min_val = min(max(team1, team2, team3) - min(team1, team2, team3), min_val)

print(min_val)