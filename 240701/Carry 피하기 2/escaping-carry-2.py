n = int(input())
nums = [int(input()) for _ in range(n)]

maximum = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a = nums[i]
            b = nums[j]
            c = nums[k]
            digit = 4
            check = True
            while digit >= 0:
                div = 10**digit
                s = a // div + b // div + c // div
                a %= div
                b %= div
                c %= div
                if s >= 10:
                    check = False
                    break
                digit -= 1
            if check:
                maximum = max(maximum, nums[i] + nums[j] + nums[k])

print(maximum)