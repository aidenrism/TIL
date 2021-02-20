import sys
sys.stdin = open('input.txt')


def my_max(x):
    result = []
    maxy = x[0]
    for i in range(len(x)):
        if x[i] >= maxy:
            maxy = x[i]
            result.append(maxy)
    # 같은크기의 값이 있어도 마지막 큰 값 하나만 출력
    return result[-1]
    # if len(result) > 1:
    #     return result[-1]
    # else:
    #     return result[-1]

# def my_max(x):
#     result = []
#     for i in x:
#         result.append(max(x))
#     return result[-1]

for tc in range(1, 11):
    t = int(input())
    ary = []
    o_list = []
    o1_list = []
    cr_list = []
    rc_list = []

    for i in range(100):
        ary.append(list(map(int, input().split())))

    # col row 정방향 순회문만들기
    for c in range(len(ary)):
        c_list = []
        r_list = []
        # col 마진합과 row 마진합 따로 내부 리스트에 append
        for r in range(len(ary[c])):
            c_list.append(ary[c][r])
            r_list.append(ary[r][c])
            if c == r:
                cr_list.append(ary[c][r])

        o_list.append(sum(c_list))
        o_list.append(sum(r_list))
    o_list.append(sum(cr_list))
    # print(rc_list)

    # print(o1_list)

    rc_list = []
    o2_list = []
    # col 정방향 row 역방향 순회문만들기
    for c in range(len(ary)):
        i2_list = []
        for r in range(len(ary[c])-1,-1,-1):
            i2_list.append(ary[c][r])
        o2_list.append(i2_list)
    # col 정방향 row 역방향중 col idx값과 row idx 값이 같은것을 모아줌
    for c in range(len(o2_list)):
        for r in range(len(o2_list[c])):
            if c == r:
                rc_list.append(o2_list[c][r])

    # print(rc_list) # 1 6 4 2 8
    o_list.append(sum(rc_list))


    # if len(my_max(o_list)) > 1:
    #     result = my_max(o_list)[0]
    # else:
    #     result = my_max(o_list)
    # print(o_list)
    print('#{} {}'.format(t, my_max(o_list)))