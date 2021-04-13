import sys
sys.stdin = open('input.txt')


# 2. 2를 곱해가면서 1이 넘으면 해당 위치(-1승..-2승..)에 1을 집어넣는 이진표기법
def FtoB(n):
    global cnt, result
    new_n = n * 2
    # 결과값에 저장
    result += str(int(new_n))
    # 자리수를 카운팅
    cnt += 1
    # 1이 되면 끝
    if new_n == 1:
        return
    # 1이 넘으면 소수부분만 재귀로 다시 실행
    else:
        n = new_n - int(new_n)
        FtoB(n)
    # 12번째 자리를 넘으면 오버플로우 출력
    if cnt > 12:
        result = 'overflow'
        return


T = int(input())
for tc in range(1, T+1):
    # 0. 실수값을 입력받는다
    num = float(input())

    # 0. 자리수와 출력문의 초기값
    cnt = 0
    result = ''
    # 1. 이진수로 변환시키면서 자리수를 저장하면서 세어주는 함수
    FtoB(num)
    # 3. 결과값 출력
    print(f'#{tc} {result}')