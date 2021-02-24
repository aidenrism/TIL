import sys
sys.stdin = open('input.txt')
# 퀵정렬
def q_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = [], []
    pibut = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] < pibut:
            left.append(nums[idx])
        else:
            right.append(nums[idx])

    sorted_left = q_sort(left)
    sorted_right = q_sort(right)
    return [*sorted_left, pibut, *sorted_right]

row, col = map(int, input().split())

n = int(input())

cut = []
x_list = []
y_list = []

for idx in range(n):
    cut_idx = list(map(int, input().split()))
    # 가로로 자를때 ==> 세로를 봐야함.
    if cut_idx[0] == 0:
        y_list.append(cut_idx[1])
    else:
        x_list.append(cut_idx[1])

y_list.append(0)
y_list.append(col)
x_list.append(0)
x_list.append(row)

# print(q_sort(y_list))
# print(q_sort(x_list))

y_list = q_sort(y_list)
x_list = q_sort(x_list)
section_y = []
section_x = []

for i in range(len(y_list)-1, 0, -1):
    section_y.append(y_list[i]-y_list[i-1])
# print(q_sort(section_y))

for k in range(len(x_list)-1, 0, -1):
    section_x.append(x_list[k]-x_list[k-1])
# print(q_sort(section_x))

x, y = [], []
try:
    y = q_sort(section_y)[-1]
    x = q_sort(section_x)[-1]
except:
    if x:
        pass
    else:
        x = row
    if y:
        pass
    else:
        y =col
print(x*y)

