import sys
sys.stdin = open('input.txt')


def bus(st):
    global change

    for j in range(1, bat[st]+1):
        # print(i+j)
        change += 1
        if st+j >= bat[0]:
            if change_lst:
                if change_lst[-1] > change:
                    change_lst.append(change)
            else:
                change_lst.append(change)
            change -= 1
            return
        else:
            bus(st+j)
            change -= 1


T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))
    change = -1
    change_lst = []
    bus(1)


    # print(change_lst)
    print(f'#{tc} {change_lst[-1]}')


# # 1. 백트래킹을 이용한 배터리 교체 함수
# def bus(st):
#     global change, result
#
#     # 1-1. 이미 교환횟수가 기존값보다 크면 여기서 반환
#     if result < change:
#         return
#     # 1-2. 도착했을때 기존값보다 작으면 결과값으로 반영
#     if st >= bat[0]:
#         if result > change:
#             result = change
#         return
#
#     # 1-3. 갈 수 있는 최대지점부터 시작해서 방문
#     for j in range(st+bat[st], st, -1):
#         change += 1
#         bus(j)
#         change -= 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     # 0. 충전소 개수와 충전량들이 있는 리스트
#     bat = list(map(int, input().split()))
#     # 0. 첫 배터리 장착은 교환횟수에서 제외
#     change = -1
#     result = 9999
#     # 1. 백트래킹을 이용한 배터리 교체 함수
#     bus(1)
#
#     # 2. 결과값 출력
#     print(f'#{tc} {result}')