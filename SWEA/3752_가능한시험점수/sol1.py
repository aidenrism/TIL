import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    score_list = list(map(int, input().split()))

    # 가능한 점수의 부분집합들
    total_list = [0]
    # 0점은 자동으로 가능하므로 1을 할당
    check = [1] + [0] * sum(score_list)

    # 1. 점수를 꺼내면서 이미 구한 부분점수들과 조합을 해줌
    for score in score_list:
        end = len(total_list)
        # 1-2. 현재 있는점수까지만 해야함 (밑에서 append 하기 때문에 계속 추가됨)
        for t in total_list[:end]:
            # 1-3. 만약 이미 그 점수가 있다면 제외시킴(중복x)
            if not check[score+t]:
                # 1-4. 방문을 기록
                check[score+t] = 1
                # 1-5. 가능한 부분집합들에 추가해줌
                total_list.append(score+t)

    # print(total_list)
    ans = len(total_list)
    # 2. 결과값 출력
    print(f'#{tc} {ans}')
