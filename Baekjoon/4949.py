import sys
sys.stdin = open('4949_input.txt')


# 기존거 수정하기 어려워서 새로 구글링한거 참고해서 작성

while True:
    sentence = input()
    # .이면 그냥 답으로 출력
    if sentence == '.':
        break
    answer = True
    emp_list = []

    for word in sentence:
        if word == '(' or word == '[':
            emp_list.append(word)

        elif word == ')':
            # 이게 처음으로 들어간다면 no출력
            if len(emp_list) == 0:
                answer = False
                break
            if emp_list[-1] == '(':
                # 마지막 인덱스를 추출 (리스트에서 비워낸다)
                emp_list.pop()
            else:
                answer = False
                break

        elif word == ']':
            # 이게 처음으로 들어간다면 no출력
            if len(emp_list) == 0:
                answer = False
                break
            if emp_list[-1] == '[':
                # 마지막 인덱스를 추출 (리스트에서 비워낸다)
                emp_list.pop()
            else:
                answer = False
                break         
    # answer 이 True 고 emp_list가 비어있다면 
    if answer and not emp_list:
        print('yes')
    else:
        print('no')



















# brackets = ['(', '[', ']', ')']
# # brackets = """'(', '[', ']', ')'"""

# emp = []

# sentence = input()
# for word in sentence:
#     for bracket in brackets:
#         if word == bracket:
#             emp.append(word)
    
# print(emp, type(emp))
# # print(emp[0], type(emp[0]))
# # print(emp[1], type(emp[1]))
# print(emp[::-1])

# count = 0
# for idx in range(len(emp)-1):

#     if len(emp) <= 2:
#         break

    
#     # 만약 연속되는 두 인덱스가 [,] 이거나 (,) 이라면 
#     elif ['[', ']'] == [emp[idx], emp[idx+1]] or  ['(', ')'] == [emp[idx], emp[idx+1]]:


#         # idx+1 값을 주면 다음값이 아니라 두개 뒤의 값을 삭제한다 
#         del emp[idx], emp[idx]
#         # 다시 순회문으로 
#         for idx in range(len(emp)-1):
#             if len(emp) <= 2:
#                 break
#             # 만약 연속되는 두 인덱스가 [,] 이거나 (,) 이라면 
#             elif ['[', ']'] == [emp[idx], emp[idx+1]] or  ['(', ')'] == [emp[idx], emp[idx+1]]:
#                 del emp[idx], emp[idx]
#             else:
#                 count += 1
#                 print(0)
#                 continue
#     else:
#         count += 1
#         print(0)
#         continue

    