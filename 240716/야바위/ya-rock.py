n = int(input())
actions = [tuple(map(int, input().split())) for _ in range(n)]

high_score = 0
for i in range(1, 4):
    score = 0
    cups = [0] * 4
    cups[i] = 1
    for a, b, c in actions:
        cups[a], cups[b] = cups[b], cups[a]
        if cups[c] == 1:
            score += 1
    high_score = max(score, high_score)

print(high_score)