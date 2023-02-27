dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
       '0110111': 8, '0001011': 9}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    code = ''
    ans = 0
    arr = [list(map(int, input())) for _ in range(N)]
    i = 0
    while ans == 0:
        for j in range(M - 1, -1, -1):
            if arr[i][j] == 1:  # 뒤에서부터 1 찾았어
                for k in range(j - 55, j + 1):
                    code += str(arr[i][k])
                ans = 1
            if ans == 1:
                break
        i += 1

    res = []
    for i in range(0, 50, 7):
        if code[i:i + 7] in dic:
            # print(dic[code[0:7]])
            res.append(dic[code[i:i + 7]])

    val = 0
    val2 = 0
    for i in range(0, 7, 2):  # 0, 2, 4, 6
        val += res[i] * 3
        val2 += res[i + 1]
    if (val + val2) % 10 == 0:
        answer = val // 3 + val2
    else:
        answer = 0

    print(f'#{test_case}', answer)