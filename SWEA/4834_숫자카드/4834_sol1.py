import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

# 첫줄에는 장수
# 두번째 줄에는 숫자카드들이 여백없이

    length = int(input())
    numbers = input()

    number = [int(_) for _ in numbers]
    # print(number)
    cnt_list = [0]*10

    # 빈공간에 출현개수만큼 채워주기
    for num in range(length):
        cnt_list[number[num]] += 1
    # print(cnt_list) [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 빈도수가 많은 값과 가장 큰값 찾기
    max_index, max_num = 0, 0
    for i in range(len(cnt_list)):
        # =을 주어서 동일한 인덱스 값이라도 마지막 값으로 대체됨
        if cnt_list[i] >= max_index:
            max_index = cnt_list[i]
            max_num = i
    print('#{} {} {}'.format(tc, max_num, max_index))
