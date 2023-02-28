dic = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9}

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr_b = [[0]*M for _ in range(N)]

    while True:

        for i in range(N):
            for j in range(M):
                li = []
                num = int(arr[i][j], 16)
                for k in range(3, -1, -1):
                    bit = 1 if num&(1<<k) else 0
                    li.append(bit)
                arr_b[i][j] = li


        ans = []
        for i in range(N):
            for j in range(M):
                if arr_b[i][j] != [0, 0, 0, 0]:

                    for k in range(4):
                        ans.append(arr_b[i][j][k])

            if len(ans) != 0:
                break
        c = 0
        while True:
            for p in range(N):
                p1 = p
                for q in range(M):
                    if arr_b[p1][q] == [0, 0, 0, 0]:
                        q += 1
                    else:
                        arr_b[p1][q] = [0, 0, 0, 0]
                        p1 = p
                        q += 1
                        if arr_b[p1][q] == [0, 0, 0, 0]:
                            c = 1
                            break
                if c == 1:
                    break
            if c == 1:
                break

        s = '000'
        for i in range(len(ans)):
            s += str(ans[i])

        for i in range(len(s)-1, 50,  -1):
            if s[i] == '1':
                temp = (s[i-55:i+1])
                break
        print(temp)

        res = []
        for i in range(0, 50, 7):
            if str(temp[i:i + 7]) in dic:
                # print(dic[code[0:7]])
                res.append(dic[temp[i:i + 7]])

        val = 0
        val2 = 0
        for i in range(0, 7, 2):  # 0, 2, 4, 6
            val += res[i] * 3
            val2 += res[i + 1]
        if (val + val2) % 10 == 0:
            answer = val // 3 + val2
        else:
            answer = 0

        answer += answer

        flag = 0
        for i in range(N):
            for j in range(M):
                if arr_b[i][j] != [0, 0, 0, 0]:
                    flag = 1
        if flag == 0:
            break

    print(f'#{test_case}', answer)
    # ans = ''
    # for i in range(len(temp)):
    #     ans.append(temp[i])
    #     if (i+1) % 7 == 0:
    #         ans.append(' ')
    #
    # print(*ans)
