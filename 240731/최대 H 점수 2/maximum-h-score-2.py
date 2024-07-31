# H 점수값 순회 --> 가능한 값인가 확인 필요
n, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

result = 0
for i in range(n + 1):
    cnt = 0
    cntl = 0
    # n보다 작은 수 개수
    for j in range(n):
        if arr[j] >= i:
            cnt += 1
        elif arr[j] == i - 1:
            if cntl < l:
                cntl += 1
                cnt += 1
    
    if cnt >= i:
        result = i

print(result)