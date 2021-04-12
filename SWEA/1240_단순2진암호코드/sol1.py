import sys
sys.stdin = open('input.txt')


# 3. 진짜 숫자를 찾는 함수
def my_number(n):
    for i in range(10):
        if n == number_list[i]:
            return i


# 4. 올바른 코드일 때 코드의 총합을 return 시킴
def check(n):
    odd = 0
    even = 0
    for i in range(7):
        if i%2 == 0:
            odd += n[i]
        else:
            even += n[i]
    # 10으로 나누어 떨어져야 함
    if (odd*3 + even + n[7]) % 10 == 0:
        return sum(n)
    # 코드가 아니면 0
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 0. 암호코드 정보
    hidden_code = [list(map(int, input())) for _ in range(n)]

    # 0. 숫자정보
    number_list = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1],
                   [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]

    # 1-1. 값이 들어있는 행찾기
    my_i = 0
    # 1-1. 시작할 위치를 찾기 위해 마지막 1 뒤에 0이 몇개있는지 확인하기
    emp = []
    for i in range(n):
        for j in range(m-1,-1,-1):
            if hidden_code[i][j] == 1:
                emp += [j]
                my_i = i
                break
    # 1-1. 값이 들어있는 행찾기
    # print(my_i)

    # 1-1. 버려지는 숫자들
    # print(emp)

    # 1-2. 순회를 시작할 위치
    # print(m - 56 - (m - emp[0] - 1))
    fr = m - 56 - (m - emp[0] - 1)
    # print(fr)

    # 2. 진짜 코드 찾기
    code = []
    # 8개의 숫자
    for i in range(8):
        number = []
        # 7개씩 끊어서 읽기
        for j in range(fr+i*7, fr+i*7+7):
            number.append(hidden_code[my_i][j])
        # print(number)

        # 2-1. 실제 숫자를 찾는 함수를 실행시켜서 code에 append
        code.append(my_number(number))

    # 5. 결과 값 출력
    print(f'#{tc} {check(code)}')
