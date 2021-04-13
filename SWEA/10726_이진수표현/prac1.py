import sys
sys.stdin = open('input.txt')


def OnOff(num):
    global result
    # 값이 0이면 while 문에 안 들어가므로 바로 'OFF'
    if not num:
        return 'OFF'
    temp = []
    while num:
        q = num//2
        remain = num%2
        temp += [remain]
        # print(temp)
        # 2이상으로 해주면 마지막 2로 나눴을 때 나머지가 안 더해짐
        if q >= 1:
            num = q
        else:
            if sum(temp[:n]) == n:
                return 'ON'
            else:
                return 'OFF'

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = []
    # print(n, m)
    print(OnOff(m))
    # print(temp)
    # print('끝')
