a, b, c = tuple(map(int, input().split()))

max_ans = 0
a_num = c // a
b_num = 0

while a_num >= 0:
    ans = (a_num * a) + (b_num * b)
    a_num -= 1
    if a_num >= 0 and ans - a + b <= c:
        b_num += 1
    max_ans = max(max_ans, ans)

print(max_ans)