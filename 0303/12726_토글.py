def tg(arr, coor):
    while len(coor):
        v = coor.pop()
        x, y = v[0], v[1]
        if arr[x][y] == 1:
            arr[x][y] = 0
        else:
            arr[x][y] = 1
    return arr

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    k = 1
    while k <= M:
        coor = []
        case = 0
        if M % k == 0:
            case = 1
        for i in range(N):
            for j in range(N):
                if case == 1:
                    coor.append((i, j))
                    tg(arr, coor)
                else:
                    if (i + j + 2) % k == 0:
                        coor.append((i, j))
                        tg(arr, coor)
        k += 1

    counts = 0
    for i in range(N):
        for x in arr[i]:
            if x == 1:
                counts += 1

    print(f'#{test_case}', counts)