import sys
sys.stdin = open('input.txt')

num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)

#부분집합 구하기
lst = []
# 2**12 만큼 i를 생성
for i in range(1<<Len):
    # 부분집합을 받을 리스트
    sub_lst = []
    # 1을 0~12번 시프팅해가며 i와 j번째 비트가 1인지 아닌지 리턴
    for j in range(Len):
        if i & (1<<j):
            sub_lst.append(num[j])
    lst.append(sub_lst)
# 2의 12승인 4096만큼 부분집합을 만듦
# print(lst)

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    k_lst = []
    for idx in lst:
        if len(idx) == n:
            k_lst.append(idx)
    # 부분집합의 길이가 n개인 리스트들
    # print(k_lst)

    result = 0
    # 부분집합의 합이 k면 result에 1을 더해줌
    for kdx in k_lst:
        if sum(kdx) == k:
            result += 1
    print('#{} {}'.format(tc, result))