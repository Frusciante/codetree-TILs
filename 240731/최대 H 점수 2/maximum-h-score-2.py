# H 점수값 순회 --> 가능한 값인가 확인 필요

def cal_hscore(nums):
    maxim = 0
    for times in nums:
        cnt = 0
        for num in nums:
            if num >= times:
                cnt += 1       
        if cnt >= times:
            maxim = max(maxim, times)
    return maxim

n, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr_set = set(arr)

cnt_dic = {num: 0 for num in arr}
for num in arr_set:
    for check in arr:
        if num <= check:
            cnt_dic[num] += 1

start = cal_hscore(arr)

m = start
for h in range(start, 101):
    if h not in arr:
        continue
    c = arr.count(h)
    if l >= c:
        if (h + 1) in arr:
            if c + cnt_dic[h + 1] >= h + 1:
                m = h + 1
        else:
            if cnt_dic[h] >= h + 1:
                m = h + 1

print(m)