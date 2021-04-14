import sys
sys.stdin = open('input.txt')


# 1. 몇번 바꿨는지 세주면서 경우의 수를 돌린다
def dfs(idx, cnt):
    global result
    # 1-1. 바꿀 수 있는 횟수가 남았다면
    if cnt:
        # 1-3. 최대값이 나와도 내부에서 교체해줌
        if lst_num == max_lst:
            # 매개변수 할당 (동일값들로 되어있는지, 만약 동일값들이면 카운팅 남아도 바꿔줄 필요없음)
            c = 0
            for i in range(len(lst_num) - 1):
                if lst_num[i] == lst_num[i + 1]:
                    c = 1
            # 동일한 값이 없다면 카운팅이 남았을 때 결과가 달라지므로 남은 카운팅 횟수만큼 위치를 바꿔줌
            if c == 0:
                while cnt:
                    lst_num[-1], lst_num[-2] = lst_num[-2], lst_num[-1]
                    cnt -= 1
            # 마지막 값을 저장
            temp = int(''.join(lst_num))
            # 마지막 값이 기존값보다 크면 마지막 값을 출력해줌
            if result < temp:
                result = temp
            return
        # 1-2.
        else:
            for i in range(idx, len(lst_num) - 1):
                for j in range(i, len(lst_num)):
                    # 내 뒤에 값이 나보다 크면 교체시도
                    if int(lst_num[i]) < int(lst_num[j]):
                        lst_num[i], lst_num[j] = lst_num[j], lst_num[i]
                        # 카운팅 빼고 재귀 (만약 카운팅이 끝났다면 기존값과 비교해준다)
                        dfs(idx + 1, cnt - 1)
                        # 원상 복귀
                        lst_num[i], lst_num[j] = lst_num[j], lst_num[i]

    # (카운팅이 끝났다면 dfs는 여기로) 기존값과 비교
    else:
        temp = int(''.join(lst_num))
        if result < temp:
            result = temp
        return


T = int(input())

for tc in range(1, 1 + T):
    num, change = input().split()

    # 0. 순회를 위해서 리스트 변환
    lst_num = list(num)
    change = int(change)
    # 0. 최대값 저장
    max_lst = sorted(lst_num)[::-1]
    result = 0
    # 1. dfs로 경우의 수를 찾아줌
    dfs(0, change)

    print(f'#{tc} {result}')