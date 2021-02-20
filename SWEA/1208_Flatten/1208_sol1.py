import sys
sys.stdin = open('input.txt')


for i in range(1, 11):

    T = int(input())

    # 1. 순회하며 최대,최소값 찾기, 갭값 구하기 > 2. 갭값이 1보다크면 최대-1,최소+1,카운트+1 >
    # 3. 1,2반복 but 카운트값이 T 값 이상이면 break 그때의 갭값 출력
    # 10개의 테스트케이스
    # for i in range(10):
    # T = 34
    # numbers = '42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96'
    # for i in range(T):
    numbers = list(map(int, input().split()))
    count = 0
    gap = 1000
    highest = numbers[0]
    lowest = numbers[0]
    for j in range(T):
        if gap > 1:
            for idx in range(len(numbers)):
                if numbers[idx] > highest:
                    highest = numbers[idx]

                if numbers[idx] < lowest:
                    lowest = numbers[idx]

            numbers.remove(highest)
            numbers.remove(lowest)

            # print(highest, lowest)
            gap = highest - lowest
            # print(gap)

            highest -= 1
            lowest += 1
            count += 1
            numbers.append(highest)
            numbers.append(lowest)
            if count >= T:
                # print(gap, '카운트 끝')
                break
            # elif gap <=1:
            #     print('dkdkdk')
            else:
                # print("카운트 끝이 아니다")
                continue
            # continue
        else:
            print('#{} {}'.format(i, gap))
            break
    print('#{} {}'.format(i, gap))
