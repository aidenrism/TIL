T = int(input())

for tc in range(1, T + 1):

    num = int(input())
    print('#{}'.format(tc))
    # N은 10이하의 정수 -- 2차원 리스트 생성
    s = [[0 for _ in range(10)] for _ in range(10)]

    # 양 끝에 1을 주고 안쪽에는 왼쪽위와 자신의 위의 값을 더해주기
    for i in range(0, num):
        for j in range(0, i + 1):
            if j == 0 or i == j:
                s[i][j] = 1
            else:
                s[i][j] = s[i - 1][j - 1] + s[i - 1][j]

    # 0이 아닌값들 출력해주기
    for i in range(0, num):
        for j in range(0, num):
            if s[i][j] == 0:
                print('', end='')
            else:
                print(s[i][j], end=' ') #여기 end 띄어쓰기 해야한다.
        print('')
