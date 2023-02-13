T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    maxV = 0
    for i in str1:          # str1에 있는 글자가 str2에 있으면 count++
        counts = 0
        for j in str2:
            if i == j:
                counts += 1
        if counts > maxV:        # 가장 많이 겹치는 횟수
            maxV = counts
    print(f'#{test_case}', maxV)
