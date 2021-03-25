import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    words = list(input())
    i = 1

    while len(words) > 1:
        if i >= len(words):
            break
        # 마지막 stack 값을 추출하고 그 전에 값과 비교한다
        current = words.pop(-i)
        if words[-i] == current:
            words.pop(-i)
            if i > 1:
                # 일치하여 뽑았다면 다시 그 전의 값과 다음값을 비교해본다.
                i -= 1
        # 마지막 stack 값과 다르다면 다시 제자리에 word를 집어넣어주고 그 아래값을 pop한다.
        else:
            if i == 1:
                words.insert(len(words), current)
            else:
                words.insert(-i+1,current)
            # 값을 추출하지 못했으므로 하나 더 아래 stack의 값을 살펴봄
            i += 1
    print('#{} {}'.format(tc, len(words)))

# i = 1
# no_erase = []
# while len(words) > 3:
#     current = words.pop(-i)
#     if current == words[-(i+1)]:
#         words.pop(-(i+1))
#
#     else:
#         no_erase.append(current)
#
# print(words)
# print(no_erase)
# #
#
# words = ['C','A','B','A','A','B','A']
#
# i = 1
# no_erase = []
# while len(words) > 3:
#     current = words.pop(-i)
#     if current == words[-(i)]:
#         words.pop(-(i+1))
#
#     else:
#         no_erase.append(current)
#
# for jdx in range(len(no_erase)-1, -1, -1):
#     words.append(no_erase[jdx])
# print(words)
# print(no_erase)
