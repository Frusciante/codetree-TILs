# H 점수값 순회 --> 가능한 값인가 확인 필요, H점수는 n을 넘지 못함
n, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

result = 0
for i in range(n + 1):
    cnt = 0
    cntl = 0
    for j in range(n):
        # H값과 원소 값 비교
        if arr[j] >= i:
            cnt += 1
        #같다면 세기 시작, l 이상인지 확인
        elif arr[j] == i - 1:
            if cntl < l:
                cntl += 1
                cnt += 1
    
    if cnt >= i:
        result = i

print(result)