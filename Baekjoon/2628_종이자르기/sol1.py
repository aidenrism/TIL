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
    # print(*cut_idx)
    cut.append(cut_idx)
    if cut_idx[0] == 0:
        if col - cut_idx[1] > int(col / 2):
            y_idx = col - cut_idx[1]
        else:
            y_idx = cut_idx[1]
        y_list.append(y_idx)
    elif cut_idx[0] == 1:
        if row - cut_idx[1] > int(row / 2):
            x_idx = row - cut_idx[1]
        else:
            x_idx = cut_idx[1]
        x_list.append(x_idx)

# print(cut)
#
# print(cut[0][1])
x, y = [], []
try:
    y = q_sort(y_list)[0]
    x = q_sort(x_list)[0]
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

## 반례가 많으므로 sol2로..