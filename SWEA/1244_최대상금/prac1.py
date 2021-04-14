import sys
sys.stdin = open('input.txt')


T = int(input())
# num, m = map(int, input().split())
num, m = input().split()


print(num, type(num))

# print(list(num))
lst_num = list(num)
print(lst_num)
join_lst = ''.join(lst_num)
print(int(join_lst))
max_lst = sorted(lst_num)[::-1]
print(max_lst)
print(lst_num)