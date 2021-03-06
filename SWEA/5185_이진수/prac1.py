import sys
sys.stdin = open('input.txt')


def AtoH(c):
    if c < '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


def HtoD(n):
    for i in range(len(asc)):
        if n == i:
            return asc[i]


T = int(input())
n, m = input().split()
n = int(n)

asc = [[0, 0, 0, 0],  #2진법 - 0(16진법)
       [0, 0, 0, 1],  #2진법 - 1(16진법)
       [0, 0, 1, 0],  #2진법 - 2(16진법)
       [0, 0, 1, 1],  #2진법 - 3(16진법)
       [0, 1, 0, 0],  #2진법 - 4(16진법)
       [0, 1, 0, 1],  #2진법 - 5(16진법)
       [0, 1, 1, 0],  #2진법 - 6(16진법)
       [0, 1, 1, 1],  #2진법 - 7(16진법)
       [1, 0, 0, 0],  #2진법 - 8(16진법)
       [1, 0, 0, 1],  #2진법 - 9(16진법)
       [1, 0, 1, 0],  #2진법 - A(16진법) - 10
       [1, 0, 1, 1],  #2진법 - B(16진법) - 11
       [1, 1, 0, 0],  #2진법 - C(16진법) - 12
       [1, 1, 0, 1],  #2진법 - D(16진법) - 13
       [1, 1, 1, 0],  #2진법 - E(16진법) - 14
       [1, 1, 1, 1]]  #2진법 - F(16진법) - 15

ans = []
for i in range(n):
    # print(AtoH(m[i]))
    # print(HtoD(AtoH(m[i])))
    # extend 로 하면 리스트로 안 집어넣고 원소로 집어넣음
    ans.extend(HtoD(AtoH(m[i])))
# print(ans)
# 숫자는 join이 안되므로 문자열 리스트로 변환시킨 다음에 join
print(''.join(list(map(str, ans))))
