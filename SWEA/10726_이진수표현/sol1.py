import sys
sys.stdin = open('input.txt')


# 2. 함수 실행
def OnOff(num):
    global result
    # 값이 0이면 while 문에 안 들어가므로 바로 'OFF'
    if not num:
        return 'OFF'
    # 임시로 이진표기의 비트를 뒤에서부터 담아주는 리스트
    temp = []
    while num:
        q = num//2
        remain = num%2
        # 2로 나눈 나머지를 임시 리스트에 삽입
        temp += [remain]
        # 2이상으로 해주면 마지막 2로 나눴을 때 나머지가 안 더해짐
        if q >= 1:
            num = q
        # 처음부터 n개까지 더해보면 모두 1로 채워졌는지 알 수 있음
        else:
            if sum(temp[:n]) == n:
                return 'ON'
            else:
                return 'OFF'


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = []
    # 1. 숫자 m의 이진표기법 마지막 n개의 비트가 모두 켜져있는지 확인하는 함수
    ans = OnOff(m)
    # 결과값 출력
    print(f'#{tc} {ans}')
