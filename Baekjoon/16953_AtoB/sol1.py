import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

cnt = 0

while True:
    if a == b:
        cnt += 1
        break
    elif (b % 10 != 1 and b % 2 != 0) or b < a:
        cnt = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1

print(cnt)