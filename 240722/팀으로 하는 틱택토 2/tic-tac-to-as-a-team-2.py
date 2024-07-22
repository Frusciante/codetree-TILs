ttt = [list(map(int, input())) for _ in range(3)]

vset = set()
hset = set()
cnt = 0
for i in range(3):
    for j in range(3):
        vset.add(ttt[i][j])
        hset.add(ttt[j][i])
    cnt += 1 if len(vset) == 2 else 0
    cnt += 1 if len(hset) == 2 else 0
    vset.clear()
    hset.clear()

dset1 = set()
dset2 = set()
for i in range(3):
    dset1.add(ttt[i][i])
    dset2.add(ttt[i][2 - i])
cnt += 1 if len(dset1) == 2 else 0
cnt += 1 if len(dset2) == 2 else 0

print(cnt)