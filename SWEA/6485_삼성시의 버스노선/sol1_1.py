my_list = [0, 1, 2, 3, 2]
# result = ' '.join(list(map(str, my_list)))
# print(result)
#
# my_list = [0, 1, 2, 3, 2]
# result = ' '.join(list(map(str, my_list)))
# print(result)

# lane = [0] * 5001 # 0~5000
# result = ''
# for idx in range(len(my_list)):
#     result += str(lane[my_list[idx]]) + ' '
# result = result[0:len(result) - 1]
# print(result)

# result = ''
# for idx in range(len(my_list)):
#     result += str(my_list[idx])+ ' '
# print(result[:-1])

for i in my_list:
    if i == 2:
        print(i)
        continue
    print('pass')