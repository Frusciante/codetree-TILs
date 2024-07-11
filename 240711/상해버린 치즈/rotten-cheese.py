n, m, d, s = tuple(map(int, input().split()))

eat_rec = [tuple(map(int, input().split())) for _ in range(d)]
ach_rec = [tuple(map(int, input().split())) for _ in range(s)]
eat_rec.sort(key = lambda x: (x[0], x[2]))

possible = [0] * (m + 1)
for (patient, start) in ach_rec:
    for (person, cheese, time) in eat_rec:
        if patient != person:
            continue
        if time < start:
            possible[cheese] += 1
        else:
            break
            
person_bitmap = [0] * (n + 1)
max_medicine = 0
for i in range(1, m + 1):
    cnt = 0
    if possible[i] >= s:
        for (person, cheese, time) in eat_rec:
            if cheese == i:
                if not person_bitmap[person]:
                    cnt += 1
                    person_bitmap[person] = 1
                
    max_medicine = max(max_medicine, cnt)

print(max_medicine)