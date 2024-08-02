n, m, p = tuple(map(int, input().split()))
c_record = []
u_record = []
for i in range(m):
    c, u = input().split()
    c_record.append(c)
    u_record.append(int(u))

full = [chr(65 + i) for i in range(n)]

while p >= 1 and u_record[p - 1] == u_record[p - 2]:
    p -= 1

if u_record[p - 1] == 0:
    print("")
else:
    answer = set()
    for i in range(p - 1, m):
        answer.add(c_record[i])

    answer = list(answer)
    for c in full:
        if c not in answer:
            print(c, end=' ')