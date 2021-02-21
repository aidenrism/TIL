import sys
sys.stdin = open('input.txt')


# num = "ZRO ONE FIV THR ONE"
T = int(input())
for _ in range(T):
    tc = list(input().split())
    str_num = list(input().split())

    # print(prac_list)

    def str_sort(x):
        emp = []
        for i in x:
            if i == 'ZRO':
                i = 0
            elif i == 'ONE':
                i = 1
            elif i == 'TWO':
                i = 2
            elif i == 'THR':
                i = 3
            elif i == 'FOR':
                i = 4
            elif i == 'FIV':
                i = 5
            elif i == 'SIX':
                i = 6
            elif i == 'SVN':
                i = 7
            elif i == 'EGT':
                i = 8
            elif i == 'NIN':
                i = 9
            emp += [i]
        for i in range(len(emp)-1, -1, -1):
            for j in range(i):
                if emp[j] > emp[j+1]:
                    emp[j+1], emp[j] = emp[j], emp[j+1]
        # return emp
        emp2 = []
        for i in emp:
            if i == 0:
                i = 'ZRO'
            elif i == 1:
                i = 'ONE'
            elif i == 2:
                i = "TWO"
            elif i == 3:
                i = "THR"
            elif i == 4:
                i = "FOR"
            elif i == 5:
                i = "FIV"
            elif i == 6:
                i = 'SIX'
            elif i == 7:
                i = 'SVN'
            elif i == 8:
                i = 'EGT'
            elif i == 9:
                i = 'NIN'
            emp2 += [i]
        return emp2

    # print(*str_sort(str_num))
    print(tc[0])
    print(*str_sort(str_num))