import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    try:
        words = input()
        sentence = []
        opener = '({['
        closer = ')}]'
        result = 1

        # input 값을 하나씩 추출하여 for 문을 돌린다.
        for word in words:
            # 여는 괄호면 빈 리스트에 넣어준다
            if word in opener:
                sentence.append(word)

            # 닫는 괄호면
            elif word in closer:
                # 빈 리스트가 비어있을 때 결과값을 -1
                if len(sentence) == 0:
                    result = 0
                    break
                # 리스트가 비어있지 않을 때 여는괄호와 같은 종류면 리스트에서 그 값을 뺀다.
                elif sentence[-1] == '(' and word == ')':
                    sentence.pop()
                elif sentence[-1] == '{' and word == '}':
                    sentence.pop()
                elif sentence[-1] == '[' and word == ']':
                    sentence.pop()
                else:
                    result = 0
            # 다 빼고 길이가 0 이면 result는 1 그리고 다시 for문의 다른 word로
            if len(sentence) == 0:
                result = 1
            else:
                result = 0
        # # input값이 공백이면 result 1
        # if len(words) == 0:
        #     result = 1
    except:
        result = 0


    print('#{} {}'.format(tc, result))