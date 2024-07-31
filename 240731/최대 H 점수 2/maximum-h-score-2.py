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

cnt_arr = [0] * 101
for num in arr:
    for i in range(101):
        if i <= num:
            cnt_arr[i] += 1
            
start = cal_hscore(arr)
m = start
for h in range(start, 101):
    c = arr.count(h)
    if l >= c:
        if (h + 1) in arr:
            if c + cnt_arr[h + 1] >= h + 1:
                m = h + 1
        else:
            if cnt_arr[h] >= h + 1:
                m = h + 1

print(m)