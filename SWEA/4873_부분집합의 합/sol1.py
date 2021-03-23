# num = '1 2 3 4 5 6'
# #
# # for i in range(1<<4):
# #     ans = ''
# #     for j in range(4):
# #         if i & (1<<j):
# #             ans += num[j]
# #     print(ans)

num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)

#부분집합 구하기
lst = []
# 2**12 만큼 i를 생성
for i in range(1<<Len):
    # 부분집합을 받을 리스트
    sub_lst = []
    # 1을 0~12번 시프팅해가며 i와 j번째 비트가 1인지 아닌지 리턴
    for j in range(3):
        if i & (1<<j):
            sub_lst.append(num[j])
    lst.append(sub_lst)
# 2의 12승인 4096만큼 부분집합을 만듦
print(lst)