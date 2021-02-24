numbers = input()

number = '0123456789'
cal = []
result = 0

for idx in range(len(numbers)):
    if numbers[idx] in number:
        cal.append(int(numbers[idx]))
    else:
        if len(cal) > 2:
            if numbers[idx] == '*':
                cal.append(cal.pop(-2) * cal.pop())
            elif numbers[idx] == '+':
                cal.append(cal.pop(-2) + cal.pop())
        else:
            if numbers[idx] == '*':
                cal.append(cal.pop(-2) * cal.pop())
            elif numbers[idx] == '+':
                cal.append(cal.pop(-2) + cal.pop())
print(cal)

print(len('952*+1+33*7*6*9*1*7*+1+86*+61*1*5*2*4*7*+43*8*2*6*+78*4*5*+3+7+2+6+5+1+7+6+73*6*+2+6+62*+4+22*+49*3'))