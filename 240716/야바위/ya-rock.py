n = int(input())
actions = [tuple(map(int, input().split())) for _ in range(n)]
cups = [0] * 4

high_score = 0
for i in range(1, 4):
    score = 0
    cups[i] = 1
    for a, b, c in actions:
        cups[a], cups[b] = cups[b], cups[a]
        if cups[c] == 1:
            score += 1
    high_score = max(score, high_score)
    for j in range(1, 4):
        cups[j] = 0

print(high_score)