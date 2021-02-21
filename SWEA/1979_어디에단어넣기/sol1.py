import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    # print(puzzle)

    # tc마다 카운트 초기화
    count = 0

    #세로
    for c in range(n):
        #정방향(가로로)읽는 리스트
        #상하로 읽는 리스트 좌상우하
        cr_list = []
        rc_list = []
        #가로와 세로 리스트에 삽입
        for r in range(n):
            cr_list.append(puzzle[c][r])
            rc_list.append(puzzle[r][c])

        # print(in_list) #체크용

        # 1을 카운팅
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            # 가로 리스트 1이 k개인거 찾기
            if cr_list[i] == 1:
                cnt1 += 1

            elif cr_list[i] == 0:
                if cnt1 == k:
                    count += 1
                    # 카운트하고 0으로 초기화를 안한다면 마지막 if cnt==k 문에 걸림
                    cnt1 = 0
                else:
                    cnt1 = 0
            # 세로 리스트 동일 작업
            if rc_list[i] == 1:
                cnt2 += 1

            elif rc_list[i] == 0:
                if cnt2 == k:
                    count += 1
                    cnt2 = 0
                else:
                    cnt2 = 0
        # 1 이 k개로 끝난다면 여기서 카운팅됨
        if cnt1 == k:
            count += 1
        if cnt2 == k:
            count += 1
    print('#{} {}'.format(tc, count))