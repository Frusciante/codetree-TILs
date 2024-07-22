ttt = [list(map(int, input())) for _ in range(3)]

vset = set()
hset = set()
win_team = set()
for i in range(3):
    for j in range(3):
        vset.add(ttt[i][j])
        hset.add(ttt[j][i])
    if len(vset) == 2:
        a = vset.pop()
        b = vset.pop()
        t = [a, b]
        t.sort()
        win_team.add(tuple(t))
    if len(hset) == 2:
        a = hset.pop()
        b = hset.pop()
        t = [a, b]
        t.sort()
        win_team.add(tuple(t))
    vset.clear()
    hset.clear()

dset1 = set()
dset2 = set()
for i in range(3):
    dset1.add(ttt[i][i])
    dset2.add(ttt[i][2 - i])
if len(dset1) == 2:
    a = dset1.pop()
    b = dset1.pop()
    t = [a, b]
    t.sort()
    win_team.add(tuple(t))
if len(dset2) == 2:
    a = dset2.pop()
    b = dset2.pop()
    t = [a, b]
    t.sort()
    win_team.add(tuple(t))

print(len(win_team))