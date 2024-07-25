rand = list(map(int, input().split()))
rand.sort()

satisfied = False
for i in range(15):
    if satisfied:
        break
    for j in range(i + 1, 15):
        if satisfied:
            break
        for k in range(j + 1, 15):
            if satisfied:
                break
            for l in range(k + 1, 15):
                if satisfied:
                    break
                arr = []
                abcd = [rand[i], rand[j], rand[k], rand[l]]
                for num in abcd:
                    arr.append(num)
                for m in range(4):
                    for n in range(m + 1, 4):
                        arr.append(abcd[m] + abcd[n])
                for o in range(4):
                    for p in range(o + 1, 4):
                        for q in range(p + 1, 4):
                            arr.append(abcd[o] + abcd[p] + abcd[q])
                arr.append(sum(abcd))
                arr.sort()
                if arr == rand:
                    print(arr[i], arr[j], arr[k], arr[l])
                    satisfied = True