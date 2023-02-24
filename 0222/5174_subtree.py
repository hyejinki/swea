def f(n):
    global counts
    if n:           # n이 0이 아닐 때
        counts += 1
        f(c1[n])
        f(c2[n])

T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    counts = 0
    for i in range(E):
        p, k = arr[i*2], arr[i*2+1]     # 두 개씩 잘라서
        if c1[p] == 0:
            c1[p] = k                   # 부모를 인덱스로
        else:                           # 이미 c1에 들어있으면 c2에 넣어
            c2[p] = k
    f(N)
    print(f'#{test_case}', counts)
