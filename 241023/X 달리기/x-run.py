def accelerate_decision(sp, remainder):
    if ((sp + 2) * sp / 2 < remainder):
        return sp + 1
    elif ((n + 1) * n / 2 < remainder):
        return sp
    else:
        return sp - 1

n = int(input())
speed = 1
cnt = 1

while n > 0:
    speed = accelerate_decision(speed, n)
    n -= speed
    cnt += 1
    

print(cnt)