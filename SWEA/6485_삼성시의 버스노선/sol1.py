import sys
sys.stdin = open('s_input.txt')


T = int(input())

# 테스트 케이스 진행 횟수
for tc in range(1, T+1):
    # 1부터 500사이의 정수 - 버스노선 개수
    N = int(input())
    # 5000개의 버스정류장을 셀, 빈 리스트
    cnt_list = [0]*5001
    # 버스 노선의 개수만큼 순회
    for idx in range(N):
        # 노선사이의 버스정류장만큼 개수를 세어줌 (tuple은 사용 안해도 괜찮음)
        A1, B1 = tuple(map(int,(input().split())))
        for stop in range(A1, B1+1):
            cnt_list[stop] += 1


    # print(cnt_list)
    p_list = []
    P = int(input())

    for i in range(P):

        t = int(input())
        for j in range(t, t+1):
            p_list.append(cnt_list[j])

    result = ' '.join(list(map(str, p_list)))

    # 위의 방식으로 해도 되고 아래 방식으로 해도 무방함
    # result = ''
    # for idx in range(len(p_list)):
    #     result += str(p_list[idx]) + ' '

    # result = result[:-1]

    print('#{} {}'.format(tc, result))







# that i tried
# print(list(map(str, p_list)))
# for i in str(p_list):
#     print(i)
# print(str(p_list))
# print(str(p_list), type(str(p_list)))
# print(str(p_list)[1])
# print(' '.join(p_list))
# print(' '.join(str(p_list5)))