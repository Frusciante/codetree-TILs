def accelerate_decision(sp, remainder):
    if ((sp + 2) * (sp + 1) / 2 <= remainder):
        return sp + 1
    elif ((sp + 1) * sp / 2 <= remainder):
        return sp
    else:
        return sp - 1

n = int(input()) - 1
speed = 1
cnt = 1

while n > 0:
    speed = accelerate_decision(speed, n)
    n -= speed
    cnt += 1
    

print(cnt)