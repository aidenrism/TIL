def group_word(word):
    n = len(word)
    # group_cnt = 0
    emp = {}
    for i in range(n):
        if word[i] not in emp:
            emp[word[i]] = 1
        else:
            if word[i-1] != word[i]:
                # print('no')
                return False
            else:
                emp[word[i]] += 1
    return True

T = int(input())

cnt = 0
for _ in range(T):
    word = input()
    cnt += group_word(word)

print(cnt)


#     n = len(word)
#     group_cnt = 0
#     emp = {}
#     # for i in word:
#     for i in range(n):
#         if word[i] not in emp:
#             emp[word[i]] = 1
#         else:
#             if word[i-1] != word[i]:
#                 print('no')
#                 break
#             else:
#                 emp[word[i]] += 1
#     print(emp)
#
