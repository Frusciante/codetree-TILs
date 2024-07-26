n, k = tuple(map(int, input().split()))
bombs = [int(input()) for _ in range(n)]
bombs_cnt = {bomb: 0 for bomb in bombs}

for i, bomb in enumerate(bombs):
    for j in range(1, k + 1):
        if i + j >= n:
            break
        if bombs[i + j] == bomb:
            bombs_cnt[bomb] += 2 if bombs_cnt[bomb] == 0 else 1
            break
# 최소 폭탄 2개는 있어야 터질 수 있으므로 카운트가 0일 때 꼬이는 것을 방지하기 위해 maximum을 1이라고 둠
maximum = 1
max_bomb_num = 0

for bomb_num in bombs_cnt:
    if bombs_cnt[bomb_num] > maximum:
        maximum = bombs_cnt[bomb_num]
        max_bomb_num = bomb_num
    elif bombs_cnt[bomb_num] == maximum and bomb_num > max_bomb_num:
        max_bomb_num = bomb_num

print(max_bomb_num)