import sys
sys.stdin = open('input.txt')


def my_number(n):

    for i in range(10):
        # print(number_list[i])
        if n == number_list[i]:
            return i

def check(n):

    odd = 0
    even = 0
    for i in range(7):
        if i%2 == 0:
            odd += n[i]

        else:
            even += n[i]
            print(n[i])
    print(n[7])
    print(odd*3 + even + n[7])
    if (odd*3 + even + n[7]) % 10 == 0:
        return sum(n)
    else:
        return 0


T = int(input())
for tc in range(1, 2):
    n, m = map(int, input().split())

    code = [list(map(int, input())) for _ in range(n)]
    # code = [list(map(int, input().split(' '))) for _ in range(10)]
    # code = [[] * list(map(int, input().split())) for _ in range(10)]
    number_list = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1],
                   [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]

    # print(code)
    # print(len(code[1]))
    #
    # print(code[1][0])
    # print(n, m)
    emp = []
    my_i = 0

    for i in range(n):
        for j in range(m-1,-1,-1):
            if code[i][j] == 1:
                emp += [j]
                my_i = i
                break
    # 값이 있는 행찾기
    # print(my_i)
    # 시작할 위치를 찾기 위해 마지막 1 뒤에 0이 몇개있는지 확인하기
    # print(emp)
    # print(m - 56 - (m - emp[0] - 1))
    # 순회를 시작할 위치
    fr = m - 56 - (m - emp[0] - 1)
    print(fr)
    temp = []
    ans = []
    for i in range(8):
        result = []
        for j in range(fr+i*7, fr+i*7+7):
            result.append(code[my_i][j])
            temp.append(code[my_i][j])
        print(result)
        ans.append(my_number(result))
    print(ans,'11')
    # 56개 수로 이루어진 7개 * 8숫자 암호
    print(temp)
    # 56
    print(len(temp))

    print(check(ans))
    # import sys
    # sys.stdin = open('input2.txt')
    #
    #
    # code = [list(map(int, input().split())) for _ in range(2)]
    # code2 = [[1]*2 for _ in range(3)]
    # print(code)
    # print(code2)