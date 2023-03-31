T = int(input())
for test_case in range(1, T + 1):
    s = list(map(int, input()))
    ans = ''
    # s.sort()
    only = []
    for x in s:
        if x not in only:
            only.append(x)
    flag = 0
    # for i in range(len(s) - 2):


    for i in range(len(only) - 2):
        if only[i] + 1 == only[i + 1] and only[i] + 2 == only[i + 2]:
            flag = 1    # 일단 연속인지
            s.remove(only[i])
            s.remove(only[i + 1])
            s.remove(only[i + 2])
            break
    if flag == 1:
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                ans = 'Baby Gin'
    if len(ans) == 0:
        ans = 'Lose'
    print(ans)
