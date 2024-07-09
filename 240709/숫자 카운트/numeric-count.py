n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

#A가 정한 숫자 완전탐색
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            satisfied = True
            for item in arr:
                num, c1, c2 = item
                num = str(num)
                #1번 카운트 계산
                cnt1 = 0
                if ord(num[0]) - ord('0') == i:
                    cnt1 += 1
                if ord(num[1]) - ord('0') == j:
                    cnt1 += 1
                if ord(num[2]) - ord('0') == k:
                    cnt1 += 1
                if cnt1 != c1:
                    satisfied = False
                    break
                #2번 카운트 계산
                cnt2 = 0
                if ord(num[0]) - ord('0') == j or ord(num[0]) - ord('0') == k:
                    cnt2 += 1
                if ord(num[1]) - ord('0') == i or ord(num[1]) - ord('0') == k:
                    cnt2 += 1
                if ord(num[2]) - ord('0') == i or ord(num[2]) - ord('0') == j:
                    cnt2 += 1
                if cnt2 != c2:
                    satisfied = False
                    break
            if satisfied:
                cnt += 1
                print(i, j, k)

print(cnt)