def check(p):
    p.sort()
    new = list(set(p))
    for i in range(len(new) - 2):     # 테케로 '1 2 2 3' 들어오면 run인지 확인 불가함!                #
        if new[i] + 1 == new[i + 1] and new[i] + 2 == new[i + 2]:
            return 1
    temp = [0] * (max(p) + 1)
    for i in range(len(p)):
        temp[p[i]] += 1
    for x in temp:
        if x == 3:
            return 1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(arr[i])
            if len(p1) >= 3:
                if check(p1) == 1:
                    winner = 1
        else:
            p2.append(arr[i])
            if len(p2) >= 3:
                if check(p2) == 1:
                    winner = 2
        if winner!= 0:
            break
    print(f'#{test_case}', winner)